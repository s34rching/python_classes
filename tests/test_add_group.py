# -*- coding: utf-8 -*-
from models.group import Group


def test_test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(group_name="test_group", header="some_text", footer="some_text"))
    app.session.logout()


def test_add_empty_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(group_name="", header="", footer=""))
    app.session.logout()
