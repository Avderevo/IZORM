# Classes of model fields
class Integer:

    def __init__(self, nulable=True, primary_key=False):

        if primary_key:
            self.sqlite_type = 'INTEGER PRIMARY KEY'
        else:
            self.sqlite_type = 'INTEGER NULL' if nulable else 'INTEGER NOT NULL'


class String:

    def __init__(self, nulable=True):

        self.sqlite_type = 'TEXT NULL' if nulable else 'TEXT NOT NULL'


class ForeignKey:

    def __init__(self, *args):
        self.args = args
        self.sqlite_type = 'INTEGER NOT NULL'
