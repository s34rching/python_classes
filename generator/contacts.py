from models.contact import Contact
import random
import string
import os.path
import jsonpickle
import getopt
import sys

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f", ["number of conatcts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 10
f = 'data/contacts.json'

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a

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

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', f)

with open(file, 'w') as out:
    jsonpickle.set_encoder_options('json', indent=2)
    out.write(jsonpickle.encode(testdata))
