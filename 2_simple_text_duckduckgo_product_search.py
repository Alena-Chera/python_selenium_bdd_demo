"""
Web test cases for DuckDuckGo search functionality
DuckDuckGo is a search engine that doesn’t track user data.
Users can enter search phrases and get links to matching websites.

Test procedure:
1.	Navigate to the DuckDuckGo home page
2.	Enter the search phrase
3.	Verify that:
  a. Results appear on the results page
  b. The search phrase appears in the search bar
  c. At least one search result contains the search phrase
It’s basic, but it covers typical searching behavior end-to-end.

"""
from selenium import webdriver

# Initialize ChromeDriver
driver = webdriver.Chrome(executable_path='drivers/chromedriver')

# Wait implicitly for elements to be ready before attempting interactions
driver.implicitly_wait(10)

# Set up some test case data
URL = 'https://www.duckduckgo.com'
PHRASE = 'panda'

# Navigate to the DuckDuckGo home page
# open the url
driver.get(URL)

# Find the search input element
# In the DOM, it has an 'id' attribute of 'search_form_input_homepage'
search_input = driver.find_element_by_id('search_form_input_homepage')

# Send a search phrase to the input and hit the RETURN key
search_input.send_keys(PHRASE)

# Find the search button element and then click
# In the DOM, it has an 'id' attribute of 'search_form_input_homepage'
search_button = driver.find_element_by_id("search_button_homepage")
search_button.click()

# Verify that results appear on the results page
link_divs = driver.find_elements_by_css_selector('#links > div')
assert len(link_divs) > 0

# Verify that at least one search result contains the search phrase
xpath = f"//div[@id='links']//*[contains(text(), '{PHRASE}')]"
phrase_results = driver.find_elements_by_xpath(xpath)
assert len(phrase_results) > 0

# Verify that the search phrase is the same
search_input = driver.find_element_by_id('search_form_input')
assert search_input.get_attribute('value') == PHRASE

# For cleanup, quit the driver
driver.quit()
