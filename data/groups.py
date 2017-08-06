from models.group import Group
import random
import string

constant = [
    Group(name='f_group', header='f_header', footer='f_footer'),
    Group(name='2f_group', header='2f_header', footer='2f_footer'),
]

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation +  ' '*10
    return prefix + ''.join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = [Group(name="", header="", footer="")] + [
    Group(name=random_string('name', 10), header=random_string('header', 15), footer=random_string('footer', 15))
    for i in range(5)
]
