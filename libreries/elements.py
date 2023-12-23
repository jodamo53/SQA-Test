import time
from selenium.webdriver.common.by import By

def get_element (self, locator_type, locator_value):
    time.sleep(0.5)
    if str(locator_type).upper() == "ID":
        by = By.ID
    elif str(locator_type).upper() == "CSS":
        by = By.CSS_SELECTOR
    elif str(locator_type).upper() == "XPATH":
        by = By.XPATH
    return self.driver.find_element(by, locator_value)

def wait_unitl_visible_element(self, locator_type, locator_value):

    element = get_element(self, locator_type, locator_value)
    if element.is_displayed():
        return print("\n The Text is in the link")
    else:
        return print("\n The Text is NOT in the link")

def highlight(self, locator_type, locator_value):
    element = get_element (self, locator_type, locator_value)
    try:
        def apply_style(s):
            self.driver.execute_script("arguments[0].setAttribute('style', arguments[1]);", element, s)
        original_style = element.get_attribute('style')
        apply_style("background: green; border: 1px solid yellow;")
        time.sleep(0.5)
        apply_style(original_style)
    except:
        return

