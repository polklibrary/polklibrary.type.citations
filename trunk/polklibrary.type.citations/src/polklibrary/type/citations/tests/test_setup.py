# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from polklibrary.type.citations.testing import POLKLIBRARY_TYPE_CITATIONS_INTEGRATION_TESTING  # noqa
from plone import api

import unittest


class TestSetup(unittest.TestCase):
    """Test that polklibrary.type.citations is properly installed."""

    layer = POLKLIBRARY_TYPE_CITATIONS_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if polklibrary.type.citations is installed with portal_quickinstaller."""
        self.assertTrue(self.installer.isProductInstalled('polklibrary.type.citations'))

    def test_browserlayer(self):
        """Test that IPolklibraryTypeCitationsLayer is registered."""
        from polklibrary.type.citations.interfaces import IPolklibraryTypeCitationsLayer
        from plone.browserlayer import utils
        self.assertIn(IPolklibraryTypeCitationsLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = POLKLIBRARY_TYPE_CITATIONS_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['polklibrary.type.citations'])

    def test_product_uninstalled(self):
        """Test if polklibrary.type.citations is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled('polklibrary.type.citations'))

    def test_browserlayer_removed(self):
        """Test that IPolklibraryTypeCitationsLayer is removed."""
        from polklibrary.type.citations.interfaces import IPolklibraryTypeCitationsLayer
        from plone.browserlayer import utils
        self.assertNotIn(IPolklibraryTypeCitationsLayer, utils.registered_layers())
