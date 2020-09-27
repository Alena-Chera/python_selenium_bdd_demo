"""
Scholastic.com user wants to do some operation in newly opened child window,
close it after all operations and do some actions in parent window.

"""

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.scholastic.com/home")

# open up a new window in current session by clicking on the link in parent window
driver.find_element_by_css_selector("span.footer-link--privacy-policy__underline").click()

# 1. Get all window handles
handles = driver.window_handles
size = len(handles)

# 2. Get parent window handle and store in a temp variable say ‘parent_handle’
parent_handle = driver.current_window_handle

# 3. If handle is not parent window handle, Switch to the child or new window using driver.switch_to.window(handles)
for x in range(size):
    if handles[x] != parent_handle:
        driver.switch_to.window(handles[x])
        # 4. Perform all required operations and close the child or new window
        print(driver.title)
        assert "Privacy Policy" in driver.title
        text_on_privacy_policy_page = driver.find_element_by_css_selector("div#cc-wrap h1.title").text
        print(text_on_privacy_policy_page)
        assert "SCHOLASTIC PRIVACY POLICY" in text_on_privacy_policy_page
        driver.close()
        break

# 5. Shift the control back to parent window
driver.switch_to.window(parent_handle)

# 6. Perform required operations / click SHOP NOW link, verify correct page open
driver.find_element_by_css_selector("div.cmp-compoundheader__actionLink.cmp-labelTextLink a.cmp-title__link").click()
assert "shop.scholastic.com" in driver.current_url

driver.quit()
