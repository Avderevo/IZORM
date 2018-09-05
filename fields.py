
class Integer:
    def __init__(self, nulable=True, primary_key=False):
        if nulable:
            self.sqlite_type = 'INTEGER NULL'
        else:
            self.sqlite_type = 'INTEGER NOT NULL'
        if primary_key:
            self.sqlite_type = 'INTEGER PRIMARY KEY'


class String:
    def __init__(self, nulable=True):
        if nulable:
            self.sqlite_type = 'TEXT NULL'
        else:
            self.sqlite_type = 'TEXT NOT NULL'


class ForeignKey:
    def __init__(self, *args):
        self.args = args
        self.sqlite_type = 'INTEGER NOT NULL'

    def get_fkey(self):
        if self.args:
            return True
        else:
            return False

