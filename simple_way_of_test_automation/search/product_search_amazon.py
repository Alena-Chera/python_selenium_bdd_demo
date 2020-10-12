"""
Web test cases for Amazon search functionality
Users can enter search product and get results page with list of matching products.

Test procedure:
1.	Navigate to the Amazon home page
2.	Enter the search product
3.	Verify that results page for search product opened

Feature: Search product on Amazon
Scenario: Basic Amazon Search

"""
from selenium import webdriver
from selenium.webdriver.common.by import By

# Initialize the ChromeDriver instance
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

# Maximize window
driver.maximize_window()

# Wait implicitly for elements to be ready before attempting interactions
driver.implicitly_wait(10)

# Given the Amazon page is displayed
driver.get('https://www.amazon.com/')

# When the user searches for "tablet"

# input search word and click ENTER key
search_keyword = 'tablet'
driver.find_element(By.ID, "twotabsearchtextbox").send_keys(search_keyword + Keys.ENTER)

# OR
# input search word and click search button, find this element by NAME
# driver.find_element(By.ID, "twotabsearchtextbox").send_keys(search_keyword)
# driver.find_element(By.NAME, "site-search").submit()

# OR
# input search word and click search button, find this element by CSS_SELECTOR using argument value
# driver.find_element(By.ID,"twotabsearchtextbox").send_keys("tablet")
# driver.find_element(By.CSS_SELECTOR, "input.nav-input[value='Go']").click()


# Then results page for "tablet" opened
search_word_on_results_page = driver.find_element(By.CSS_SELECTOR, "span.a-color-state.a-text-bold").text
assert search_keyword in search_word_on_results_page

# Quit the WebDriver instance for the cleanup
driver.quit()

