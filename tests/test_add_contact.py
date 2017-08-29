# -*- coding: utf-8 -*-
from models.contact import Contact
import pytest


def test_add_contact(app, orm, json_contacts, check_ui):
    with pytest.allure.step('Given a contact with attributes <firstname>, <lastname>, <address>, <email>, <home_number>, <mobile_number>, <work_number>, <secondary_number>, <email2>, <email3>'):
        contact = json_contacts
    with pytest.allure.step('Given a contact list'):
        old_contact_list = orm.get_contact_list()
    with pytest.allure.step('When I add a new contact to the list'):
        app.contact.create(contact)
    with pytest.allure.step('Then the new contact list is equal to the old list with the added contact'):
        new_contact_list = orm.get_contact_list()
        old_contact_list.append(contact)
        assert sorted(old_contact_list, key=Contact.id_or_max) == sorted(new_contact_list, key=Contact.id_or_max)
        if check_ui:
            assert sorted(new_contact_list, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
