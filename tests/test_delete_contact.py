# -*- coding: utf-8 -*-
from models.contact import Contact
import random
import pytest

def test_delete_contact(app, orm, check_ui):
    with pytest.allure.step('Given a non-empty contact list'):
        if app.contact.count() == 0:
            app.contact.create(Contact(firstname="Test", lastname="Test", address="some address, 1", home_number="+375293003030",
                                   mobile_number="+375294004040"))
        old_contact_list = orm.get_contact_list()
    with pytest.allure.step('Given a random contact from the list'):
        contact = random.choice(old_contact_list)
    with pytest.allure.step('When I delete a new contact from the list'):
        app.contact.delete_some_contact_by_id(contact.id)
    with pytest.allure.step('Then the new contct list is equal to the old list without the deleted contact'):
        new_contact_list = orm.get_contact_list()
        old_contact_list.remove(contact)
        assert old_contact_list == new_contact_list
        if check_ui:
            assert sorted(new_contact_list, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)