# -*- coding: utf-8 -*-
from models.group import Group
import pytest


def test_test_add_group(app, orm, json_groups, check_ui):
    group = json_groups
    with pytest.allure.step('Given a group list'):
        old_group = orm.get_group_list()
    with pytest.allure.step('When I add a new group %s to the list' % group):
        app.group.create(group)
    with pytest.allure.step('Then the new group is equal to the old list with the added group'):
        new_group = orm.get_group_list()
        old_group.append(group)
        assert sorted(new_group, key=Group.id_or_max) == sorted(old_group, key=Group.id_or_max)
        if check_ui:
            assert sorted(new_group, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)
