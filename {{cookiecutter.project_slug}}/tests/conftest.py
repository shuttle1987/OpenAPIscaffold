"""Configration for pytest to run the test suite"""
import pytest

from {{cookiecutter.project_slug}}.app import create_app
from {{cookiecutter.project_slug}}.settings import TestConfig

app = create_app(TestConfig)

@pytest.fixture
def client():
    with app.test_client() as c:
        yield c