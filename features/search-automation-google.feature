Feature: Search automation key
  Scenario: Selecting a search result by keyword
    Given user access to Google website
    And cookies accept
    And searching automatizacion
    When selecting wikipedia result
    Then valid the year of the first automatic process