# -*- coding: utf-8 -*-
from models.contact import Contact


def test_add_contact(app, db, json_contacts):
    contact = json_contacts
    old_contact_list = db.get_contact_list()
    app.contact.create(contact)
    new_contact_list = db.get_contact_list()
    old_contact_list.append(contact)
    assert sorted(old_contact_list, key=Contact.id_or_max) == sorted(new_contact_list, key=Contact.id_or_max)
