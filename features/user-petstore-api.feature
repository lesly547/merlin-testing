Feature: Search petstore API
  Scenario: Create petstore user
    Given petstore service is deployed
    And create user object with file user.json
    When execute create user petstore service
    Then obtain status code 200
    And obtain id message


  Scenario: Obtain petstore user
    Given petstore service is deployed
    When execute get user petstore service by username
    Then obtain status code 200
    And obtain data user