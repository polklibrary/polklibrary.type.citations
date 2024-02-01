from plone import api
from plone.app.textfield import RichText
from plone.supermodel import model
from zope import schema
from zope.interface import directlyProvides
from zope.schema.interfaces import IContextSourceBinder
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm

message_types = SimpleVocabulary([
    SimpleTerm(value=u'Book', title=u'Book'),
    SimpleTerm(value=u'Magazine', title=u'Magazine'),
    SimpleTerm(value=u'Newspaper', title=u'Newspaper'),
    SimpleTerm(value=u'Journal Article', title=u'Journal Article'),
    SimpleTerm(value=u'Website', title=u'Website'),
    SimpleTerm(value=u'Film', title=u'Film'),
    SimpleTerm(value=u'Interview', title=u'Interview'),
])

class ICitation(model.Schema):

    title = schema.TextLine(
            title=u"Citation",
            required=True,
        )
        
    body = RichText(
            title=u"Information about this citation",
            default_mime_type='text/structured',
            required=False,
            default=u"",
        )
    
    json_data = schema.Text(
            title=u"Json Data",
            required=False
        )
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        