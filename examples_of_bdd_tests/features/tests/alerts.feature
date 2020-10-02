Feature: JavaScript alert,confirmation, and prompt

  Scenario: User can see an alert message, user can close an alert
    Given Open google page


    When simple alert is open
    Then capture simple alert message, close simple alert

    When a Confirm alert is open
    Then capture the Confirm alert message, close the Confirm alert

    When Prompt is open
    Then capture Prompt message, close Prompt



#  The following methods are useful to handle alerts in selenium:

#1.  This method is used when ‘Cancel’ button is clicked in the alert box.
#driver.switch_to().alert().dismiss()

#2.  This method is used to click on the ‘OK’ button of the alert.
#driver.switch_to().alert().accept()

#3.  This method is used to capture the alert message.
#driver.switch_to().alert().text

#4.  This method is used to send data to the alert box.
#driver.switch_to().alert().send_keys("Text")



