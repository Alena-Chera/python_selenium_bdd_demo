
# These tests cover DuckDuckGo searches

Feature: Search using DuckDuckGo

  Scenario: Basic DuckuckGo Search
    Given the DuckuckGohome page is displayed
    When the user searches for "gift"
    Then search results for "gift" should appear

