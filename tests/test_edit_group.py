from models.group import Group

def test_edit_group(app):
    app.session.login(username="admin", password="secret")
    app.group.edit(Group('ModifiedName', 'ModifiedHeader', 'ModifiedFooter'))
    app.session.logout()