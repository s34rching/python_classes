# -*- coding: utf-8 -*-
from models.group import Group


def test_test_add_group(app, json_groups):
    group = json_groups
    old_group = app.group.get_group_list()
    app.group.create(group)
    assert len(old_group) + 1 == app.group.count()
    new_group = app.group.get_group_list()
    old_group.append(group)
    assert sorted(new_group, key=Group.id_or_max) == sorted(old_group, key=Group.id_or_max)