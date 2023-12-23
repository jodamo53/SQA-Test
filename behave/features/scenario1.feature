# Created by Dario at 18/12/2023
Feature: Searching on Google and Clicking

  Scenario: User can search with “Google Search”
    Given Launch the Browser on the Google Home Page
    When I type the word "test automation"
    When I click on the Search Buttom, I go to the search page
    Then I confirm the first 3 result contain the word "automation"
