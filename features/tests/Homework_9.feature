Feature: Homework 9


  Scenario: Make a test case using a dropdown and search for a different topic on Target Help. Verify that Select works and opens the correct page.

    Given Open Target returns page
    When Select returns topic Holiday Help
    Then Verify returns Holiday Help page opened

  Scenario: User is unable to login in with wrong credentials
    Given Open Target page
    Then Click header sign in
    Then Click sign in menu
    Then Verify sign in page open
    Then Input helloworld1255@careerist.com username on sign in page
    And Input password 12345 password on sign in page
    Then Click sign in on sign in page
    Then The error message displays


