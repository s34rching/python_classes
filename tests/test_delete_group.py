# -*- coding: utf-8 -*-
from models.group import Group
from random import randrange

def test_delete_group(app):
#    if app.group.count() == 0:
#        app.group.create(Group(name="test_group", header="some_text", footer="some_text"))
    old_group = app.group.get_group_list()
    index = randrange(len(old_group))
    app.group.delete_some_group(index)
    new_group = app.group.get_group_list()
    assert len(old_group) - 1 == len(new_group)