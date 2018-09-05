import sqlite3
import decorators
import logging
from query import Query
from dbconfig import connection

logging.basicConfig(format=u' %(message)s', level=logging.INFO)


class Base:

    query_class = Query
  
    def __init__(self, *args, **kwargs):

        self.args = args
        self.kwargs = kwargs
    
    def get_field_name(self):
        fkey_list = []
        field_list = []
        class_dict = dict(self.__class__.__dict__)
        for key, value in class_dict.items():
            if not key.startswith('__'):
                f_arg = value.__dict__['sqlite_type']
                field_list.append('{} {}'.format(key, f_arg))

        for key, value in class_dict.items():
            if not key.startswith('__'):
                if value.__class__.__name__.lower() == 'foreignkey':
                    fkey_list.append(key)
                    fkey_list.append(value.__dict__['args'][0])
        if fkey_list:
            fkey_string = 'FOREIGN KEY ({}) REFERENCES {}(id)'.format(
                fkey_list[0], fkey_list[1])
            field_list.append(fkey_string)
        return field_list

    def test(self):
        return dict(self.__class__.__dict__)

    def get_table_name(self):
        return self.__class__.__name__

    def create(self):
        table_name = self.get_table_name()
        field_list = self.get_field_name()
        table = ''' CREATE TABLE IF NOT EXISTS {} ({})''' .format(
            table_name, ', '.join(field_list))
        connection.execute(table)
        connection.commit()

    def get_arg_table(self):
        arg_dict = dict(self.__dict__)
        if len(arg_dict['args']) != 0:
            table_args = self.get_arg_from_typle(arg_dict['args'])
        elif len(arg_dict['kwargs']) != 0:
            table_args = self.get_arg_from_dict(arg_dict['kwargs'])
        else:
            table_args = None
        return table_args

    def get_arg_from_typle(self, args):
        arg_list = ['"' + str(i) + '"' for i in args]
        return arg_list

    def get_arg_from_dict(self, args):
        list_fild_names = []
        list_fild_args = []
        for key, value in args.items():
            list_fild_names.append(str(key))
            list_fild_args.append(str(value))
        list_fild_args = self.get_arg_from_typle(list_fild_args)
        return (list_fild_names, list_fild_args,)

    def save(self):
        table_name = self.get_table_name()
        table_args = self.get_arg_table()
        if table_args:
            if type(table_args).__name__ .lower() == 'list':
                table = ('''INSERT INTO {} VALUES ({})'''.format(
                    table_name, ', '.join(table_args)))
            else:
                table = ('''INSERT INTO {} ({}) VALUES ({})'''.format(
                        table_name, ', '.join(
                        table_args[0]), ', '.join(table_args[1])))
            connection.execute(table)
            connection.commit()
        else:
            logging.info('Нет значений для записи в таблицу!')

    def update(self, filters):
        table_name = self.get_table_name()
        table_args = self.get_arg_table()
        if kwargs:
            update_filter = self.get_update_filter(filters)
            table = '''UPDATE {} SET {} WHERE {}'''.format(table_name, table_args, update_filter)
            connection.execute(table)
            connection.commit()


    def get_update_filter(self, kwargs):
        update_filter = []
        for k, v in kwargs.items():
            update_filter =  ' = ' + '"' + v + '"'
        return update_filter



    @decorators.classproperty
    def query(cls):
        query_class = cls.query_class
        return query_class(orm_class=cls)

