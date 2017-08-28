from pytest_bdd import given, when, then
from models.contact import Contact
import random
from random import randrange

@given('a contact list')
def contact_list(orm):
    return orm.get_contact_list()


@given('a contact with attributes <firstname>, <lastname>, <address>, <email>, <home_number>, <mobile_number>, <work_number>, <secondary_number>, <email2>, <email3>')
def new_contact(firstname, lastname, address, email, home_number, mobile_number, work_number, secondary_number, email2, email3):
    return Contact(firstname=firstname, lastname=lastname, address=address, email=email, home_number=home_number, work_number=work_number, mobile_number=mobile_number,
                   secondary_number=secondary_number, email2=email2, email3=email3)


@when('I add a new contact to the list')
def add_new_contact(app, new_contact):
    app.contact.create(new_contact)


@then('the new contact list is equal to the old list with the added contact')
def verify_contact_added(orm, new_contact, contact_list):
    old_contacts_list = contact_list
    new_contacts_list = orm.get_contact_list()
    old_contacts_list.append(new_contact)
    assert sorted(old_contacts_list, key=Contact.id_or_max) == sorted(new_contacts_list, key=Contact.id_or_max)


@given('a non-empty contact list')
def old_contact_list(app, orm):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Test", middlename="Test", lastname="Test", nickname="test_contact1",
                               address="some address, 1", home_number="+375293003030", mobile_number="+375294004040"))
    return orm.get_contact_list()


@given('a random contact from the list')
def random_contact(old_contact_list):
    return random.choice(old_contact_list)


@when('I delete a new contact from the list')
def delete_random_contact(app, random_contact):
    app.contact.delete_some_contact_by_id(random_contact.id)


@then('the new contct list is equal to the old list without the deleted contact')
def verify_contact_deleted(orm, random_contact, old_contact_list):
    new_contact_list = orm.get_contact_list()
    old_contact_list.remove(random_contact)
    assert old_contact_list == new_contact_list


@given('a non-empty contact list')
def old_contact_list(app, orm):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Test", middlename="Test", lastname="Test", nickname="test_contact1",
                               address="some address, 1", home_number="+375293003030", mobile_number="+375294004040"))
    return orm.get_contact_list()


@given('a random contact from the list')
def random_contact(old_contact_list):
    index = randrange(len(old_contact_list))
    return old_contact_list[index]


@given('a contact with new <firstname>')
def new_contact():
    return Contact(firstname='Mod_firstname')


@when('I edit a random contact from the list')
def edit_random_contact(app, random_contact, new_contact):
    app.contact.edit_some_contact_by_id(new_contact, random_contact.id)


@then('the new contact list is equal to the old list')
def verify_contact_edited(orm, old_contact_list):
    new_contact_list = orm.get_contact_list()
    assert sorted(old_contact_list, key=Contact.id_or_max) == sorted(new_contact_list, key=Contact.id_or_max)