from models.group import Group


def test_edit_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(group_name='ListWasEmpty'))
    old_group = app.group.get_group_list()
    app.group.modify(Group(group_name='ModifiedName'))
    new_group = app.group.get_group_list()
    assert len(old_group) == len(new_group)


def test_edit_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(group_name='ListWasEmpty'))
    old_group = app.group.get_group_list()
    app.group.modify(Group(header='ModifiedName'))
    new_group = app.group.get_group_list()
    assert len(old_group) == len(new_group)


def test_edit_group_footer(app):
    if app.group.count() == 0:
        app.group.create(Group(group_name='ListWasEmpty'))
    old_group = app.group.get_group_list()
    app.group.modify(Group(footer='ModifiedName'))
    new_group = app.group.get_group_list()
    assert len(old_group) == len(new_group)