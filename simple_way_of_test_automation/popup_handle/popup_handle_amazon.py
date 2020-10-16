"""
           Python webdriver to handle pop up browser windows which is not an alert

Web test cases for Amazon 'add to cart' functionality
Users can enter search product and add product to cart, close pop up if it will appear

Test procedure:
1. Navigate to the Amazon home page
2. Enter the search product
3. Select first product from results page
4. When product page will open edd product to cart. Close pop up if it will appear

Feature: Add to cart
Scenario: Amazon add to cart product, close pop up

"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

# Initialize the ChromeDriver instance
driver = webdriver.Chrome()

# Maximize window
driver.maximize_window()

# Wait implicitly for elements to be ready before attempting interactions
driver.implicitly_wait(10)

# Given the Amazon page is displayed
driver.get('https://www.amazon.com/')

# Search for "tablet", click on first matching result
search_keyword = 'ipad'
driver.find_element(By.ID,"twotabsearchtextbox").send_keys(search_keyword)
driver.find_element(By.CSS_SELECTOR, "input.nav-input[value='Go']").click()

first_product = driver.find_elements(By.CSS_SELECTOR, "a.a-link-normal.s-no-outline")[0]
first_product.click()

# Click add to cart button
wait = WebDriverWait(driver, 5)
wait.until(expected_conditions.presence_of_element_located((By.ID, "add-to-cart-button"))).click()

# Close popup if it appears
if driver.find_elements(By.ID, 'a-popover-1') and driver.find_element(By.ID, 'a-popover-1').is_displayed():
    driver.find_element_by_css_selector('#a-popover-1 .a-button-close').click()

# Quit the WebDriver instance for the cleanup
driver.quit()

