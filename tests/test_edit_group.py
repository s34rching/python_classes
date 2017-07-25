from models.group import Group
from random import randrange


def test_edit_group_name(app):
#    if app.group.count() == 0:
#        app.group.create(Group(name='ListWasEmpty'))
#    app.group.open_group_page()
    old_group = app.group.get_group_list()
    group = Group(name='ModifiedName')
    group.id = old_group[0].id
    index = randrange(len(old_group))
    app.group.modify_some_group(group, index)
    assert len(old_group) == app.group.count()
    new_group = app.group.get_group_list()
    old_group[0] = group
    assert sorted(new_group, key=Group.id_or_max) == sorted(old_group, key=Group.id_or_max)

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