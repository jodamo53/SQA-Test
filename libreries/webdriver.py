import unittest
import os
from libreries.drivers import browser_drivers

class Webdriverconf (unittest.TestCase):
    def setUp(self):
        print(os.environ['BROWSER_NAME'])
        self.browser_name = os.environ['BROWSER_NAME']
        self.driver = browser_drivers(self.browser_name)
        self.driver.maximize_window()
        return self.driver

    def tearDown(self):
        if self.driver is not None:
            self.driver.quit()