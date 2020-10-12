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


Feature: Search using DuckDuckGo
Scenario: Basic DuckuckGo Search

"""
from selenium import webdriver


# Initialize the ChromeDriver instance
driver = webdriver.Chrome()

# Maximize window
# We try to stay our test more stable - we open the window for full size
# to make sure that user actually works with a full screen
driver.maximize_window()

# Make its calls wait up to 10 seconds for elements to appear
# (Wait implicitly for elements to be ready before attempting interactions)
driver.implicitly_wait(10)

"""
1
Given the DuckuckGohome page is displayed
"""
# Set up some test case data
URL = 'https://www.duckduckgo.com'
PHRASE = 'gift'

# Navigate to the DuckDuckGo home page
# open the url
driver.get(URL)

"""
2
When the user searches for "gift"
"""
# Find the search input element
# In the DOM, it has an 'id' attribute of 'search_form_input_homepage'
search_input = driver.find_element_by_id('search_form_input_homepage')

# Send a search phrase to the input and hit the RETURN key
search_input.send_keys(PHRASE)

# Find the search button element and then click
# In the DOM, it has an 'id' attribute of 'search_form_input_homepage'
search_button = driver.find_element_by_id("search_button_homepage")
search_button.click()

"""
3
Then search results for "gift" should appear
"""
# Verify that results appear on the results page
link_divs = driver.find_elements_by_css_selector('#links > div')
assert len(link_divs) > 0

"""
4
The search phrase appears in the search bar
"""
# Verify that the search phrase is the same
search_input = driver.find_element_by_css_selector('input#search_form_input')
assert search_input.get_attribute('value') == PHRASE


"""
5
And at least one search result contains the search phrase
"""
# Verify that at least one search result contains the search phrase
xpath = f"//div[@id='links']//*[contains(text(), '{PHRASE}')]"
phrase_results = driver.find_elements_by_xpath(xpath)
assert len(phrase_results) > 0


# Quit the WebDriver instance for the cleanup
# This closes the browser session, not just the window
driver.quit()
















