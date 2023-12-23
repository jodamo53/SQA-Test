import os
from behave import given, when, then
from libreries.webdriver import Webdriverconf
from page.googlesearch import GoogleSearch
from libreries.drivers import browser_drivers

class GoogleSearchSteps(Webdriverconf):

    @given(u'Launch the Browser on the Google Home Page')
    def step_impl(context):
        context.driver = browser_drivers(os.environ['BROWSER_NAME'])
        context.driver.maximize_window()
        context.url = GoogleSearch.get_url(context)
        context.driver.get(context.url)
        context.load = GoogleSearch(context.driver)

    @when(u'I type the word "test automation"')
    def step_impl(context):
        context.load.write_text_to_search()

    @when(u'I click on the Search Buttom, I go to the search page')
    def step_impl(context):
        context.load.click_on_search_button()

    @then(u'I confirm the first 3 result contain the word "automation"')
    def step_impl(context):
        context.load.confirm_searched_text()
