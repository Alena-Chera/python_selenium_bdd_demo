# ActionChains -- moving the mouse to the middle of an element.
# This action helps us to deal with dropdown menu that appears when the user moves the mouse over an element or when the user clicks on an element.
#
# move_to_element(to_element)
# Parameters:
# to_element: The WebElement to move to.


Feature: Shop. Educator store. Sale Teaching kids page. QUICK L00K feature


  Scenario: User can quick look the product
    Given user opens Sale Teaching kids shop page
    Then hover over the product image, verify user can see that the QUICK LOOK button appears




