import pytest
from fixture.application import Application
from selenium.webdriver.common.keys import Keys

@pytest.fixture(scope = "session")
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture