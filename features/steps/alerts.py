from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from behave import given, when, then


@when('simple alert is open')
def create_alert(context):

    # create alert
    context.driver.execute_script('window.alert(\'Please click OK button.\')')


@then('capture simple alert message, close simple alert')
def get_alert_text_and_close_alert(context):

    try:
        # wait for the alert to be displayed and store it in a variable
        alert = context.driver.wait.until(EC.alert_is_present())

        # capture an alert message (store the alert text in a variable)
        alert_text = alert.text
        print(f'The simple alert shows following message: ' + alert_text)

        # press the OK button to accept the alert
        alert.accept()
        print("Alert accepted")
    except TimeoutException:
        print("No alert")


@when('a Confirm alert is open')
def create_confirm_alert(context):

    # create confirm alert
    context.driver.execute_script('window.confirm(\'Do you confirm action?\')')


@then('capture the Confirm alert message, close the Confirm alert')
def get_confirm_alert_text_and_close_confirm_alert(context):

    try:
        # wait for the Confirm alert to be displayed
        context.driver.wait.until(EC.alert_is_present())

        # store the Confirm alert in a variable for reuse
        alert = context.driver.switch_to.alert

        # store the confirm alert text in a variable
        confirm_alert_text = alert.text

        print(f'The Confirm alert shows following message: ' + confirm_alert_text)

        # press the cancel button to dismiss the Confirm alert
        alert.dismiss()
        print("Confirm alert dismissed")
    except TimeoutException:
        print("No Confirm alert")


@when('Prompt is open')
def create_prompt_verify_prompt_is_present(context):

    # create prompt alert
    context.driver.execute_script('window.prompt(\'Please enter your name and click OK button.\')')


@then('capture Prompt message, close Prompt')
def type_message_and_get_prompt_text_and_close_prompt(context):

    try:
        # wait for Prompt to be displayed
        context.driver.wait.until(EC.alert_is_present())

        # store Prompt in a variable for reuse
        alert = Alert(context.driver)

        # type a message
        alert.send_keys("Anna")

        # store the Prompt text in a variable
        prompt_text = alert.text

        print(f'Prompt shows following message: ' + prompt_text)

        # press the OK button to accept Prompt
        alert.accept()
        print("Prompt accepted")
    except TimeoutException:
        print("No Prompt")




