# -*- coding: utf-8 -*-
from models.group import Group


def test_test_add_group(app):
    old_group = app.group.get_group_list()
    app.group.create(Group(group_name="test_group", header="some_text", footer="some_text"))
    new_group = app.group.get_group_list()
    assert len(old_group) + 1 == len(new_group)


def test_add_empty_group(app):
    old_group = app.group.get_group_list()
    app.group.create(Group(group_name="", header="", footer=""))
    new_group = app.group.get_group_list()
    assert len(old_group) + 1 == len(new_group)