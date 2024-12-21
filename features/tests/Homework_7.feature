
Feature: Homework 7

  Scenario: Sign in Page verification
    Given Open Target page
    Then Click header sign in
    Then Click sign in menu
    And Verify sign in page open

  Scenario: Item added to the cart
    Given Open Target page
    When Search for Blogilates Gym Bag - Black
    Then Blogilates Gym Bag - Black result is displayed
    And Add to cart Blogilates Gym Bag - Black in results page
    Then Add to cart Blogilates Gym Bag - Black in add product menu
    Then Click view cart and checkout in product menu
    Then Verify Blogilates Gym Bag - Black on cart page

  Scenario: Create a new username for Target
    Given Open Target page
    Then Click header sign in
    Then Click sign in menu
    Then Input alexsorqa@gmail.com username on sign in page
    Then Input alexsorqa@gmail.com password on sign in page
    And Click sign in on sign in page
    Then Target main page opens
