# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
import time, unittest

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class draft(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
    
    def test_draft(self):
        success = True
        wd = self.wd
        wd.get("http://localhost/addressbook/")
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").send_keys("\\undefined")
        wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()
        if not wd.find_element_by_id("27").is_selected():
            wd.find_element_by_id("27").click()
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        wd.find_element_by_link_text("home").click()
        wd.find_element_by_link_text("Logout").click()
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").send_keys("\\undefined")
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").send_keys("\\undefined")
        self.assertTrue(success)
    
    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
