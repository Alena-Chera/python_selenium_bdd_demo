Feature: Test scenarios for searching product color

  Scenario: User can select through colors
    Given Open Amazon bag page
    When Get all bag monogrammed A-Z colors
    Then Check that every monogram has description
    Then User can add bag with M monogram to cart