from models.contact import Contact
import random
import string


constant = [
    Contact(firstname='name1', lastname='lastname1',
            address='some_address', home_number='375295580000',
            mobile_number='375295580000', work_number='375295580000',
            secondary_number='375295580000', email='email@email.com',
            email2='email2@email.com', email3='email3@email.com'),
    Contact(firstname='name2', lastname='lastname2',
            address='some_address2', home_number='375295580000222',
            mobile_number='375295580000222', work_number='375295580000222',
            secondary_number='375295580000222', email='2email@email.com',
            email2='2email2@email.com', email3='2email3@email.com')]


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