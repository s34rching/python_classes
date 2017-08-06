# -*- coding: utf-8 -*-
from models.group import Group
import pytest
from data.groups import constant as testdata


@pytest.mark.parametrize('group', testdata, ids=[repr(x) for x in testdata])
def test_test_add_group(app, group):
    old_group = app.group.get_group_list()
    app.group.create(group)
    assert len(old_group) + 1 == app.group.count()
    new_group = app.group.get_group_list()
    old_group.append(group)
    assert sorted(new_group, key=Group.id_or_max) == sorted(old_group, key=Group.id_or_max)