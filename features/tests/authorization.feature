Feature: Implement UI auto-tests to check basic authorization flows

  Scenario: Standard user passes authorization with valid credentials
    Given User is on the page with Login form
    When User fill in the login form with user name "standard_user" and password "secret_sauce"
    And Click Login button
    Then The user should be navigated to Products page

  Scenario: Standard user fails authorization with wrong credentials (wrong password)
    Given User is on the page with Login form
    When User fill in the login form with user name "standard_user" and password "secret_sauce1221"
    And Click Login button
    Then The error message "Epic sadface: Username and password do not match any user in this service" is displayed


  Scenario: Locked out user fails authorization with valid credentials
    Given User is on the page with Login form
    When User fill in the login form with user name "locked_out_user" and password "secret_sauce"
    And Click Login button
    Then The error message "Epic sadface: Sorry, this user has been locked out." is displayed
