class Integer:

    def __init__(self, nulable=True, primary_key=False):

        self.sqlite_type = 'TEXT NULL'

        if not nulable:
            self.sqlite_type = 'TEXT NOT NULL'
        if primary_key:
            self.sqlite_type = 'INTEGER PRIMARY KEY'


class String:

    def __init__(self, nulable=True):

        self.sqlite_type = 'TEXT NULL'

        if not nulable:
            self.sqlite_type = 'TEXT NOT NULL'


class ForeignKey:

    def __init__(self, *args):
        self.args = args
        self.sqlite_type = 'INTEGER NOT NULL'
