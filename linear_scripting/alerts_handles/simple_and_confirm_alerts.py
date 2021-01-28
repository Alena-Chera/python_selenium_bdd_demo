from selenium import webdriver

driver = webdriver.Chrome()

# maximize the browser window
driver.maximize_window()

# get method to launch the URL
driver.get("http://demo.guru99.com/test/delete_customer.php")

# refresh the browser
driver.refresh()

# click on submit button
driver.find_element_by_name("submit").click()

# the alert object creation and switching focus to the alert
a = driver.switch_to.alert

# capture the alert message
print(f'An alert shows following message: ' + a.text)

# accept the alert
a.accept()
# or dismiss the alert using
# a.dismiss()

# the alert object creation and switching focus to the alert
a = driver.switch_to.alert

# capture the alert message
print(f'An alert shows following message: ' + a.text)

# accept the alert
a.accept()

# close browser
driver.quit()
