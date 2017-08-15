# -*- coding: utf-8 -*-
from models.contact import Contact
import random

def test_delete_contact(app, orm, check_ui):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Test", middlename="Test", lastname="Test", nickname="test_contact1", address="some address, 1", home_number="+375293003030",
                               mobile_number="+375294004040"))
    old_contact_list = orm.get_contact_list()
    contact = random.choice(old_contact_list)
    app.contact.delete_some_contact_by_id(contact.id)
    new_contact_list = orm.get_contact_list()
    old_contact_list.remove(contact)
    assert old_contact_list == new_contact_list
    if check_ui:
        assert sorted(new_contact_list, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)