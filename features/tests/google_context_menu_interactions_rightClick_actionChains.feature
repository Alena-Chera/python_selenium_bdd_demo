# ActionChains -- perform a context-click (right click) on an element.
#
# context_click(on_element=None)
# Parameters:
# on_element: The element to context-click or right click on. If no element passed, right clicks on current mouse position.


# ActionChains -- sends keys to current focused element.
#
# send_keys(keys_to_send)
# Parameters:
# keys_to_send: The keys to send.       (Keys.ARROW_DOWN, Keys.ENTER)


Feature: context menu interactions


  Scenario: user can open link in new window by using context menu
    Given open google application
    When right click onl ink About, then click on Open Link in New Window on the displayed list
    Then verify about.google page opened in new window







