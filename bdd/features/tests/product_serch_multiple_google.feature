Feature: Test Scenarios for Google multiple search functionality


Scenario Outline: User can search for different products
  Examples:
  |search_word       |expected_search_result |
  |Towel             |Towel                  |
  |Jeans             |Jeans                  |
  |Dress             |Dress                  |
  |Gifts             |Gifts                  |

  Given Open Google page
  When input <search_word> into search field
  And click on search icon
  Then product results for <expected_search_result> are shown
  And first result contains <expected_search_result>