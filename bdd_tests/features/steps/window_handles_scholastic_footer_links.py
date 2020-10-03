from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

PRIVACY_POLICE_LINK = (By.CSS_SELECTOR, "span.footer-link--privacy-policy__underline")
PRIVACY_POLICE_TEXT = (By.CSS_SELECTOR, "div#cc-wrap h1.title")

SOCIAL_NETWORK_ICONS = (By.CSS_SELECTOR, "div.cmp-fatFooter__socialLinksInner a")

SHOP_NOW_LINK = (By.CSS_SELECTOR, "div.cmp-compoundheader__actionLink.cmp-labelTextLink a.cmp-title__link")


@given('open Scholastic home page')
def open_google(context):
    context.driver.get('https://www.scholastic.com/home')


@then('click on {privacy_policy_link} link, verify {privacy_text_on_page} new window open, get back to home page')
def click_privacy_policy_link_verify_privacy_policy_page_open_get_back(context, privacy_policy_link, privacy_text_on_page):

    # 1. Open up a new window in current session
    context.driver.find_element(*PRIVACY_POLICE_LINK).click()

    # 2. Get all window handles
    handles = context.driver.window_handles
    size = len(handles)

    # 3. Get parent window handle and store in a temp variable say ‘parent_handle’
    parent_handle = context.driver.current_window_handle

    # 4. If handle is not parent window handle, Switch to the child or new window using driver.switch_to.window(handles)
    for x in range(size):
        if handles[x] != parent_handle:
            context.driver.switch_to.window(handles[x])
            # 5. Perform all required operations and close the child or new window
            print(context.driver.title)
            assert privacy_policy_link in context.driver.title
            text_on_privacy_policy_page = context.driver.find_element(*PRIVACY_POLICE_TEXT).text
            print(text_on_privacy_policy_page)
            assert privacy_text_on_page in text_on_privacy_policy_page
            context.driver.close()
            break

    # 6. Shift the control back to parent window
    context.driver.switch_to.window(parent_handle)


# 7. Perform required operations / click SHOP NOW link, verify correct page open
@then('be sure user can click on SHOP NOW link')
def verify_user_can_click_link_on_home_page(context):
    context.driver.find_element(*SHOP_NOW_LINK).click()
    assert "shop.scholastic.com" in context.driver.current_url


@then('click on Twitter Icon and verify {twitter} {scholasticinc} page was opened')
def click_twitter_icon_and_verify_new_twitter_window_opens(context, twitter, scholasticinc):

    original_windows = context.driver.window_handles
    original_window = context.driver.current_window_handle
    context.driver.find_elements(*SOCIAL_NETWORK_ICONS)[2].click()
    context.driver.wait.until(EC.new_window_is_opened)
    current_windows = context.driver.window_handles
    context.driver.switch_to_window(current_windows[1])
    current_url = context.driver.current_url
    print(f'Current url is ' + current_url)
    assert twitter in current_url
    assert scholasticinc in current_url
    context.driver.close()
    context.driver.switch_to_window(original_window)