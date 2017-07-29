# -*- coding: utf-8 -*-
from models.group import Group


def test_test_add_group(app):
    old_group = app.group.get_group_list()
    group = Group(name="test_group", header="some_text", footer="some_text")
    app.group.create(group)
    assert len(old_group) + 1 == app.group.count()
    new_group = app.group.get_group_list()
    old_group.append(group)
    assert sorted(new_group, key=Group.id_or_max) == sorted(old_group, key=Group.id_or_max)


def test_add_empty_group(app):
    old_group = app.group.get_group_list()
    group = Group(name="", header="", footer="")
    app.group.create(group)
    assert len(old_group) + 1 == app.group.count()
    new_group = app.group.get_group_list()
    old_group.append(group)
    assert sorted(new_group, key=Group.id_or_max) == sorted(old_group, key=Group.id_or_max)