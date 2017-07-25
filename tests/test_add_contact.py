# -*- coding: utf-8 -*-
from models.contact import Contact


def test_add_contact(app):
    old_contact_list = app.contact.get_contact_list()
    contact = Contact(firstname="Test", middlename="", lastname="AVS", nickname="", address="", home_number="", mobile_number="")
    app.contact.create(contact)
    assert len(old_contact_list) + 1 == app.contact.count()
    new_contact_list = app.contact.get_contact_list()
    old_contact_list.append(contact)
    assert sorted(old_contact_list, key=Contact.id_or_max) == sorted(new_contact_list, key=Contact.id_or_max)
