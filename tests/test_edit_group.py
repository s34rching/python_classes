from models.group import Group
import random
from random import randrange


def test_edit_group_name(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name='FirstGroup'))
    app.group.open_group_page()
    old_group = db.get_group_list()
    index = randrange(len(old_group))
    random_group = old_group[index]
    group = Group(name='ModifiedName')
    group.id = random_group.id
    app.group.modify_some_group_by_id(group, random_group.id)
    new_group = db.get_group_list()
    old_group[index] = group
    assert sorted(new_group, key=Group.id_or_max) == sorted(old_group, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_group, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)



#def test_edit_group_header(app):
#    if app.group.count() == 0:
#        app.group.create(Group(name='ListWasEmpty'))
#    old_group = app.group.get_group_list()
#    app.group.modify(Group(header='ModifiedName'))
#    new_group = app.group.get_group_list()
#    assert len(old_group) == len(new_group)


#def test_edit_group_footer(app):
#    if app.group.count() == 0:
#        app.group.create(Group(name='ListWasEmpty'))
#    old_group = app.group.get_group_list()
#    app.group.modify(Group(footer='ModifiedName'))
#    new_group = app.group.get_group_list()
#    assert len(old_group) == len(new_group)