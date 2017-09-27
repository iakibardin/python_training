from model.contact import Contact
import re

def test_info_from_home_page(app, db):
    contact_list_db = sorted(map(app.contact.delete_spaces, db.get_contact_list()), key=Contact.id_or_max)
    contact_list_home_page = sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
    assert len(contact_list_db) == len(contact_list_home_page)
    assert contact_list_db == contact_list_home_page
    for index in range(0, len(contact_list_home_page)):
        contact_from_home_page = contact_list_home_page[index]
        contact_from_db = contact_list_db[index]
        assert contact_from_home_page.lastname == contact_from_db.lastname
        assert contact_from_home_page.firstname == contact_from_db.firstname
        assert contact_from_home_page.address == contact_from_db.address
        assert contact_from_home_page.all_emailes_from_home_page == merge_mail_cells(contact_from_db)
        assert contact_from_home_page.all_phones_from_home_page == merge_phone_cells(contact_from_db)


def clear(s):
    return re.sub("[() -]","",s)

def merge_mail_cells(contact):
    return "\n".join(filter(lambda x: x!="", filter(lambda x: x is not None, [contact.email1, contact.email2, contact.email3])))

def merge_phone_cells(contact):
    return "\n".join(filter(lambda x: x!="", map(lambda x: clear(x),
filter(lambda x: x is not None, [contact.home_number, contact.mobile_number, contact.work_number, contact.home_number2]))))