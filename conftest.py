import pytest
from fixture.application import Application
from selenium.webdriver.common.keys import Keys
<<<<<<< HEAD
import os.path
import json
import importlib
=======
>>>>>>> parent of 51bdc5c... Загрузка информации из конфига


fixture = None


@pytest.fixture
def app(request):
    global fixture
    if fixture is None:
        browser = request.config.getoption("--browser")
        base_url = request.config.getoption("--baseUrl")
        fixture = Application(browser=browser, base_url=base_url)
    else:
        if not fixture.is_valid():
            fixture = Application()
    fixture.session.ensure_login(username="admin", password="secret")
    return fixture

@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox")
<<<<<<< HEAD
    parser.addoption("--target", action="store", default="target.json")

def pytest_generate_tests(metafunc):
    for fixture in metafunc.fixturenames:
        if fixture.startswith("data_"):
            testdata = load_from_module(fixture[5:])
            metafunc.parametrize(fixture, testdata, ids=[str(x) for x in testdata])

def load_from_module(module):
    return  importlib.import_module("data.%s" % module).testdata
=======
    parser.addoption("--baseUrl", action="store", default="http://localhost/addressbook/")
>>>>>>> parent of 51bdc5c... Загрузка информации из конфига
