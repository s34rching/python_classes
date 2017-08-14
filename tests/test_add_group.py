# -*- coding: utf-8 -*-
from models.group import Group


def test_test_add_group(app, db, json_groups, check_ui):
    group = json_groups
    old_group = map(db.get_group_list())
    app.group.create(group)
    new_group = db.get_group_list()
    old_group.append(group)
    assert sorted(new_group, key=Group.id_or_max) == sorted(old_group, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_group, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)
