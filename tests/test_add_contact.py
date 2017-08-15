# -*- coding: utf-8 -*-
from models.contact import Contact


def test_add_contact(app, orm, json_contacts, check_ui):
    contact = json_contacts
    old_contact_list = orm.get_contact_list()
    app.contact.create(contact)
    new_contact_list = orm.get_contact_list()
    old_contact_list.append(contact)
    assert sorted(old_contact_list, key=Contact.id_or_max) == sorted(new_contact_list, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contact_list, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
