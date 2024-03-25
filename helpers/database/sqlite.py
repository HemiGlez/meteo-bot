import sqlite3

import settings


class Database:
    DATABASE_FILE = settings.DATABASE_FILE
    connection = None
    cursor = None

    def _create_connection(self):
        self.connection = sqlite3.connect(self.DATABASE_FILE)

    def _get_cursor(self):
        self.cursor = self.connection.cursor()

    def _commit(self):
        self.connection.commit()

    def _close(self):
        self.connection.close()

    def execute(self, query: str, params: tuple = None):
        if params is None:
            params = ()
        self._create_connection()
        self._get_cursor()
        self.cursor.execute(query, params)
        self._commit()
        self._close()
