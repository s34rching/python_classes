from pytest_bdd import given, when, then
from models.group import Group
import random

@given('a group list')
def group_list(orm):
    return orm.get_group_list()

@given('a group with attributes <name>, <header> and <footer>')
def new_group(name, header, footer):
    return Group(name=name, header=header, footer=footer)

@when('I add a new group to the list')
def add_new_group(app, new_group):
    app.group.create(new_group)

@then('the new group is equal to the old list with the added group')
def verify_group_added(orm, group_list):
    old_groups = group_list
    new_groups = orm.get_group_list()
    old_groups.append(new_group)
    assert sorted(new_groups, key=Group.id_or_max) == sorted(old_groups, key=Group.id_or_max)

@given('a non-empty group list')
def old_groups_list(app, orm):
    if len(orm.get_group_list()) == 0:
        app.group.create(Group(name="test_group", header="some_text", footer="some_text"))
    return orm.get_group_list()

@given('a random group from the list')
def random_group(old_groups_list):
    return random.choice(old_groups_list)

@when('I delete a new group to the list')
def delete_random_group(app, random_group):
    app.group.delete_some_group_by_id(random_group.id)

@then('the new group is equal to the old list without the deleted group')
def verify_group_deleted(orm, old_groups_list, random_group):
    new_group_list = orm.get_group_list()
    old_groups_list.remove(random_group)
    assert old_groups_list == new_group_list