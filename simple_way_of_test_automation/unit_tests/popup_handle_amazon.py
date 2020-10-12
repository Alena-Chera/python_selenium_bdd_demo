"""
         Python webdriver to handle pop up browser windows which is not an alert
"""

import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class AmazonBestSellerExample(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://www.amazon.com/')

    def tearDown(self):
        self.driver.quit()

    def test_find_tablet(self):
        driver = self.driver
        wait = WebDriverWait(driver, 5)

        # Search for "tablet"
        search_keyword = 'tablet'
        driver.find_element(By.ID, "twotabsearchtextbox").send_keys(search_keyword + Keys.ENTER)
        # OR
        # driver.find_element(By.ID,"twotabsearchtextbox").send_keys("tablet")
        # driver.find_element(By.NAME, "site-search").submit()
        # driver.find_element(By.ID,"twotabsearchtextbox").send_keys("tablet")
        # driver.find_element(By.CSS_SELECTOR, "input.nav-input[value='Go']").click()

        # Click on first matching result
        first_product = driver.find_elements(By.CSS_SELECTOR, "a.a-link-normal.s-no-outline")[0]
        first_product.click()

        # Click add to cart button
        wait.until(expected_conditions.presence_of_element_located((By.ID, "add-to-cart-button"))).click()

        # Close popup if it appears
        if driver.find_elements(By.ID, 'a-popover-1') and driver.find_element(By.ID, 'a-popover-1').is_displayed():
            driver.find_element_by_css_selector('#a-popover-1 .a-button-close').click()


if __name__ == '__main__':
    unittest.main()
