import mysql.connector
from models.group import Group
from models.contact import Contact
from models.relation import Relation


class DbFixture:

    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = mysql.connector.connect(host=host, database=name, user=user, password=password)
        self.connection.autocommit = True

    def get_group_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute('select group_id, group_name, group_header, group_footer from group_list')
            for row in cursor:
                (id, name, header, footer) = row
                list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return list

    def get_contact_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute('select id, lastname, firstname, address, mobile from addressbook where deprecated = "0000-00-00 00:00:00"')
            for row in cursor:
                (id, lastname, firstname, address, mobile) = row
                list.append(Contact(id=str(id), lastname=lastname, firstname=firstname, address=address, mobile_number=mobile))
        finally:
            cursor.close()
        return list

    def get_relations_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute('select id, group_id from address_in_groups')
            for row in cursor:
                (id, group_id) = row
                list.append(Relation(id=id, group_id=group_id))
        finally:
            cursor.close()
        return list

    def destroy(self):
        self.connection.close()