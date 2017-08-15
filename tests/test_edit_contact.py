# -*- coding: utf-8 -*-
from models.contact import Contact
from random import randrange


def test_edit_contact_firstname(app, orm, check_ui):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Test", middlename="Test", lastname="Test", nickname="test_contact1", address="some address, 1", home_number="+375293003030",
                               mobile_number="+375294004040"))
    old_contact_list = orm.get_contact_list()
    contact = Contact(firstname='F_ModifiedName')
    index = randrange(len(old_contact_list))
    random_contact = old_contact_list[index]
    contact.id = random_contact.id
    print(random_contact.id)
    app.contact.edit_some_contact_by_id(contact, random_contact.id)
    new_contact_list = orm.get_contact_list()
    old_contact_list[index] = contact
    assert sorted(old_contact_list, key=Contact.id_or_max) == sorted(new_contact_list, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contact_list, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)


# def test_some_test(app, db):
#    old_contact_list = db.get_contact_list()
#    index = randrange(len(old_contact_list))
#    random_contact = old_contact_list[index]
#    app.contact.test_f(random_contact.id)
#    qaaa = random_contact.id
#    print(qaaa)
#    print('q')

#def test_edit_contact_middlename(app):
#    if app.contact.count() == 0:
#        app.contact.create(Contact(firstname="Test", middlename="Test", lastname="Test", nickname="test_contact1", address="some address, 1", home_number="+375293003030",
#                               mobile_number="+375294004040"))
#    old_contact_list = app.contact.get_contact_list()
#    app.contact.edit(Contact(middlename='M_ModifiedName'))
#    new_contact_list = app.contact.get_contact_list()
#    assert len(old_contact_list) == len(new_contact_list)


#def test_edit_contact_lastname(app):
#    if app.contact.count() == 0:
#        app.contact.create(Contact(firstname="Test", middlename="Test", lastname="Test", nickname="test_contact1", address="some address, 1", home_number="+375293003030",
#                               mobile_number="+375294004040"))
#    old_contact_list = app.contact.get_contact_list()
#    app.contact.edit(Contact(lastname='L_ModifiedName'))
#    new_contact_list = app.contact.get_contact_list()
#    assert len(old_contact_list) == len(new_contact_list)


#def test_edit_contact_nickname(app):
#    if app.contact.count() == 0:
#        app.contact.create(Contact(firstname="Test", middlename="Test", lastname="Test", nickname="test_contact1", address="some address, 1", home_number="+375293003030",
#                               mobile_number="+375294004040"))
#    old_contact_list = app.contact.get_contact_list()
#    app.contact.edit(Contact(nickname='N_ModifiedName'))
#    new_contact_list = app.contact.get_contact_list()
#    assert len(old_contact_list) == len(new_contact_list)


#def test_edit_contact_address(app):
#    if app.contact.count() == 0:
#        app.contact.create(Contact(firstname="Test", middlename="Test", lastname="Test", nickname="test_contact1", address="some address, 1", home_number="+375293003030",
#                               mobile_number="+375294004040"))
#    old_contact_list = app.contact.get_contact_list()
#    app.contact.edit(Contact(address='A_ModifiedName'))
#    new_contact_list = app.contact.get_contact_list()
#    assert len(old_contact_list) == len(new_contact_list)


#def test_edit_contact_home_number(app):
#    if app.contact.count() == 0:
#        app.contact.create(Contact(firstname="Test", middlename="Test", lastname="Test", nickname="test_contact1", address="some address, 1", home_number="+375293003030",
#                               mobile_number="+375294004040"))
#    old_contact_list = app.contact.get_contact_list()
#    app.contact.edit(Contact(home_number='HN_ModifiedName'))
#    new_contact_list = app.contact.get_contact_list()
#    assert len(old_contact_list) == len(new_contact_list)


#def test_edit_contact_mobile_number(app):
#    if app.contact.count() == 0:
#        app.contact.create(Contact(firstname="Test", middlename="Test", lastname="Test", nickname="test_contact1", address="some address, 1", home_number="+375293003030",
#                               mobile_number="+375294004040"))
#    old_contact_list = app.contact.get_contact_list()
#    app.contact.edit(Contact(mobile_number='MN_ModifiedName'))
#    new_contact_list = app.contact.get_contact_list()
#    assert len(old_contact_list) == len(new_contact_list)