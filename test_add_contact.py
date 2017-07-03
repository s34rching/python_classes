# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
import unittest
from contact import Contact

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class test_add_contact(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)

    def test_add_contact(self):
        self.login(username="admin", password="secret")
        self.create_new_contact(Contact(firstname="Test", middlename="Test", lastname="Test", nickname="test_contact1", address="some address, 1", home_number="+375293003030",
                                mobile_number="+375294004040"))
        self.logout()

    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
