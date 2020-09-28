
"""
 ActionChains -- hover over element(move_to_element)

Scenario to Automate:
1. Launch the web browser and open the application
2. Hover over the product image
3. Verify user can see that the Quick Look button appears
4. Close the browser

"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

# init driver:
driver = webdriver.Chrome()

# open the url:

driver.get('https://shop.scholastic.com/teachers-ecommerce/teacher/shops/teaching-kits.html')
# wait 4 sec:
driver.implicitly_wait(10)

all_products = driver.find_elements(By.CSS_SELECTOR, "div.card-img")
for x in range(len(all_products)):
    product = driver.find_elements(By.CSS_SELECTOR, "div.card-img")[x]
    action = ActionChains(driver)
    action.move_to_element(product).perform()
    assert driver.find_elements(By.CSS_SELECTOR, "a.quicklookButton")[x]
    assert driver.find_elements(By.CSS_SELECTOR, "a.quicklookButton")[x].text == "QUICK LOOK"

# close browser
driver.quit()