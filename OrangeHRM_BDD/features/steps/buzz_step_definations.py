@buzzmodule
Feature: This module contains buzz feature scenarios

    Background: Precondition steps for buzz module
        Given Chrome browser is launched
        When User navigates to OrangeHRM Login Page
        And User enter valid username, password and clicks on login button
        And User clicks on Buzz item in left menu
    
@PostText
    Scenario: Validate admin should be able post in Buzz Newsfeed
        When Admin type a message in Post input field
        And Clicks on Post button
        Then Post should appear in most recent post section