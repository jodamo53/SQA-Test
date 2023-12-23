# QA Automation Test

## Overview
This project was created using tools to Automation Testing on Web Application, the tools used were Selenium WebDriver, Pytest , WebDriver Manager following the Page Object Model pattern and using the environment variables


## Setup Instructions
If you know how to clone a repository from github please do it, If you don’t know how do yo do it, please go the following page https://docs.github.com/es/repositories/creating-and-managing-repositories/cloning-a-repository


1.	Install Python 3.9 or above
2.	Is a good practice to have a virtual environment for each project, with this we can guarantee that a repository after setup it works good, now for to create our own virtual environment we use the following instruction:
    #### Windows Users
    - In your PowerShell terminal we create our virtual environment
    
      `python -m venv <virtual_environment>`
      
    - We activate our virtual environment
    
      `<virtual_environment>/Scripts/activate`
    
    #### MAC Users
    
    - In your terminal we create our virtual environment
    
      `pyenv virtualenv <virtual_environment>`
    
    - We activate our virtual environment
    
      `pyenv activate <name of venv>`
    
3. Now with the virtual environment activated we need to go to the where we clone this repository, and then enter path Page Object Model folder
    
    `/user_path/PageObjectModel/`
    
4. Now we need to install of the requirements with the following command
    
    `pip install -r requirements.txt`
    
5. Then we are gonna set one environment variable that we will use for to open own browser, this project was created for to be used with Chrome, Firefox and Edge browsers, only we need to change the browser name in the following command

   #### Windows Users

      `[Environment]::SetEnvironmentVariable('BROWSER_NAME', 'chrome')`
    
   #### MAC Users
  
      `export BROWSER_NAME=chrome`
      
    
  
   ***Note:***
    
   We can change the browser name for firefox, edge or chrome.
  
6.	Now we can use the pytest framework, that it was installed with the requirements, executing the following commmand

    `pytest .\Test\test_Scenario1.py`
    
    For to test the first scenario or for the second scenario we can execute the following command
    
    `pytest .\Test\test_Scenario2.py`
    
    Or only executing the following command we can execute both scenarios
    
    `pytest`
 
 7.  For to finish we can deactivate the virtual environment
    `deactivate`
 
## Definitions

### What's POM or Page Object Model?

Page Object Model is a design pattern, nowadays is widely used for in test automation that permite to keep organized all our code in a skeleton folders and files totally identified that help us to reduce code duplication and improve our test cases, following I show you how is the skeleton of the POM:

<p align="center" width="100%">
<img width="40%" src="https://i.postimg.cc/mDqNnPJz/POM-pattern.jpg">
</p>

#### Advantages of using POM

- It's easier to maintain the code. Any changes to the UI will be reflected wherever it is used in the class.
- It's robust and readable
- Makes code reusable and reduces code duplication
- Code becomes less and optimized because of the reusable


### What's Selenium?
Selenium refers to a suite of tools that are widely used in the testing community when it comes to cross-browser testing, doesn't support desktop applications and can only be used in browsers. Nowadays is considereted like one the best tool suite for the automation testing.
It supports a number of browsers like Chrome, Safari, Firefox and opera among others, also is compatible with diferents operating system like Windows, Mac and Linux/Unix.
It compatible with different programming languages like C#, Java, JavaScript, Ruby, Python, PHP.

#### Selenium Components
The selenium test suite have four main components:
<p align="center" width="100%">
<img width="60%" src="https://i.postimg.cc/SQvdy6bt/Selenium-Suite.png">
</p>

- **Selenium IDE** is an Add-on available in the Firefox and Chrome browsers, and help us to do a quickly test  through its functionality recording step by step for after to do playback it, for this you don't need to know any programming lenguage because Selenium IDE does it for you.
- **Selenium RC** is a tool allows you develop responsive desing test in any scripting language of your preference, nowadays is hardly used for its complex architecture and its limitantions.
- **Selenium WebDriver** is a web framework that permits you to execute cross-browser tests. This tool is used for automating web-based application testing to verify that it performs expectedly.
- **Selenium Grid** is a tool that is used for concurrent execution of test cases on different browsers, machines, and operating systems simultaneously.


### What's the WebDriver Manager?
WebDriver Manager is a great library sponsored by Python Software Foundation that its first idea is to simplify management of binary drivers for different browsers and with that headache that is generated due to the constant updating of the web browsers, for each web browser version there is a web driver, so thanks to the webdriver manager, that is over!!!

WebDriver Manager is compatible with Selenium 4.x  and below, and support the following web browsers:

- Chrome
- Firefox
- Internet explorer and Edge
- Opera
- Brave

Before you needed to download the binary driver, unzip it somewhere on your PC and set the path to this driver according to the browser, now and thanks to WebDriver Manager you do the following:

 - First you install the web driver manager
 
   `pip install webdriver-manager`
       
 - And then for example for to install the webdriver on chrome browser you do this
 
   ``` 
     from selenium import webdriver
     from selenium.webdriver.chrome.service import Service as ChromeService
     from webdriver_manager.chrome import ChromeDriverManager

     driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
   ```
   
   **Note**
   
   If you want to know more about the WebDriver Manager, you can check its documentation [here](https://pypi.org/project/webdriver-manager/).


### References
 
 - https://www.selenium.dev/documentation/test_practices/encouraged/page_object_models/
 - https://www.guru99.com/page-object-model-pom-page-factory-in-selenium-ultimate-guide.html
 - https://pypi.org/project/webdriver-manager/
 
    
    
