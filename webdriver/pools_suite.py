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
from inspect import stack
from util import read_conf

class PoolTests(RockStorTestCase):
    def login(self):
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
        
    def test_pools_page_visible(self):
        try:
            self.login()
            self.save_screenshot(stack()[0][3])
            driver = self.driver
            driver.find_element_by_id("pools_nav").click()
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "add_pool")))
        except Exception, e:
            self.save_screenshot(stack()[0][3])
            print e

    def mytest_create_raid0_2disks(self):
        try:
            self.login()
            driver = self.driver
            driver.find_element_by_id("pools_nav").click()
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "add_pool")))
            driver.find_element_by_id("add_pool").click()
            driver.find_element_by_id("pool_name").clear()
            driver.find_element_by_id("pool_name").send_keys("pool1")
            driver.find_element_by_id("sdb").click()
            driver.find_element_by_id("sdc").click()
            driver.find_element_by_id("create_pool").click()
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "pool1")))
        except Exception, e:
            self.save_screenshot(stack()[0][3])
            print e

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(RockStorTestCase.parametrize(PoolTests, 
        screenshot_dir = 'output2'))
    unittest.TextTestRunner(verbosity=2).run(suite)


