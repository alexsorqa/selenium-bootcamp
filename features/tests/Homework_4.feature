Feature: Homework 4.1-4

  Scenario: User search for product
    Given Open Target page
    When Search for meme cat
    Then meme cat result is displayed

  Scenario: 10 Benefit cells are displayed
    Given Open Target Circle page
    Then 14 benefit cells are displayed

  Scenario: Item added to the cart
    Given Open Target page
    When Search for Blogilates Gym Bag - Black
    Then Blogilates Gym Bag - Black result is displayed
    And Add to cart Blogilates Gym Bag - Black in results page
    Then Verify Blogilates Gym Bag - Black on cart page

  Scenario: Target help page UI
    Given Open Target help page
    Then Verify UI elements present





