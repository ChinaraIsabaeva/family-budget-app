Feature: Add expense
    In order to use mybudget app
    I want to be able to add new expense

    Scenario: New expense
        Given I navigate to url "/"
        When I fill in the "expense"
        And I click "Add expense"
        Then I new expense add to database