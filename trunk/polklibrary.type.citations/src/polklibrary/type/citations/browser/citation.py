from plone import api
from plone.dexterity.browser import add
from Products.Five import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

class CitationView(BrowserView):

    template = ViewPageTemplateFile("citation_view.pt")
    
    next_url = ''
    
    def __call__(self):
        self.next_url = ''
        container = self.context.aq_parent
        brains = api.content.find(context=container, 
                                  depth=1, 
                                  portal_type='polklibrary.type.citations.models.citation',
                                  sort_on='getObjPositionInParent', 
                                  sort_order='ascending'
                                  )
        
        next = False
        for brain in brains:
            if next:
                self.next_url = brain.getURL()
                break
            if brain.UID == self.context.UID():
                next = True
                
        return self.template()

    @property
    def portal(self):
        return api.portal.get()
        
        
class CitationManager(BrowserView):

    template = ViewPageTemplateFile("citation_manager.pt")
    
    title = ''
    json_data = ''
    body = ''
    action = ''
    
    def __call__(self):
        self.action = self.context.absolute_url() + '/++add++polklibrary.type.citations.models.citation'
        if self.context.portal_type == 'polklibrary.type.citations.models.citation':
            self.title = self.context.title
            self.json_data = self.context.json_data
            self.body = self.context.body.output
            self.action = self.context.absolute_url() + '/edit'
        return self.template()

    @property
    def portal(self):
        return api.portal.get()
        
    