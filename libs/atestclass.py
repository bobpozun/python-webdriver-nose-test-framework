#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import unittest
from selenium import webdriver
from testconfig import config

class ATestClass (unittest.TestCase):
    """Abstract Test Class """

    variables = config['variables']
    app_url = variables['env']
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main()
