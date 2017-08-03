# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
import time, unittest
import pytest
from group import Group
from application import Application

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture




def test_add_group(app):
    app.login(username="admin", password="secret")
    app.create_gropup(Group(name="1234", header="1234", footer="1234"))
    app.logout()

def test_add_empty_group(app):
    app.login(username="admin", password="secret")
    app.create_gropup(Group(name="", header="", footer=""))
    app.logout()


if __name__ == '__main__':
    unittest.main()
