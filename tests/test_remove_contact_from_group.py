from models.group import Group
from models.contact import Contact


def test_remove_contact_from_group(app, db, orm):
    # check if there is any contact-group in 'address_in_groups' table
    relations = len(db.get_relations_list())
    # if there is no contacts in group create group and contact in group
    if relations == 0:
        group = Group(name='Group_to_add', header='header_to_add', footer='footer_to_add')
        app.group.create(group)
        contact = Contact(firstname='Contact_to_add', lastname='Contact_to_add', address='Contact_to_add', home_number='358522', mobile_number='65464464')
        app.contact.create_contact_with_adding_to_group(contact)
    # get first group id in 'address_in_groups' table
    group_id = db.get_relations_list()[0].group_id
    # get first contact id for contact in selected group
    contact_id = orm.get_contacts_in_group(Group(id=group_id))[0].id
    # remove contact from selected group
    app.contact.remove_contact_from_group(contact_id, group_id)
    # get new list of contacts in selected groups
    new_contact_in_group_list = orm.get_contacts_in_group(Group(id=group_id))
    # create list where add ids of contacts in the selected group in
    contact_id_list = []
    # get ids of contacts in selected group
    for contact in new_contact_in_group_list:
        id = contact.id
        contact_id_list.append(id)
    # assert removed contact id is not in list of contacts of the selected group
    assert contact_id not in contact_id_list



