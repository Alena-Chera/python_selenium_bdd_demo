# EXAMPLES OF SCENARIOS

    Given Open Amazon main page
    Given Open Amazon page

    # Shopping Cart is empty
    # Lana
  Scenario: 'Your Shopping Cart is empty' shown if no product added
    Given Open Amazon page
    When Click on cart icon
    Then Verify 'Your Shopping Cart is empty.' text present

    # Click Orders link - Verify Sign In page is opened
    # Lana
  Scenario: Logged out user sees Sign in page when clicking Orders
    Given Open Amazon page
    When Click Amazon Orders link
    Then Verify Sign In page is opened

    # Search
    # Lana
  Feature: Lego search
  Scenario: Find header on goods page
    Given Open Amazon main page
    When Search input fill Lego
    And Click search button
    Then Assert Lego header on page

      # Search
    # Lana
Feature: Test Scenarios for Amazon Search functionality
  Scenario: User can search for the product
    Given open Amazon page
    When search for dress
    Then product results for "dress" are shown

    # Count the elements of the ListElements
    # Lana
Feature: Tests for hamburger menu functionality
  Scenario: Amazon Music has 6 menu items
    Given Open Amazon main page
    When Click on hamburger menu
    And Click on Amazon Music menu item
    Then 6 menu items are present

    # Interacting with elements to avoid StaleElementReferenceException
    # Lana
Feature: Test for bestseller functionality
  Scenario: Bestseller link can be open
    Given Open Amazon Bestsellers
    Then User can click through top links and verify correct page opens

    # Use for loop to Select multiple items
# 1 Lana
Feature: Test for dress selection
  Scenario: User can select dress colors
    Given Open Amazon Dress B07K16R9V3 page
    Then Verify user can select through colors
# 2 Ilya
 Feature: Dress color
  Scenario: Check every dress color name
    Given Open Amazon dress page
    When Get all dress colors
    Then Check every color has description

    #  Search result, print text from n-element from list of elements,
    #  if-elif-else loop
    # Anna
Feature: Search result
  Scenario: Check the number of search result
    Given Open Amazon main page
    When Search input fill Lego
    And Click search button
    Then The number of items is equal to 60


    # Verify Each item has Regular field and Product name
    # Anna-Lana
 Feature: Search Result WholeFoods deals
  Scenario: Each product has "Regular" price field and product name
    Given Open  WholeFoods Amazon page
    Then Each item has Regular field and Product name

    # Use EXPECTED CONDITION (EC) for waiting in code.
    # Anna
Feature: Amazon main page popup
  Scenario: Sign in popup appears and then disappears
    Given Open Amazon main page
    Then VerifySign In popup is present and clickable
    When Sign in popup disappears
    Then Verify Sign in popup is not clickable

    # Window handling
    # Anna
Feature: Window handling
  Scenario: Company's website is open in a new tab
    Given Open a Anchors fish & chips Yelp page
    When Click a website link
    And Switch to a new window
    Then The Anchors fish & chips website is open
    And A user can close the new window and go to the original one