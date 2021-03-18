import coverage

COV = coverage.coverage(
    branch=True,
    include="project/*",
    omit=[
        "project/tests/*",
        "project/config.py",
        "project/api/models.py",
        "project/api/__init__.py",
        "project/__init__.py",
    ],
)
COV.start()

import unittest

from project import create_app
from flask.cli import FlaskGroup
from flask import current_app
from database_singleton import Singleton

# Config coverage report
app = create_app()
cli = FlaskGroup(create_app=create_app)
db = Singleton().database_connection()

# new
@cli.command()
def recreate_db():
    db.drop_all()
    db.create_all()
    db.session.commit()


@cli.command()
def test():
    """ Runs the tests without code coverage"""
    tests = unittest.TestLoader().discover("project/tests", pattern="test*.py")
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1


@cli.command()
def cov():
    """Runs the unit tests with coverage."""
    tests = unittest.TestLoader().discover("project/tests")
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        COV.stop()
        COV.save()
        print("Coverage Summary:")
        COV.report()
        COV.html_report()
        COV.xml_report()
        return 0
    return 1


if __name__ == "__main__":
    cli()
