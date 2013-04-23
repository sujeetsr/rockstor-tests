from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
import unittest, time, re
import yaml
import sys, getopt
from rockstor_testcase import RockStorTestCase

class Login(RockStorTestCase):
    def test_login(self):
        # Login
        driver = self.driver
        driver.get(self.base_url + "/login_page")
        driver.find_element_by_id("inputUsername").clear()
        driver.find_element_by_id("inputUsername").send_keys("admin")
        driver.find_element_by_id("inputPassword").clear()
        driver.find_element_by_id("inputPassword").send_keys("admin")
        driver.find_element_by_id("sign_in").click()

        # Check that the dashboard title is displayed
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "widgets-container")))
        dashboard_title = driver.find_element_by_id("title")
        self.assertRegexpMatches(dashboard_title.text, r"^[\s\S]*System Dashboard[\s\S]*$")
        
        # logout
        driver.find_element_by_id("logout_user").click()

if __name__ == '__main__':
    unittest.main()

