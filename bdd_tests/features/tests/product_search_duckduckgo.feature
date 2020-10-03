
# These tests cover DuckDuckGo searches

Feature: DuckuckGo Web Browsing

  Scenario: Basic DuckuckGo Search
    Given the DuckuckGohome page is displayed
    When the user searches for "panda"
    Then result are shown for "panda"