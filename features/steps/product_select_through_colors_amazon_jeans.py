from selenium.webdriver.common.by import By
from behave import given, when, then

COLOR_OPTIONS = (By.CSS_SELECTOR, "div#variation_color_name li")
SELECTED_COLOR = (By.CSS_SELECTOR, "#variation_color_name .selection")


@given('Open Amazon Jeans {productid} page')
def open_jeans_page(context, productid):
    context.driver.get(f'https://www.amazon.com/gp/product/{productid}/?th=1')


@then('User can select through colors')
def verify_colors(context):
    expected_colors = ['Black', 'Blue Overdyed', 'Indigo Wash', 'Light Wash', 'Medium Wash', 'Rinse', 'Dark Wash',
                       'Vintage Light Wash']
    color_options = context.driver.find_elements(*COLOR_OPTIONS)

    # 1. THIS IS FIRST WAY HOW TO USE FOR LOOP HERE:
    print("=====================================")
    for color in color_options:
        color.click()
        print(context.driver.find_element(*SELECTED_COLOR).text)
        assert context.driver.find_element(*SELECTED_COLOR).text == expected_colors[color_options.index(color)]

    # 2. THIS IS SECOND WAY HOW TO USE FOR LOOP HERE:
    print("=====================================")
    for x in range(len(color_options)):
        color_options[x].click()
        select_color_text = context.driver.find_element(*SELECTED_COLOR).text
        print("COLOR ELEMENT: ", select_color_text)
        assert select_color_text == expected_colors[x]
