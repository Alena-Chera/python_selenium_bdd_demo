"""
Web test cases for Amazon add product to cart functionality
Users can enter search product and add product to cart

Test procedure:
1.	Navigate to the Amazon home page
2.	Enter the search product
3.	Select first product from results page
4. When product page is open edd product to cart. Close pop up if it appears.

Feature: Search product on Amazon
Scenario: Basic Amazon Search

"""
from selenium import webdriver
from selenium.webdriver.common.by import By

# Initialize the ChromeDriver instance
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

# Maximize window
# We try to stay our test more stable - we open the window for full size
# to make sure that user actually works with a full screen
driver.maximize_window()

# Make its calls wait up to 10 seconds for elements to appear
# (Wait implicitly for elements to be ready before attempting interactions)
driver.implicitly_wait(10)

# Given the Amazon page is displayed
driver.get('https://www.amazon.com/')

# When the user searches for "tablet"
search_keyword = 'tablet'
driver.find_element(By.ID, "twotabsearchtextbox").send_keys(search_keyword + Keys.ENTER)
# OR
# driver.find_element(By.ID,"twotabsearchtextbox").send_keys("tablet")
# driver.find_element(By.NAME, "site-search").submit()
# driver.find_element(By.ID,"twotabsearchtextbox").send_keys("tablet")
# driver.find_element(By.CSS_SELECTOR, "input.nav-input[value='Go']").click()

# Then results page for "tablet" opened
search_word_on_results_page = driver.find_element(By.CSS_SELECTOR, "span.a-color-state.a-text-bold").text
assert search_keyword in search_word_on_results_page

# Quit the WebDriver instance for the cleanup
driver.quit()
