from selenium import webdriver
from selenium.webdriver.common.by import By

# init driver
driver = webdriver.Chrome()

# open the url
driver.get('https://www.google.com/')

search = driver.find_element(By.NAME, 'q')
search.clear()
search.send_keys('jeans')

# wait 3 sec
driver.implicitly_wait(4)

# click search
driver.find_element(By.NAME, 'btnK').click()

# verify
assert 'jeans' in driver.find_element(By.XPATH, "//div[contains(@class,'commercial-unit-desktop-top')]").text
assert 'jeans' in driver.find_element(By.XPATH, "//div[@class='g']").text

# closes the browser session, not just the window
driver.quit()
