# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import polklibrary.type.citations


class PolklibraryTypeCitationsLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        self.loadZCML(package=polklibrary.type.citations)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'polklibrary.type.citations:default')


POLKLIBRARY_TYPE_CITATIONS_FIXTURE = PolklibraryTypeCitationsLayer()


POLKLIBRARY_TYPE_CITATIONS_INTEGRATION_TESTING = IntegrationTesting(
    bases=(POLKLIBRARY_TYPE_CITATIONS_FIXTURE,),
    name='PolklibraryTypeCitationsLayer:IntegrationTesting'
)


POLKLIBRARY_TYPE_CITATIONS_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(POLKLIBRARY_TYPE_CITATIONS_FIXTURE,),
    name='PolklibraryTypeCitationsLayer:FunctionalTesting'
)


POLKLIBRARY_TYPE_CITATIONS_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        POLKLIBRARY_TYPE_CITATIONS_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='PolklibraryTypeCitationsLayer:AcceptanceTesting'
)
