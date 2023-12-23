from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager

def browser_drivers(browser_name: str):
    if browser_name.upper() == "CHROME":
        return webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    if browser_name.upper() == "FIREFOX":
        return webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    if browser_name.upper() == "EDGE":
        return webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))