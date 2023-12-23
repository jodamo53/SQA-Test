# Created by Dario at 19/12/2023
Feature: Searching on Google and Clicking

  Scenario: User can search with “Google Search”
    Given I Search by keyword
    When I click on the first result link
    Then I go to the page, and the page title contains the word “automation”
