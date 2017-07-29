# -*- coding: utf-8 -*-
from models.contact import Contact
import random
import string
import pytest


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation +  ' '*10
    return prefix + ''.join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Contact(firstname='', lastname='', address='', home_number='', email='')] + [
    Contact(firstname=random_string('name', 10), lastname=random_string('lastname', 15),
            address=random_string('address', 15), home_number=random_string('hn', 15),
            mobile_number=random_string('mn', 15),work_number=random_string('wn', 15),
            secondary_number=random_string('sn', 15), email=random_string('address', 15),
            email2=random_string('email2', 15), email3=random_string('email3', 15))
    for i in range(5)
]


@pytest.mark.parametrize('contact', testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contact_list = app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(old_contact_list) + 1 == app.contact.count()
    new_contact_list = app.contact.get_contact_list()
    old_contact_list.append(contact)
    assert sorted(old_contact_list, key=Contact.id_or_max) == sorted(new_contact_list, key=Contact.id_or_max)
