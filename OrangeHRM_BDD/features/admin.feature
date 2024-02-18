#Author: your.email@your.domain.com
#Keywords Summary :
#Feature: List of scenarios.
#Scenario: Business rule through list of steps with arguments.
#Given: Some precondition step
#When: Some key actions
#Then: To observe outcomes or validation
#And,But: To enumerate more Given,When,Then steps
#Scenario Outline: List of steps for data-driven as an Examples and <placeholder>
#Examples: Container for s table
#Background: List of steps run before each of the scenarios
#""" (Doc Strings)
#| (Data Tables)
#@ (Tags/Labels):To group Scenarios
#<> (placeholder)
#""
## (Comments)
#Sample Feature Definition Template


@tag
Feature: Title of your feature
  I want to use this template for my feature file

  @nav1
   Given Chrome browser is launched
   When User navigates to OrangeHRM Login Page
  Scenario: Validate navigation to OrangeHRM
    Then User should see page title as OrangeHRM
    
  @nav2
   Given Chrome browser is launched
   When User navigates to OrangeHRM Login Pagebea
  Scenario: Validate login to OrangeHRM site
  And User enter valid username, password and clicks on login button
  Then User should be on dashboard page

