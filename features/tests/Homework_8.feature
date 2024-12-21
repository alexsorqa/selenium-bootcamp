Feature: Homework 8

  Scenario: User can open and close Terms and Conditions from sign in page
    Given Open Target page
    Then Click header sign in
    Then Click sign in menu
    And Verify sign in page open
    Given Store original window
    Then Click on terms and conditions link
    When Switch to new window
    Then Verify terms and conditions page open
    And Close current window
    And Switch back to original window