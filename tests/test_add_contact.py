# -*- coding: utf-8 -*-
from models.contact import Contact


def test_add_contact(app, db, json_contacts, check_ui):
    contact = json_contacts
    old_contact_list = db.get_contact_list()
    app.contact.create(contact)
    def clean(contact):
        return Contact(id=contact.id, firstname=contact.firstname.strip(), lastname=contact.lastname.strip())
    new_contact_list = map(clean, db.get_contact_list())
    old_contact_list.append(contact)
    assert sorted(old_contact_list, key=Contact.id_or_max) == sorted(new_contact_list, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contact_list, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)

