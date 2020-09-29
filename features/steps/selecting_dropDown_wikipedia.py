from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

SELECT_SEARCH_LANGUAGE = (By.CSS_SELECTOR, "select#searchLanguage")
SEARCH_BUTTON = (By.CSS_SELECTOR, "button.pure-button.pure-button-primary-progressive")
TEXT_ON_PAGE = (By.ID, 'firstHeading')


@given('open wikipedia home page')
def open_wikipedia(context):
    context.driver.get('https://www.wikipedia.org/')


@when('user selects {language} as search language by visible text "{visible_text}"')
def selects_language_by_visible_text(context, language, visible_text):
    select = Select(context.driver.find_element(*SELECT_SEARCH_LANGUAGE))
    select.select_by_visible_text(f'{visible_text}')


@when('click the search button')
def click_search_button(context):
    search_button = context.driver.find_element(*SEARCH_BUTTON)
    search_button.click()


@then('make sure the page has been opened and user can do Search in German "{word_on_the_page}"')
def verify_correct_page_opened(context, word_on_the_page):
    text_on_the_page = context.driver.find_element(*TEXT_ON_PAGE).text
    print(f'Word "Search" on the wiki page in selected language - ' + text_on_the_page)

    assert word_on_the_page == text_on_the_page

