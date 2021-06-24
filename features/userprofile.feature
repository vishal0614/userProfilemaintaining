Feature: Maintaining User Profile

  Scenario: User login
    Given I launch browser
    When I open user login page
    And Enter username,password and click login button
    Then Welcome page displayed with user profile Which shows Username,Name,Company_name and Role

