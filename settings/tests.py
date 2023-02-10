from django.db import connections, DEFAULT_DB_ALIAS
from django_nose import NoseTestSuiteRunner

class TestRunner(NoseTestSuiteRunner):
    def setup_databases(self):
        result = super(TestRunner, self).setup_databases()

        connection = connections[DEFAULT_DB_ALIAS]
        cursor = connection.cursor()
        cursor.execute('CREATE EXTENSION HSTORE')

        return result