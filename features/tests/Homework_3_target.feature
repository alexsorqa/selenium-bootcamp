Feature: Homework 3 target.com

  Scenario: User verifying cart is empty
    Given Open Target page
    Then Click on cart icon
    And Verify cart is empty

  Scenario: User verifying sign in page is opened
  Given Open Target page
  When Click Signin button
  Then Verify Signin page open
