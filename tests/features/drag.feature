Feature: Test draggable elements
    As a developer
    I want to be able to test a given draggable element

    Background:
        Given I open the site "/"
        And   I have a screen that is 1024 by 768 pixels
        When  I scroll to element "#draggable"

    Scenario: Drag to dropzone
        When  I drag element "#draggable" to element "#droppable"
        Then  I expect that element "#droppable" contains the text "Dropped!"
