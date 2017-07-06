# -*- coding: utf-8 -*-
from models.contact import Contact

def test_delete_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit(Contact('ModifiedName', 'ModifiedMiddleName', 'ModifiedLastName', 'ModifiedNickname', 'ModifiedAddress', 'ModifiedHome_number', 'ModifiedMobile_number'))
    app.session.logout()