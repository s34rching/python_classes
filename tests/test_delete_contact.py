# -*- coding: utf-8 -*-
from models.contact import Contact

def test_delete_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Test", middlename="Test", lastname="Test", nickname="test_contact1", address="some address, 1", home_number="+375293003030",
                               mobile_number="+375294004040"))
    old_contact_list = app.contact.get_contact_list()
    app.contact.delete_contact()
    new_contact_list = app.contact.get_contact_list()
    assert len(old_contact_list) - 1 == len(new_contact_list)