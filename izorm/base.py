import decoratorms
import logging
from query import Query
from dbconfig import connection
from exception import QueryFieldException, EmptyArgsException

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
                    self.foreign_keys_on()
        if fkey_list:
            fkey_string = 'FOREIGN KEY ({}) REFERENCES {}(id)'.format(
                fkey_list[0], fkey_list[1])
            field_list.append(fkey_string)
        return field_list

    def get_list_fields(self):
        fields_list = []
        class_dict = dict(self.__class__.__dict__)
        for key, value in class_dict.items():
            if not key.startswith('__'):
                fields_list.append(str(key))
        return fields_list

    def foreign_keys_on(self):
        f = '''PRAGMA foreign_keys = ON'''
        connection.execute(f)
        connection.commit()

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
        table_args = None
        arg_dict = dict(self.__dict__)
        if len(arg_dict['args']):
            table_args = self.get_arg_from_tuple(arg_dict['args'])
        if len(arg_dict['kwargs']):
            table_args = self.get_arg_from_dict(arg_dict['kwargs'])
        return table_args

    def get_arg_from_tuple(self, args):
        arg_list = ['"' + str(i) + '"' for i in args]
        return arg_list

    def get_arg_from_dict(self, args):
        list_fild_names = []
        list_fild_args = []
        for key, value in args.items():
            list_fild_names.append(str(key))
            list_fild_args.append(str(value))
        list_fild_args = self.get_arg_from_tuple(list_fild_args)
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
            raise EmptyArgsException('No values to write to the table!')

    def update(self, **kwargs):
        table_name = self.get_table_name()

        table_args = self.get_update_args()

        if kwargs:
            update_filter = self.get_update_filter(kwargs)
            table = '''UPDATE {} SET {} WHERE {}'''.format(
                table_name, ', '.join(table_args), update_filter)
        else:
            table = '''UPDATE {} SET {}'''.format(
                table_name, ', '.join(table_args))
        connection.execute(table)
        connection.commit()

    def get_update_filter(self, kwargs):
        update_filter = []
        for k, v in kwargs.items():
            if k in self.get_list_fields():
                update_filter = k + '=' + '"' + v + '"'
            else:
                logging.info(
                    'В модели отсутствует указаное поле сортировки:{}'.format(
                        kwargs.keys()))
                raise QueryFieldException(
                    'The model does not have the indicated sorting field {}'.format(
                        kwargs.keys()))
        return update_filter

    def get_update_args(self):
        update_args = []
        for k, v in dict(self.__dict__)['kwargs'].items():
            arg = k + '=' + '"' + v + '"'
            update_args.append(arg)
        return update_args

    def delete(self, **kwargs):
        table_name = self.get_table_name()
        if kwargs:
            delete_filter = self.get_update_filter(kwargs)
            table = '''DELETE FROM {} WHERE {}'''.format(
                table_name, delete_filter)
        else:
            table = '''DELETE FROM {}'''.format(table_name)
        connection.execute(table)

    @decoratorms.classproperty
    def query(cls):
        query_class = cls.query_class
        return query_class(orm_class=cls)

