Feature: selecting elements from the dropdown menu


  Scenario: Using the language Selector component, users can select their preferred language on the wikipedia page.
    Given open wikipedia home page
    When user selects German as search language by visible text "Deutsch"
    And click the search button
    Then make sure the page has been opened and user can do Search in German "Suche"

