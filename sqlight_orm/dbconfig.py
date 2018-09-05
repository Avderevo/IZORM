import sqlite3
import logging


logging.basicConfig(format=u' %(message)s', level=logging.INFO)


class Connection(object):

    def __init__(self):
        self.db = None
        self.connection = None
        self._cursor = None

    def connect(self, db_name=":memory:"):

        if self.connection:

            try:
                self.close()
            except Exception:
                logging.info("Can't close connection")
        self.db = db_name
        self.connection = sqlite3.connect(self.db)
        return self

    @property
    def connected(self):

        if self.connection:
            return True
        return False

    def execute(self, values):

        new_cursor = self.cursor
        new_cursor.execute(values)
        return new_cursor

    @property
    def cursor(self):

#        if self._cursor:
#            self._cursor.close()
        self._cursor = self.connection.cursor()
        return self._cursor

    def commit(self):
        self.connection.commit()

    def close(self):
        """
        Attemps to close the current connection and cursor.
        """
        if self.connection:
            if self._cursor:
                self._cursor.close()
                self._cursor = None
            self.connection.close()
            self.connection = None

    def __del__(self):
        self.close()


connection = Connection()  


def connect(*args, **kwargs):
    """ The connect function """
    return connection.connect(*args, **kwargs)

def cursor():
    """ The cursor function """
    return connection.cursor