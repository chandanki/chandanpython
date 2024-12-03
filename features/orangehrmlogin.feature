Feature: Orange HRM login

  Scenario: Login to HRM with valid parameter
    Given I launch Chrome browser
    When I open Orange HRM Homepage
    And Enter username "student" and "password123"
    And Click on login button
    Then User must login to the dashboard

  Scenario Outline: Login to practice automation
    Given I launch Chrome browser
    When I open Orange HRM Homepage
    And Enter username "<username>" and password "<password>"
    And Click on login button
    Then User must log in

    Examples:
     | username | password |
     | student | passwrd123 |
     | student | password123 |
     | were | pass |

