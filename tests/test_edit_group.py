from models.group import Group

def test_edit_group_name(app):
    app.group.modify(Group(group_name='ModifiedName'))


def test_edit_group_header(app):
    app.group.modify(Group(header='ModifiedName'))


def test_edit_group_footer(app):
    app.group.modify(Group(footer='ModifiedName'))