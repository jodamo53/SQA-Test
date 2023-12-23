import os
from behave import given, when, then
from libreries.webdriver import Webdriverconf
from page.googlesearch import GoogleSearch
from libreries.drivers import browser_drivers
#import pdb

class GoogleSearchSteps(Webdriverconf):

    @given(u'I Search by keyword')
    def step_impl(context):
        context.driver = browser_drivers(os.environ['BROWSER_NAME'])
        context.driver.maximize_window()
        context.url = GoogleSearch.get_url(context)
        context.driver.get(context.url)
        context.load = GoogleSearch(context.driver)
        context.load.click_search()

    @when(u'I click on the first result link')
    def step_impl(context):
        context.load.click_on_first_link()

    @then(u'I go to the page, and the page title contains the word “automation”')
    def step_impl(context):
        context.load.page_title_confirm()