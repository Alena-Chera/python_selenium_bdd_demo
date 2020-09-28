# ActionChains right click (context menu interactions)

Feature: context menu interactions


  Scenario: user can open link in new window by using context menu
    Given open google application
    When right click onl ink About, then click on Open Link in New Window on the displayed list
    Then verify about.google page opened in new window







