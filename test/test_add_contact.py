# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
from data.contacts import constant as testdata




def test_add_contact(app, db, json_contacts):
    contact = json_contacts
    old_contacts = db.get_contact_list()
    app.contact.create(contact)
    new_contacts = db.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)











#def test_add_contact(app):
#        old_contacts = app.contact.get_contact_list()
#        contact = Contact(firstname="test", middlename="test", lastname="test", nickname="test", photo_directory="C:\\Users\\ikibardin\\Desktop\\newscreen.jpg",                              title="test",
#                                   company="test", address="test", home_number="11111", mobile_number="22222", work_number="33333", fax="44444", email1="mail1", email2="mail2", email3="mail3", homepage="test.com",
#                                   day_of_birth="//div[@id='content']/form/select[1]//option[3]",
#                                   month_of_birth="//div[@id='content']/form/select[2]//option[2]", year_of_birth="1990",
#                                   day_of_annivesary="//div[@id='content']/form/select[3]//option[3]",
#                                   month_of_annivesary="//div[@id='content']/form/select[4]//option[2]", year_of_annivesary="2010", address2="test test test 1",
#                                   home_number2="55555", note="testnote")
#
#        app.contact.create(contact)
#        assert len(old_contacts) + 1 == app.contact.count()
#        new_contacts = app.contact.get_contact_list()
#        old_contacts.append(contact)
#        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

