from time import sleep
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from libreries import elements

def scroll_propierty (self, driver, locator_type, locator_value, delay):
    tag_goal = elements.get_element(self, locator_type, locator_value)
    print(tag_goal.text)
    ActionChains(driver)\
       .scroll_to_element(tag_goal)\
       .perform()
    sleep(delay)

def click_propierty(self, locator_type, locator_value):
   click_element = elements.get_element(self, locator_type, locator_value)
   elements.highlight(self, locator_type, locator_value)
   click_element.click()




