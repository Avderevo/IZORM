import decoratorms
import logging
from query import Query
from dbconfig import connection
from exception import QueryFieldException, EmptyArgsException
import sqlines

logging.basicConfig(format=u' %(message)s', level=logging.INFO)


class Base:
    '''
    Super class for the Model class.
    In the Base class, the following methods are implemented:
    create a table, write data to a table, update the data,
    and delete data from the table.
    '''

    query_class = Query

    def __init__(self, *args, **kwargs):

        self.args = args
        self.kwargs = kwargs
        self.arg_dict = dict(self.__dict__)['kwargs']
        self.arg_tuple = dict(self.__dict__)['args']
        self.class_dict = dict(self.__class__.__dict__)
        self.table_name = self.__class__.__name__
    
    def get_field_name(self):
        fkey_list = []
        field_list = []
        for key, value in self.class_dict.items():
            if not key.startswith('__'):
                f_arg = value.__dict__['sqlite_type']
                field_list.append('{} {}'.format(key, f_arg))

        for key, value in self.class_dict.items():
            if not key.startswith('__'):
                if value.__class__.__name__.lower() == 'foreignkey':
                    fkey_list.append(key)
                    fkey_list.append(value.__dict__['args'][0])
                    self.foreign_keys_on()
        if fkey_list:
            fkey_string = sqlines.F_KEY.format(
                fkey_list[0], fkey_list[1])
            field_list.append(fkey_string)
        return field_list

    def get_list_fields(self):
        fields_list = []
        for key, value in self.class_dict.items():
            if not key.startswith('__'):
                fields_list.append(str(key))
        return fields_list

    def foreign_keys_on(self):
        f = sqlines.PRAGMA
        connection.execute(f)
        connection.commit()

    def create(self):
        field_list = self.get_field_name()
        table = sqlines.CREATE.format(
            self.table_name, ', '.join(field_list))
        connection.execute(table)
        connection.commit()

    def get_arg_table(self):
        if self.arg_tuple:
            table_args = self.get_arg_from_tuple(self.arg_tuple)
        else:
            table_args = self.get_arg_from_dict(self.arg_dict)
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
        table_args = self.get_arg_table()
        if table_args:
            if type(table_args).__name__ .lower() == 'list':
                table = sqlines.SAVE.format(
                    self.table_name, ', '.join(table_args))
            else:
                table = sqlines.SAVE_DICT.format(
                    self.table_name, ', '.join(
                        table_args[0]), ', '.join(table_args[1]))
            connection.execute(table)
            connection.commit()
        else:
            logging.info('Нет значений для записи в таблицу!')
            raise EmptyArgsException('No values to write to the table!')

    def update(self, **kwargs):
        table_args = self.get_update_args()
        if kwargs:
            update_filter = self.get_update_filter(kwargs)
            table = sqlines.UPDATE_WHERE.format(
                self.table_name, ', '.join(table_args), update_filter)
        else:
            table = sqlines.UPDATE.format(
                self.table_name, ', '.join(table_args))
        connection.execute(table)
        connection.commit()

    def get_update_filter(self, kwargs):
        update_filter = []
        for k, v in kwargs.items():
            if k in self.get_list_fields():
                update_filter = '{}="{}"'.format(k, v)
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
        for k, v in self.arg_dict.items():
            arg = '{}="{}"'.format(k, v)
            update_args.append(arg)
        return update_args

    def delete(self, **kwargs):
        if kwargs:
            delete_filter = self.get_update_filter(kwargs)
            table = sqlines.DELETE_WHERE.format(
                self.table_name, delete_filter)
        else:
            table = sqlines.DELETE.format(self.table_name)
        connection.execute(table)

    @decoratorms.classproperty
    def query(cls):
        query_class = cls.query_class
        return query_class(orm_class=cls)

