from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

MONOGRAM_TITLE_LOCATOR = (By.CSS_SELECTOR, "#variation_color_name .selection")
MONOGRAMS_BUTTON_LOCATOR = (By.CSS_SELECTOR, "#variation_color_name ul[role='radiogroup'] li")
ADD_TO_CART_BUTTON_LOCATOR = (By.CSS_SELECTOR, '#add-to-cart-button')


@given('Open Amazon bag page')
def open_bag_page(context):
    context.driver.get('https://www.amazon.com/DALIX-Premium-Striped-Zippered-Monogrammed/dp/B07FYS7KF9/ref=sr_1_9'
                       '?crid=280XERBNVLE4K&dchild=1&keywords=bag%2Bbeach&qid=1581827095&sprefix=bag%2Bbea%2Caps'
                       '%2C138&sr=8-9&th=1')


@when('Get all bag monogrammed A-Z colors')
def get_all_bag_monograms(context):
    context.bag_colors = context.driver.find_elements(*MONOGRAMS_BUTTON_LOCATOR)


@then('Check that every monogram has description')
def monogram_has_description(context):
    color_title = context.driver.find_element(*MONOGRAM_TITLE_LOCATOR)
    for bag_color in context.bag_colors:
        bag_color.click()
        print(color_title.text)
        print(bag_color.get_attribute('title'))
        assert color_title.text in bag_color.get_attribute(
            'title'), f"Expected {color_title.text} in {bag_color.get_attribute('title')}"


@then('User can add bag with {need_color} monogram to cart')
def add_needed_bag_color_to_cart(context, need_color):
    for bag_color in context.bag_colors:
        if need_color in bag_color.get_attribute('title'):
            sleep(3)
            bag_color.click()
    add_to_cart_button = context.driver.find_element(*ADD_TO_CART_BUTTON_LOCATOR)

    add_to_cart_button.click()
