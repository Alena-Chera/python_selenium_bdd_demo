from selenium.webdriver.common.by import By
from behave import given, when, then

URL = 'https://www.duckduckgo.com'
SEARCH_FIELD = (By.ID, "search_form_input_homepage")
SEARCH_BUTTON = (By.ID, "search_button_homepage")


@given('the DuckuckGohome page is displayed')
def open_duckuckgohome_page(context):
    context.driver.get(URL)


@when('the user searches for "{search_phrase}"')
def search_for_world(context, search_phrase):
    search_input = context.driver.find_element(*SEARCH_FIELD)
    search_input.send_keys(search_phrase)
    search_button = context.driver.find_element(*SEARCH_BUTTON)
    search_button.click()


@then('search results for "{search_phrase}" should appear')
def verify_result_appears_on_the_results_page(context, search_phrase):
    link_divs = context.driver.find_elements_by_css_selector('#links > div')
    assert len(link_divs) > 0

# Verify that results appear on the results page
    link_divs = context.driver.find_elements_by_css_selector('#links > div')
    assert len(link_divs) > 0

# Verify that at least one search result contains the search phrase
    xpath = f"//div[@id='links']//*[contains(text(), '{search_phrase}')]"
    phrase_results = context.driver.find_elements_by_xpath(xpath)
    assert len(phrase_results) > 0

# Verify that the search phrase is the same
    search_input = context.driver.find_element_by_id('search_form_input')
    assert search_input.get_attribute('value') == search_phrase