from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By

# init driver
driver = webdriver.Chrome()

# open the url
driver.get('https://www.wikipedia.org/')

# maximize window
driver.maximize_window()

# select German as search language by visible text 'Deutsch'
select = Select(driver.find_element(By.CSS_SELECTOR, "select#searchLanguage"))
select.select_by_visible_text('Deutsch')

# click the search button
search_button = driver.find_element(By.CSS_SELECTOR, "button.pure-button.pure-button-primary-progressive")
search_button.click()

# wait 2 sec
driver.implicitly_wait(2)

text_on_the_page = driver.find_element(By.ID, 'firstHeading').text
print(text_on_the_page)

# make sure the page has been opened and contains information in German
assert 'Suche' == text_on_the_page

driver.quit()

