import re
import random


def test_contact_data_from_home_page(app):
    r_index = random.randrange(len(app.contact.get_contact_list()))
    data_from_home_page = app.contact.get_contact_list()[r_index]
    data_from_edit_page = app.contact.get_contact_info_from_edit_page(r_index)
    assert data_from_home_page.firstname == data_from_edit_page.firstname
    assert data_from_home_page.lastname == data_from_edit_page.lastname
    assert data_from_home_page.address == data_from_edit_page.address
    assert data_from_home_page.all_phones_from_homepage == merge_phones_like_on_homepage(data_from_edit_page)
    assert data_from_home_page.all_emails_from_homepage == merge_emails_like_on_homepage(data_from_edit_page)
    assert data_from_home_page.id == data_from_edit_page.id


def test_phones_from_view_page(app):
    r_index = random.randrange(len(app.contact.get_contact_list()))
    data_from_view_page = app.contact.get_contact_info_from_view_page(r_index)
    data_from_edit_page = app.contact.get_contact_info_from_edit_page(r_index)
    assert data_from_view_page.home_number == data_from_edit_page.home_number
    assert data_from_view_page.mobile_number == data_from_edit_page.mobile_number
    assert data_from_view_page.work_number == data_from_edit_page.work_number
    assert data_from_view_page.secondary_number == data_from_edit_page.secondary_number


def clear(s):
    return re.sub('[() -]', '', s)

def merge_phones_like_on_homepage(contact):
    return '\n'.join(filter(lambda x: x!= '',
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                    [contact.home_number, contact.work_number, contact.mobile_number, contact.secondary_number]))))

def merge_emails_like_on_homepage(contact):
    return '\n'.join(filter(lambda x: x!= '',
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                    [contact.email, contact.email2, contact.email3]))))