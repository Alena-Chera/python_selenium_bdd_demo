from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver

# init driver:
driver = webdriver.Chrome()

# maximize the browser window
driver.maximize_window()

# open the url:
driver.get('https://www.google.com/')

# refresh the browser
driver.refresh()

# creat an alert
driver.execute_script('window.alert(\'This is an alert. Please click OK button.\')')

try:
    # wait for the alert to be displayed and store it in a variable
    driver.wait = WebDriverWait(driver, 15)
    alert = driver.wait.until(EC.alert_is_present())

    # capture an alert message (store the alert text in a variable)
    alert_text = alert.text
    print(f'An alert shows following message: ' + alert_text)

    # press the OK button to accept the alert
    alert.accept()
    print("An alert accepted")

except TimeoutException:
    print("No alert")

# close browser
driver.quit()
