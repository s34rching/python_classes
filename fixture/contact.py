from models.contact import Contact

class ContactHelper:

    def __init__(self, app):
        self.app = app

    def open_home_page(self):
        wd = self.app.wd
        wd.get("http://localhost/addressbook/")

    def init_contact_creation(self):
        wd = self.app.wd
        # init contact creating
        wd.find_element_by_link_text("add new").click()

    def create(self, contact):
        wd = self.app.wd
        self.init_contact_creation()
        # create new contact
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.firstname)
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(contact.middlename)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.lastname)
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(contact.nickname)
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(contact.address)
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(contact.home_number)
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(contact.mobile_number)
        wd.find_element_by_name("work").click()
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys(contact.work_number)
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(contact.email)
        wd.find_element_by_name("phone2").click()
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys(contact.secondary_number)
        wd.find_element_by_xpath("//div[@id='content']/form/input[@type='submit']").click()
        self.return_to_homepage()
        self.contact_cache = None

    def return_to_homepage(self):
        wd = self.app.wd
        # return to the homepage
        wd.find_element_by_link_text("home").click()

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def type(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.type('firstname', contact.firstname)
        self.type('middlename', contact.middlename)
        self.type('lastname', contact.lastname)
        self.type('nickname', contact.nickname)
        self.type('address', contact.address)
        self.type('home', contact.home_number)
        self.type('mobile', contact.mobile_number)

    def delete_contact(self):
        wd = self.app.wd
        # select contact
        self.select_first_contact()
        # init deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        # submit deletion
        wd.switch_to_alert().accept()
        self.return_to_homepage()
        self.contact_cache = None

    def delete_some_contact(self, index):
        wd = self.app.wd
        # select contact
        self.select_contact_by_index(index)
        # init deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        # submit deletion
        wd.switch_to_alert().accept()
        self.return_to_homepage()
        self.contact_cache = None

    def edit_some_contact(self, new_group_data, index):
        wd = self.app.wd
        self.select_contact_by_index(index)
        # init edition
        wd.find_elements_by_xpath("//img[@alt='Edit']")[index].click()
        # modify contact data
        self.fill_contact_form(new_group_data)
        # submit modifying
        wd.find_element_by_name('update').click()
        # return to homepage
        self.return_to_homepage()
        self.contact_cache = None

    def count(self):
        wd = self.app.wd
        return len(wd.find_elements_by_name('selected[]'))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.contact_cache = []
            for element in wd.find_elements_by_name("entry"):
                cells = element.find_elements_by_tag_name("td")
                lastname = cells[1].text
                firstname = cells[2].text
                address = cells[3].text
                email = cells[4].text
                all_phones = cells[5].text.splitlines()
                id = cells[0].find_element_by_tag_name('input').get_attribute('value')
                self.contact_cache.append(Contact(firstname=firstname, lastname=lastname,
                                                  home_number=all_phones[0], mobile_number=all_phones[1],
#                                                  work_number=all_phones[2], secondary_number=all_phones[3],
                                                  address=address, email=email, id=id))
        return list(self.contact_cache)

    def open_contact_to_edit_by_index(self, c_index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_name('entry')[c_index]
        cell = row.find_elements_by_tag_name('td')[7]
        cell.find_element_by_tag_name('a').click()

#    def open_contact_view_by_index(self, c_index):
#        wd = self.app.wd
#        self.app.open_home_page()
#        row = wd.find_elements_by_name('entry')[c_index]
#        cell = row.find_elements_by_tag_name('tr')[6]
#        cell.find_element_by_tag_name('a').click()

    def get_contact_info_from_edit_page(self, c_index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(c_index)
        firstname = wd.find_element_by_name('firstname').get_attribute('value')
        lastname = wd.find_element_by_name('lastname').get_attribute('value')
        address = wd.find_element_by_name('address').get_attribute('value')
        home_number = wd.find_element_by_name('home').get_attribute('value')
        mobile_number = wd.find_element_by_name('mobile').get_attribute('value')
        work_number = wd.find_element_by_name('work').get_attribute('value')
        email = wd.find_element_by_name('email').get_attribute('value')
        secondary_number = wd.find_element_by_name('phone2').get_attribute('value')
        id = wd.find_element_by_name('id').get_attribute('value')
        return Contact(firstname=firstname, lastname=lastname, address=address, home_number=home_number,
                       mobile_number=mobile_number, work_number=work_number,
                       email=email, secondary_number=secondary_number, id=id)