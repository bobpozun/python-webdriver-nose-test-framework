#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import time
import libs.webdriverhelper #not used currently, will store repeatable methods here

from nose.tools import istest
from nose.plugins.attrib import attr
from libs.atestclass import ATestClass


class Basic(ATestClass):
    """Basic Test Class"""

    @istest
    @attr('smoke', 'regression')
    def open_page(self):
        """Example test method. Opens test webpage and waits 10 seconds."""
        self.driver.get(self.app_url)
        time.sleep(10)