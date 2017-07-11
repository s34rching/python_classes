from models.group import Group

def test_edit_group_name(app):
    app.session.login(username="admin", password="secret")
    app.group.modify(Group(group_name='ModifiedName'))
    app.session.logout()


def test_edit_group_header(app):
    app.session.login(username="admin", password="secret")
    app.group.modify(Group(header='ModifiedName'))
    app.session.logout()


def test_edit_group_footer(app):
    app.session.login(username="admin", password="secret")
    app.group.modify(Group(footer='ModifiedName'))
    app.session.logout()