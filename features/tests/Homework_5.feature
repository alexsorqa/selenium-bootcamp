Feature: Homework 5

  Scenario: Item colors verification
    Given Open Target page
    When Search for DualSense Wireless Controller for PlayStation 5
    Then DualSense Wireless Controller for PlayStation 5 result is displayed
    Then Click on DualSense Wireless Controller for PlayStation 5 in results page
    And DualSense Wireless Controller for PlayStation 5 colors are visible

  Scenario: Item color selection
    Given Open shoes page
    Then Select different colors