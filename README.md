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
    
 7.  If you want to see a Basic Report, you can excecute the next command
    
     `pytest <scenario_name>.py --html=report.html`

     When you execute this command, in path that you are, you can see a new file with `report.html` name, and if you open with any browser, you will see an image like following:
    
<p align="center" width="200%">
<img width="70%" src="https://i.postimg.cc/SNhG0MbD/Report-image.png">
</p>

 **Note**
  If you want to learn more about the pytest reports, go to the https://pypi.org/project/pytest-html/ 
 
 8.  Now We are going to do Behave test, that it was installed with the requirements, executing the following commmand

   `behave .\behave\features\scenario1.feature`

For to test the first scenario or for the second scenario we can execute the following command

   `behave .\behave\features\scenario1.feature`


 10.  For to finish we can deactivate the virtual environment
    `deactivate`


### Now, we are going to use the Postman and Jmeter Tools, these tools are normally used for API Test

In this repository, you can find the API Tools folder, inside the folder, you are goin to find two folders more, the first one is JMeter Scenarios and the second one is Postman Scenarios, inside them, there is one file by folder, those files are compatible only with the API tool that contain them. So, you need to download the last version of the Postman and Jmeter for the use them, these tools you can download in the follow links:

https://www.postman.com/downloads/

https://jmeter.apache.org/download_jmeter.cgi

Well each file have two scenarios:

- Scenario 3: User can login
  
   Use the following link and builds the corresponding requests to login
  
   https://the-internet.herokuapp.com/login

- Scenario 4: User can upload file
  
  Use the following link and uploads any file to the webapp
  
  https://the-internet.herokuapp.com/upload

  The instrutions to execute or open the files are simple, for JMeter you need to open Test Plan.jmx file and in Postman you need to import the Postman Automation.postman_collection.json file, the Scenario 4  needs that you explore and find one file into your computer, this requirement is necesario to Scenario goal, for that please follow instructions:

## Postman

In Postman you need to replace the exits PATH, like this
<p align="center" width="200%">
<img width="60%" src="https://i.postimg.cc/bwnxm7gD/Postman1.png">
</p>


<p align="center" width="200%">
<img width="60%" src="https://i.postimg.cc/Wpf0TNfq/Postman2.png">
</p>


<p align="center" width="200%">
<img width="60%" src="https://i.postimg.cc/fTGXSHsw/Postman3.png">
</p>

After this you can run the test by clicking on the send button.

## JMeter

For JMeter, only you need to change the image PATH, by a full path of an image that exists on your computer

<p align="center" width="200%">
<img width="60%" src="https://i.postimg.cc/dt62pRcv/JMeter1.png">
</p>

After this you can run the test by clicking on the play green button

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

### What's the BDD paradigm
   Behaviour Driven Development (BDD) is a synthesis and refinement of practices stemming from Test Driven Development (TDD) and Acceptance Test Driven Development (ATDD). BDD augments TDD and ATDD with the following tactics:

- Apply the “Five Why’s” principle to each proposed user story, so that its purpose is clearly related to business outcomes
- Thinking “from the outside in”, in other words, implement only those behaviors which contribute most directly to these business outcomes, so as to minimize waste
- Describe behaviors in a single notation that is directly accessible to domain experts, testers, and developers, so as to improve communication
- Apply these techniques all the way down to the lowest levels of abstraction of the software, paying particular attention to the distribution of behavior, so that evolution remains cheap
  
  


### References
 
 - https://www.selenium.dev/documentation/test_practices/encouraged/page_object_models/
 - https://www.guru99.com/page-object-model-pom-page-factory-in-selenium-ultimate-guide.html
 - https://pypi.org/project/webdriver-manager/
 
    
    
