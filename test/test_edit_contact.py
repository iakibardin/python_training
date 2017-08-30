from model.contact import Contact
from random import randrange

def test_edit_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test", middlename="test", lastname="test", nickname="test", photo_directory="C:\\Users\\ikibardin\\Desktop\\newscreen.jpg",                              title="test",
                                   company="test", address="test", home_number="11111", mobile_number="22222", work_number="33333", fax="44444", email1="mail1", email2="mail2", email3="mail3", homepage="test.com",
                                   day_of_birth="//div[@id='content']/form/select[1]//option[3]",
                                   month_of_birth="//div[@id='content']/form/select[2]//option[2]", year_of_birth="1990",
                                   day_of_annivesary="//div[@id='content']/form/select[3]//option[3]",
                                   month_of_annivesary="//div[@id='content']/form/select[4]//option[2]", year_of_annivesary="2010", address2="test test test 1",
                                   home_number2="test test test 3", note="testnote"))

    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact1 = (Contact(firstname="update", middlename="update", lastname="update", nickname="update",
                               photo_directory="C:\\Users\\ikibardin\\Desktop\\newscreen.jpg", title="update",
                               company="update", address="update", home_number="update", mobile_number="update",
                               work_number="update", fax="update", email1="update", email2="update", email3="update",
                               homepage="update.com",
                               day_of_birth="//div[@id='content']/form/select[1]//option[4]",
                               month_of_birth="//div[@id='content']/form/select[2]//option[3]", year_of_birth="1995",
                               day_of_annivesary="//div[@id='content']/form/select[3]//option[4]",
                               month_of_annivesary="//div[@id='content']/form/select[4]//option[3]",
                               year_of_annivesary="2015", address2="update update update 2",
                               home_number2="update update update 3", note="updatetestnote"))
    contact1.id = old_contacts[index].id
    app.contact.edit_contact_by_index(contact1, index)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[index] = contact1
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


