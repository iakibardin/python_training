# -*- coding: utf-8 -*-
import unittest

import pytest

from contact import Contact
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_contact(app):
        app.login(username="admin", password="secret")
        app.create_contact(Contact(firstname="test", middlename="test", lastname="test", nickname="test", photo_directory="C:\\Users\\ikibardin\\Desktop\\screen.jpg", title="test",
                            company="test", address="test", home_number="11111", mobile_number="22222", work_number="33333", fax="44444", email1="mail1", email2="mail2", email3="mail3", homepage="test.com",
                            day_of_birth="//div[@id='content']/form/select[1]//option[3]",
                            month_of_birth="//div[@id='content']/form/select[2]//option[2]", year_of_birth="1990",
                            day_of_annivesary="//div[@id='content']/form/select[3]//option[3]",
                            month_of_annivesary="//div[@id='content']/form/select[4]//option[2]", year_of_annivesary="2010", address2="test test test 1",
                            home_number2="test test test 3", note="testnote"))
        app.logout()

if __name__ == '__main__':
    unittest.main()
