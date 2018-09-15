# Base class sql command

CREATE = ''' CREATE TABLE IF NOT EXISTS {} ({})'''
SAVE = '''INSERT INTO {} VALUES ({})'''
SAVE_DICT = '''INSERT INTO {} ({}) VALUES ({})'''
UPDATE_WHERE = '''UPDATE {} SET {} WHERE {}'''
UPDATE = '''UPDATE {} SET {}'''
DELETE = '''DELETE FROM {} WHERE {}'''
DELETE_WHERE = '''DELETE FROM {}'''
F_KEY = 'FOREIGN KEY ({}) REFERENCES {}(id)'
PRAGMA = '''PRAGMA foreign_keys = ON'''

# Query class sql command

ALL = '''SELECT * FROM {}'''
ORDER_BY = '''SELECT {} FROM {} ORDER BY {}'''
ORDER_BY_DESC = '''SELECT {} FROM {} ORDER BY {} DESC'''
ORDER_BY_ASC = '''SELECT {} FROM {} ORDER BY {} ASC'''
FILTER = '''SELECT {} FROM {} WHERE {}'''
BETWEEN = '''SELECT {} FROM {} WHERE {} BETWEEN {}'''
