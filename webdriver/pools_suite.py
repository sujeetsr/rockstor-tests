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
from pools_create_raid0_2disks import PoolsCreateRaid02Disks

if __name__ == '__main__':
    suite = unittest.TestSuite([\
            unittest.TestLoader().loadTestsFromTestCase(\
            PoolsCreateRaid02Disks)])
    unittest.TextTestRunner(verbosity=2).run(suite)


