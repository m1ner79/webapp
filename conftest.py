import pytest

import app as webapp

import DBcm

from appconfig import config


@pytest.fixture
def app():
    """
    this fixture creates the client object before each test runs, assuming the test
    references the client object.
    """
    app = webapp.app
    return app


@pytest.fixture
def clean_up_db():
    """
    This code removes any and all test data from the database *after*
    the tests which refer to it run
    """
    # this code,before the yield, runs befre the test runs.
    yield
    # this code, after the yield, runs after the test completes.
    with DBcm.UseDatabase(config) as db:
        SQL = """
            delete from visitors
            where fname = "test"
        """
        db.execute(SQL)
        SQL = """
            delete from visitors
            where fname = "tester"
        """
        db.execute(SQL)
