

def test_contact_data_from_home_page(app):
    data_from_home_page = app.contact.get_contact_list()[1]
    data_from_edit_page = app.contact.get_contact_info_from_edit_page(1)
    assert data_from_home_page.firstname == data_from_edit_page.firstname
    assert data_from_home_page.lastname == data_from_edit_page.lastname
    assert data_from_home_page.address == data_from_edit_page.address
    assert data_from_home_page.home_number == data_from_edit_page.home_number
    assert data_from_home_page.mobile_number == data_from_edit_page.mobile_number
    assert data_from_home_page.work_number == data_from_edit_page.work_number
    assert data_from_home_page.secondary_number == data_from_edit_page.secondary_number
    assert data_from_home_page.email == data_from_edit_page.email
    assert data_from_home_page.id == data_from_edit_page.id
