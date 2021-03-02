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
    tests = unittest.TestLoader().discover('project/tests', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1

# docker-compose -f docker-compose-dev.yml run boiler python manage.py test

if __name__ == '__main__':
    cli()