"""
Perform automation in Chrome browser
Launch the Sause Demo site
Fetch the title and url
Quit the browser instance


"""

# import all the necessary dependencies
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By

class Chrome_automate:
    # Test Data
    username = "standard_user"
    password = "secret_sauce"

    # Test Locators
    username_locator = 'user-name'  # name
    password_locator = 'password'  # name
    button_locator = 'login-button'  # ID


    def __init__(self, url):
       self.url = url
       self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    # creating method to start automation
    def start_automation(self):
    # exception handling
        try:
            self.driver.get(self.url)
            self.driver.maximize_window()
            return True
        except:
            print("Error: Unable to start the automation")
            return False

    #creating method to quit the browser instances
    def shutdown(self):
        self.driver.quit()

    # creating method to login webpage

    def login_automation(self):

        self.start_automation()
        # fill the username
        self.driver.find_element(by=By.NAME, value=self.username_locator).send_keys(self.username)

        # fill the password
        self.driver.find_element(by=By.NAME, value=self.password_locator).send_keys(self.password)

        # click the login button
        self.driver.find_element(by=By.ID, value=self.button_locator).click()
        sleep(5)
        return self.driver.current_url

    # Extract the entire content from webpage
    def write(self):
        self.login_automation()
        page_content = self.driver.page_source
        print(page_content[:500])

        with open('Webpage_task_11.txt', 'w', encoding='utf-8') as file:
            file.write(page_content)
        print("content successfully saved")

    # creating method to fetch url

    def fetch_url(self):
        if self.login_automation():
            return self.driver.current_url
        else:
            print("Error: unable to fetch the url")

    # creating method to fetch homepage url
    def Homepage_url(self):
        if self.start_automation():
            return self.driver.current_url
        else:
            print("Error: unable to fetch the url")

    # creating method to fetch title:
    def fetch_title(self):
        if self.login_automation():
            return self.driver.title
        else:
            print("Error: unable to fetch the title")
            return False

