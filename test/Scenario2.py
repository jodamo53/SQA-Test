from libreries.webdriver import Webdriverconf
from page.googlesearch import GoogleSearch

class Scernario2(Webdriverconf):
    def test2(self):
        driver = self.driver
        self.driver.get(GoogleSearch.get_url(self))
        search = GoogleSearch(driver)
        search.click_search()
        search.click_on_first_link()
        search.page_title_confirm()
