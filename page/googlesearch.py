import time
from libreries import elements, mouse_propierties
from selenium.webdriver.common.by import By

url = 'https://www.google.com'

class GoogleSearch:

    def __init__(self, driver):
        self.driver = driver
        self.text_to_search = "test automation"
        self.text_to_confirm = "automation"
        self.input_text_name = "q"
        self.search_button = "btnK"
        self.link1 = "#rso > div:nth-child(3) > div > div > div.kb0PBd.cvP2Ce.jGGQ5e > div > div > span > a > h3"
        self.link2 = "/html/body/div[5]/div/div[10]/div[1]/div[2]/div[2]/div/div/div[4]/div/div/div[1]/div/div/span/a/h3"
        self.link3 = "/html/body/div[5]/div/div[10]/div[1]/div[2]/div[2]/div/div/div[5]/div/div/div[1]/div/div/span/a/h3"

    def open_browser(self):
        return self.driver.get(url)

    def write_text_to_search(self):
        self.write_text = self.driver.find_element(By.NAME, self.input_text_name)
        self.write_text.send_keys(self.text_to_search)
        return

    def click_on_search_button(self):
        time.sleep(3)
        self.driver.find_element(By.NAME, self.search_button).click()
        return

    def search(self):
        return self.driver.find_element(By.NAME, self.input_text_name)

    def click_search(self):
        self.search().send_keys(self.text_to_search)
        time.sleep(2)
        self.driver.find_element(By.NAME, self.search_button).click()
        return

    def confirm_searched_text(self):
        elements.wait_unitl_visible_element(self, locator_type="CSS", locator_value=self.link1)
        mouse_propierties.scroll_propierty(self, driver=self.driver, locator_type= "CSS", locator_value=self.link1, delay=3 )
        elements.highlight(self, locator_type= "CSS", locator_value=self.link1)
        elements.wait_unitl_visible_element(self, locator_type="XPATH", locator_value=self.link2)
        mouse_propierties.scroll_propierty(self, driver=self.driver, locator_type="XPATH", locator_value=self.link2, delay=3)
        elements.highlight(self, locator_type= "XPATH", locator_value=self.link2)
        elements.wait_unitl_visible_element(self, locator_type="XPATH", locator_value=self.link3)
        mouse_propierties.scroll_propierty(self, driver=self.driver, locator_type="XPATH", locator_value=self.link3, delay=3)
        elements.highlight(self, locator_type="XPATH", locator_value=self.link3)

    def click_on_first_link(self):
        elements.wait_unitl_visible_element(self, locator_type="CSS", locator_value=self.link1)
        mouse_propierties.scroll_propierty(self,driver=self.driver, locator_type="CSS", locator_value=self.link1, delay=3)
        mouse_propierties.click_propierty(self, locator_type="CSS", locator_value=self.link1)

    def page_title_confirm(self):
        time.sleep(3)
        self.page_title = self.driver.title
        print(type(self.page_title))
        assert (self.text_to_confirm in self.page_title.lower())

    def get_url(self):
        return url
