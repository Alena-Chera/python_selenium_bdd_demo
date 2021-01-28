"""
Web test cases for Amazon 'add to cart' functionality
Users can search for product, then open product page of this product in new window/tub

Test procedure:
1. Navigate to the Amazon home page
2. Enter the search product
3. Select first product from results page, open product page in new window
4. When product page will open make sure product name is the same as on the results page

Feature: Product page
Scenario: Open amazon product page in new window

"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://www.amazon.com/")

search_keyword = 'ipad'

wait = WebDriverWait(driver, 5)

driver.find_element_by_id("twotabsearchtextbox").send_keys(search_keyword)
driver.find_element_by_name("site-search").submit()

first_product_title_on_result_page = driver.find_elements(By.CSS_SELECTOR, "span.a-size-medium.a-color-base.a-text-normal")[0]
first_product_title_on_result_page_text = first_product_title_on_result_page.text

first_product_image = driver.find_elements(By.CSS_SELECTOR, "a.a-link-normal.s-no-outline")[0]

# 1. Click COMMAND and ENTER key on keyboard to open product page in new window/tub
first_product_image.send_keys(Keys.COMMAND + Keys.ENTER)

# 2. Wait until this new window will be open
wait.until(expected_conditions.number_of_windows_to_be(2))
# 3. Get all window handles
handles = driver.window_handles            # list of window handles

# 4. Get parent window handle and store in a temp variable say ‘parent_handle’
parent_handle = driver.current_window_handle

# 5. Switch to the child or new window using driver.switch_to.window(handles)
driver.switch_to.window(handles[1])

# # 5. In case if we need to open more than one window, j window
# for j in range(1, len(handles)):
#     driver.switch_to.window(handles[j])

# wait until product title on product page will be presence
wait.until(expected_conditions.presence_of_element_located((By.ID, "productTitle")))

# make sure product name is the same as on the results page
product_title_on_product_page = driver.find_element(By.ID, "productTitle").text
assert first_product_title_on_result_page_text in product_title_on_product_page

# print product name on results page and print product name on product page
print(first_product_title_on_result_page_text)
print(product_title_on_product_page)

driver.quit()