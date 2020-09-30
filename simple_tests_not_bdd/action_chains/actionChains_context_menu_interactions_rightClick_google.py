
"""
 ActionChains -- right click (context menu interactions)

Scenario to Automate:
1. Launch the web browser and open the application
2. Find the required element (the link 'About') and do right click on the element
3. Click on an element 'Open Link in New Window' on the displayed list of right click options
4. Close the browser
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

# init driver:
driver = webdriver.Chrome()

# open the url:
driver.get('https://www.google.com/')

# wait 4 sec:
driver.implicitly_wait(10)

link = driver.find_elements(By.CSS_SELECTOR, "div#hptl a ")[0]

# action chain object creation
action = ActionChains(driver)

action\
    .context_click(link)\
    .send_keys(Keys.ARROW_DOWN)\
    .send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER)\
    .perform()

current_url = driver.current_url
print(current_url)
assert "about.google" in current_url

# close browser
driver.quit()







