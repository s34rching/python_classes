# -*- coding: utf-8 -*-
from models.contact import Contact


def test_add_contact(app):
    old_contact_list = app.contact.get_contact_list()
    contact = Contact(firstname='Alex', middlename='Jr', lastname='Smith', nickname='smth', address='some_street, 15', home_number='+149152959521', mobile_number='1-4915-295-95-21',
                      work_number='1 4915 295 95 21', secondary_number='1(4915)2959521', email='asd111@email.com', id=None)
    app.contact.create(contact)
    assert len(old_contact_list) + 1 == app.contact.count()
    new_contact_list = app.contact.get_contact_list()
    old_contact_list.append(contact)
    assert sorted(old_contact_list, key=Contact.id_or_max) == sorted(new_contact_list, key=Contact.id_or_max)
