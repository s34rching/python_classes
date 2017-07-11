# -*- coding: utf-8 -*-
from models.contact import Contact


def test_delete_contact_firstname(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit(Contact(firstname='F_ModifiedName'))
    app.session.logout()


def test_delete_contact_middlename(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit(Contact(middlename='M_ModifiedName'))
    app.session.logout()


def test_delete_contact_lastname(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit(Contact(lastname='L_ModifiedName'))
    app.session.logout()


def test_delete_contact_nickname(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit(Contact(nickname='N_ModifiedName'))
    app.session.logout()


def test_delete_contact_address(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit(Contact(address='A_ModifiedName'))
    app.session.logout()


def test_delete_contact_home_number(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit(Contact(home_number='HN_ModifiedName'))
    app.session.logout()


def test_delete_contact_mobile_number(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit(Contact(mobile_number='MN_ModifiedName'))
    app.session.logout()