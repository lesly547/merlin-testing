Feature: Search pets petstore API
  Scenario: Search pets sold petstore API
    Given petstore service is deployed
    When execute pet find by status sold
    Then obtain status code 200
    And transform in tupla id and petname
    And obtain number similar pets name