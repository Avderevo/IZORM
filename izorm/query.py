from dbconfig import connection
from exception import QueryFieldException, EmptyArgsException
import sqlines
from sqlite3 import OperationalError
import logging
logging.basicConfig(format=u' %(message)s', level=logging.INFO)


class Query:

    '''
    The query class for querying our database.
    All methods of the class are written after the "query" instance.
    For example: User.query.filter(name='some name').
    '''

    def __init__(self, orm_class=None, *args, **kwargs):

        self.orm_class = orm_class
        self.args = args
        self.kwargs = kwargs
        self.table_name = orm_class.__name__

    def model_field(self):
        model_field_dict = {}
        for k, v in dict(self.orm_class.__dict__).items():
            if not k.startswith('__'):
                v = [i for i in v.__dict__['sqlite_type'].split()][0]
                model_field_dict[k] = v
        return model_field_dict

    def all(self):
        select_all = sqlines.ALL.format(self.table_name)
        q_all = connection.execute(select_all)
        return q_all.fetchall()

    def order_by(self, order_arg):
        field_list = self.field_parse()
        select = sqlines.ORDER_BY.format(
            field_list, self.table_name, str(order_arg))
        select = connection.execute(select)
        return select.fetchall()

    def order_by_desc(self, order_arg):
        field_list = self.field_parse()
        select = sqlines.ORDER_BY_DESC.format(
            field_list, self.table_name, str(order_arg))
        select = connection.execute(select)
        return select.fetchall()

    def order_by_asc(self, order_arg):
        field_list = self.field_parse()
        select = sqlines.ORDER_BY_ASC.format(
            field_list, self.table_name, str(order_arg))
        select = connection.execute(select)
        return select.fetchall()

    def get_field_list(self, field):
        field_list = None
        if len(field):
            field_list = [str(i) for i in field]
            for fild in field_list:
                if fild not in self.model_field().keys():
                    logging.info(
                        'Поле "{}" отсутствует в модели!'.format(fild))
                    raise QueryFieldException(
                        'The model does not have the indicated sorting field "{}"'.format(fild))
        return field_list

    def field(self, *field):
        fields = self.get_field_list(field)
        self.args = fields
        return self

    def field_parse(self):
        fields = dict(self.__dict__)['args']
        fields = ', '.join(fields) if fields else '*'
        return fields

    def filter(self, **kwargs):
        filter_args = self.get_filter_args(kwargs)
        if not filter_args:
            logging.info('Нет аргументов для фильтра!')
            raise EmptyArgsException('Missing required arguments!')
        field_list = self.field_parse()
        select = sqlines.FILTER.format(
            field_list, self.table_name, ' AND '.join(filter_args))
        try:
            select = connection.execute(select)
            return select.fetchone()
        except OperationalError as o:
            logging.info(o)

    def get_filter_args(self, kwargs):
        filter_args = []
        for k, v in kwargs.items():
            filt_arg = '{}="{}"'.format(k, v)
            filter_args.append(filt_arg)
        return filter_args

    def between(self, *args):
        try:
            b_args = self.get_between_ars(args)
            field_list = self.field_parse()
            select = sqlines.BETWEEN.format(
                field_list, self.table_name, b_args[0],
                ' AND '.join(b_args[1:]))
            try:
                select = connection.execute(select)
                return select.fetchall()
            except KeyError as k:
                logging.info(k)
        except TypeError:
            logging.info(
                'Недопустимый тип аргументов!')

    def get_between_ars(self, args):
        b_args = [i for i in args]
        if len(b_args) != 3:
            logging.info('Не допустимое колличество аргументов! Необходимо 3 аргумента.')
            raise QueryFieldException('Invalid number of arguments!')
        return self.btw_arg_match(b_args)

    def btw_arg_match(self, b_args):
        field = b_args[0]
        if not field in self.model_field().keys() or self.model_field()[field].lower() != 'integer':
            logging.info(
                'Недопустимый тип аргументов! Поле сортировки должно быть INTEGER.')
            raise QueryFieldException('The sort field must be INTEGER!')
        return b_args
