from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from behave import given, when, then


GOOGLE_LINKS = (By.CSS_SELECTOR, "div#hptl a")


@given('open {application} application')
def open_application(context, application):
    context.driver.get(f'https://www.{application}.com/')


@when('right click onl ink About, then click on {list_option} on the displayed list')
def do_right_click_on_link_click_on_list_option(context, list_option):
    link = context.driver.find_elements(*GOOGLE_LINKS)[0]

    # action chain object creation
    action = ActionChains(context.driver)

    action \
        .context_click(link) \
        .send_keys(Keys.ARROW_DOWN) \
        .send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER) \
        .perform()


@then('verify {page} page opened in new window')
def verify_page_opened_in_new_window(context, page):
    current_url = context.driver.current_url
    print(current_url)
    assert "about.google" in current_url



