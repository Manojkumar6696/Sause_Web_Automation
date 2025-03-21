"""
Test the SauseWebsite using pytest with testcases
"""

#import necessary modules

from SauseWeb_task import Chrome_automate

url="https://www.saucedemo.com/"

#creating object from sause web task class

my_Automation = Chrome_automate(url)

class TestAutomation:

# creating method to test positive url

    def test_positive_url(self):
        expected_url="https://www.saucedemo.com/inventory.html"
        actual_url=my_Automation.fetch_url()
        assert expected_url==actual_url
        print("Success: Test Url passed")

# creating method to test negative url

    def test_negative_url(self):
        expected_url="https://www.google.in/"
        actual_url=my_Automation.fetch_url()
        assert expected_url!=actual_url
        print("Success: Test Negative Url passed")

# creating method to test homepage positive url

    def test_homepage_positive_url(self):
        expected_url="https://www.saucedemo.com/"
        actual_url=my_Automation.Homepage_url()
        assert expected_url==actual_url
        print("Success: Test homepage Positive Url passed")

# creating method to test homepage negative url

    def test_homepage_negative_url(self):
        expected_url="https://www.google.in/"
        actual_url=my_Automation.Homepage_url()
        assert expected_url!=actual_url
        print("Success: Test homepage Negative Url passed")

# creating method to test positive title

    def test_positive_title(self):
        expected_title="Swag Labs"
        actual_title=my_Automation.fetch_title()
        assert expected_title==actual_title
        print("Success: Test Positive title passed")

# creating method to test negative title

    def test_negative_title(self):
        expected_title="Swiggy"
        actual_title=my_Automation.fetch_title()
        assert expected_title!=actual_title
        print("Success: Test Negative title passed")

# creating method to write a webpage content in text file

    def test_write(self):
        my_Automation.write()

