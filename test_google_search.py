import pytest
from selene.api import *


@pytest.fixture
def setup_browser():
    browser.open('https://google.com')
    browser.driver.set_window_size(1200, 600)

    yield

    browser.quit()


def test_google_search(setup_browser):
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('User-oriented Web UI browser tests in ...'))


def test_google_search_negative(setup_browser):
    browser.element('[name="q"]').should(be.blank).type("OMG!It'sRandomText!").press_enter()
    browser.element('[id="topstuff"]').should(have.text(f"Страницы, содержащие все слова запроса, не найдены."))
