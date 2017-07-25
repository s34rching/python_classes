from models.group import Group

class GroupHelper:

    def __init__(self, app):
        self.app = app

    def open_group_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith('/group.php') and len(wd.find_elements_by_name('new')) > 0):
            wd.find_element_by_link_text("groups").click()

    def create(self, group):
        wd = self.app.wd
        self.open_group_page()
        # init group creation
        wd.find_element_by_name("new").click()
        # fill creating form
        self.fill_group_form(group)
        # submit group cretion
        wd.find_element_by_name("submit").click()
        self.return_to_group_page()
        self.group_cache = None

    def select_first_group(self):
        wd = self.app.wd
        wd.find_element_by_xpath('//input[@name="selected[]"]').click()

    def select_group_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name('selected[]')[index].click()

    def change_field_value(self, group_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(group_name).click()
            wd.find_element_by_name(group_name).clear()
            wd.find_element_by_name(group_name).send_keys(text)

    def fill_group_form(self, group):
        wd = self.app.wd
        self.change_field_value('group_name', group.name)
        self.change_field_value('group_header', group.header)
        self.change_field_value('group_footer', group.footer)

    def return_to_group_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()

    def delete(self):
        wd = self.app.wd
        self.open_group_page()
        self.select_first_group()
        if not wd.find_element_by_name("selected[]").is_selected():
            wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath('//input[@name="delete"]').click()
        self.return_to_group_page()
        self.group_cache = None

    def delete_some_group(self, index):
        wd = self.app.wd
        self.open_group_page()
        self.select_group_by_index(index)
        wd.find_element_by_xpath('//input[@name="delete"]').click()
        self.return_to_group_page()
        self.group_cache = None

    def modify(self, new_group_data):
        wd = self.app.wd
        self.open_group_page()
        self.select_first_group()
        wd.find_element_by_name('edit').click()
        self.fill_group_form(new_group_data)
        wd.find_element_by_name('update').click()
        self.return_to_group_page()
        self.group_cache = None

    def modify_some_group(self, new_group_data, index):
        wd = self.app.wd
        self.open_group_page()
        self.select_group_by_index(index)
        wd.find_element_by_name('edit').click()
        self.fill_group_form(new_group_data)
        wd.find_element_by_name('update').click()
        self.return_to_group_page()
        self.group_cache = None

    def count(self):
        wd = self.app.wd
        self.open_group_page()
        return len(wd.find_elements_by_name('selected[]'))

    group_cache = None

    def get_group_list(self):
        if self.group_cache is None:
            wd = self.app.wd
            self.open_group_page()
            self.group_cache = []
            for element in wd.find_elements_by_xpath("//span[@class='group']"):
                text = element.text
                id = element.find_element_by_name('selected[]').get_attribute('value')
                self.group_cache.append(Group(name=text, id=id))
        return list(self.group_cache)