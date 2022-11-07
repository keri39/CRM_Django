import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import warnings


class ll_ATS(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome("/Users/abhishekkeri/mfscrm/tests/chromedriver")
        warnings.simplefilter('ignore', ResourceWarning)

    def test_ll(self):
        driver = self.driver
        driver.maximize_window()
        driver.get("http://127.0.0.1:8000")
        time.sleep(5)
        elem = driver.find_element(By.XPATH, '//*[@id="myNavbar"]/ul[2]/li/a').click()


        user = "keri39"  # must be a valid username for the application
        pwd = "3950"  # must be the password for a valid user
        elem = driver.find_element(By.ID, "id_username")
        elem.send_keys(user)
        elem = driver.find_element(By.ID, "id_password")
        elem.send_keys(pwd)
        elem.send_keys(Keys.RETURN)
        time.sleep(5)
        elem = driver.find_element(By.XPATH, '//*[@id="myNavbar"]/ul[1]/li[5]/a').click()
        time.sleep(5)
        try:
            elem = driver.find_element(By.XPATH, '//*[@id="app-layout"]/div[2]/div/div[3]/table/tbody/tr/td[9]/a')
            print("Test passed - Product list displayed")
            assert True
        except NoSuchElementException:
            self.fail("Product List does not appear when Customers is clicked - test failed")


def tearDown(self):
    self.driver.close()


if __name__ == "__main__":
    unittest.main()
