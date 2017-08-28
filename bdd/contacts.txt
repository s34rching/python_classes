Scenario Outline: Add new contact
    Given a contact list
    Given a contact with attributes <firstname>, <lastname>, <address>, <email>, <home_number>, <mobile_number>, <work_number>, <secondary_number>, <email2>, <email3>
    When I add a new contact to the list
    Then the new contact list is equal to the old list with the added contact

    Examples:
    | firstname | lastname | address | email | home_number | mobile_number | work_number | secondary_number | email2 | email3 |
    | firstname1 | lastname2 | address3 | email4 | home_number1 | mobile_number1 | work_number1 | secondary_number1 | email21 | email31 |
    | firstname1 | lastname1 | address1 | email6 | home_number4 | mobile_number5 | work_number2 | secondary_number2 | email22 | email32 |


Scenario Outline: Delete random contact
    Given a non-empty contact list
    Given a random contact from the list
    When I delete a new contact from the list
    Then the new contct list is equal to the old list without the deleted contact


Scenario Outline: Edit random contact
    Given a non-empty contact list
    Given a random contact from the list
    Given a contact with new <firstname>
    When I edit a random contact from the list
    Then the new contact list is equal to the old list
