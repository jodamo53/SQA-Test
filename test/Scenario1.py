from libreries.webdriver import Webdriverconf
from page.googlesearch import GoogleSearch

class Scenario(Webdriverconf):
    def test1(self):
        driver = self.driver
        self.driver.get(GoogleSearch.get_url(self))
        search = GoogleSearch(driver)
        search.click_search()
        search.confirm_searched_text()
