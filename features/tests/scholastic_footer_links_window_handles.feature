# Handling multiple windows.


Feature: Home Page footer links. PRIVACY POLICY link, social network link(Tweeter)
  Background:
    Given open Scholastic home page

# Scholastic.com user wants to do some operation in newly opened child window,
# close it after all operations and do some actions in parent window.
  Scenario: User can click on PRIVACY POLICY link and is taken to correct page, user is able to get back and do some activities on home page
    Then click on Privacy Policy link, verify SCHOLASTIC PRIVACY POLICY new window open, get back to home page
    And be sure user can click on SHOP NOW link


  Scenario: Clicking on a social network link a network page opens
    Then click on Twitter Icon and verify twitter scholastic page was opened