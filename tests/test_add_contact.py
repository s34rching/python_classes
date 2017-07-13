# -*- coding: utf-8 -*-
from models.contact import Contact


def test_add_contact(app):
    app.contact.create(Contact(firstname="Test", middlename="Test", lastname="Test", nickname="test_contact1", address="some address, 1", home_number="+375293003030",
                               mobile_number="+375294004040"))