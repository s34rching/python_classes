from models.group import Group

def test_edit_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(group_name='ListWasEmpty'))
    app.group.modify(Group(group_name='ModifiedName'))


def test_edit_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(group_name='ListWasEmpty'))
    app.group.modify(Group(header='ModifiedName'))


def test_edit_group_footer(app):
    if app.group.count() == 0:
        app.group.create(Group(group_name='ListWasEmpty'))
    app.group.modify(Group(footer='ModifiedName'))