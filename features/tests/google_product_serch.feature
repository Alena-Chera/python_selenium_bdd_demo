Feature: Test Scenarios for Search functionality

  Scenario: User can search for a product
    Given Open Google page
    When input Dress into search field
    And click on search icon
    Then product results for Dress are shown
    And first result contains Dress