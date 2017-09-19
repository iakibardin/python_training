
from model.contact import Contact
import random

def test_delete_first_contact(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="test", middlename="test", lastname="test", nickname="test", photo_directory="C:\\Users\\ikibardin\\Desktop\\newscreen.jpg",                              title="test",
                                   company="test", address="test", home_number="11111", mobile_number="22222", work_number="33333", fax="44444", email1="mail1", email2="mail2", email3="mail3", homepage="test.com",
                                   day_of_birth="//div[@id='content']/form/select[1]//option[3]",
                                   month_of_birth="//div[@id='content']/form/select[2]//option[2]", year_of_birth="1990",
                                   day_of_annivesary="//div[@id='content']/form/select[3]//option[3]",
                                   month_of_annivesary="//div[@id='content']/form/select[4]//option[2]", year_of_annivesary="2010", address2="test test test 1",
                                   home_number2="test test test 3", note="testnote"))

    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    app.contact.delete_contact_by_id(contact.id)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts.remove(contact)
    assert old_contacts == new_contacts

