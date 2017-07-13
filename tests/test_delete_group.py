# -*- coding: utf-8 -*-
from models.group import Group


def test_delete_group(app):
    if app.group.count() == 0:
        app.group.create(Group(group_name="test_group", header="some_text", footer="some_text"))
    app.group.delete()