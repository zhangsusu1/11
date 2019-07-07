from appium import webdriver
from selenium.webdriver.common.by import By
import xlrd
import sys
import time
import os
#import xlrd
import unittest
from appium import webdriver
from test_case import quit
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
#class MyUnitTest(unittest.TestCase):
#def setUp(self):
class Anewnotes(unittest.TestCase):
    def setUp(self):
        desired_caps = {
        'platformName': 'Android',
        'deviceName': '3HX5T17427013396',
        'platformVersion': '8.0.0',
        'appPackage': 'com.panda.videoliveplatform',
        'appActivity': 'com.panda.videoliveplatform.activity.WelcomeActivity',
        'unicodeKeyboard':'True',
        'resetKeyboard':'True'
        }
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    def test_newnotes(self):
        time.sleep(10)
        driver=self.driver
        wd=xlrd.open_workbook("D:\\document\\daima\\data\\data.xls")
        #driver.find_element(By.NAME,'星秀').click()
        time.sleep(10)
        driver.find_element(By.NAME,'新人').click()
        base_path=os.path.dirname(__file__)
        print(base_path)
        path=base_path.replace("test_case","image/xingr.png")
        self.driver.get_screenshot_as_file(path)
        driver.find_element(By.ID,'com.panda.videoliveplatform:id/iv_back').click()
        driver.find_element(By.NAME,'小视频').click()
        driver.find_element(By.ID,'com.panda.videoliveplatform:id/iv_back').click()
        driver.find_element(By.NAME,'排行榜').click()
        time.sleep(5)
        driver.find_element(By.NAME,'明星主播榜').click()
        driver.find_element(By.NAME,'富豪实力榜').click()
        driver.find_element(By.NAME,'竹子收割机').click()
        driver.find_element(By.ID,'com.panda.videoliveplatform:id/toolbar_back').click()
        driver.find_element(By.ID,'com.panda.videoliveplatform:id/iv_follow').click()
    def tearDown(self):
        quit.logout(self)
if __name__=='main':
     unittest.main()
























































































