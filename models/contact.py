from sys import maxsize


class Contact:

    def __init__(self, firstname=None, lastname=None, address=None, home_number=None, mobile_number=None,
                 work_number=None, secondary_number=None, email=None, email2=None, email3=None, id=None,
                 all_phones_from_homepage=None, all_emails_from_homepage = None):
        self.firstname = firstname
        self.lastname = lastname
        self.address = address
        self.home_number = home_number
        self.mobile_number = mobile_number
        self.work_number = work_number
        self.secondary_number = secondary_number
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.id = id
        self.all_phones_from_homepage = all_phones_from_homepage
        self.all_emails_from_homepage = all_emails_from_homepage

    def __repr__(self):
       return "%s:%s:%s:%s:%s" % (self.id, self.lastname, self.firstname, self.mobile_number, self.address)

    def __eq__(self, other):
       return (self.id is None or other.id is None or self.id == other.id) and self.firstname == other.firstname and (self.lastname is None or other.lastname is None or self.lastname == other.lastname)

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize