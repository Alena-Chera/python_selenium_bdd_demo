from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

PRODUCT_IMAGE = (By.CSS_SELECTOR, "div.card-img")


@given('user opens Sale Teaching kids shop page')
def open_sale_teaching_kids_page(context):
    context.driver.get('https://shop.scholastic.com/teachers-ecommerce/teacher/shops/teaching-kits.html')


@then('hover over the product image, verify user can see that the {button_name} button appears')
def hover_over_product_image_verify_Quick_Look_button_appears(context, button_name):
    all_products = context.driver.find_elements(*PRODUCT_IMAGE)
    for x in range(len(all_products)):
        product = context.driver.find_elements(*PRODUCT_IMAGE)[x]
        action = ActionChains(context.driver)
        action.move_to_element(product).perform()