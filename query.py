from dbconfig import connection

import logging
logging.basicConfig(format=u' %(message)s', level=logging.INFO)


class Query:
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
        select_all = '''SELECT * FROM {}'''.format(self.table_name)
        q_all = connection.execute(select_all)
        return q_all.fetchall()


    def order_by(self, order_arg):
        field_list = self.field_parse()
        select = '''SELECT {} FROM {} ORDER BY {}'''.format(
            field_list, self.table_name, str(order_arg))
        select = connection.execute(select)
        return select.fetchall()

    def order_by_desc(self, order_arg):
        field_list = self.field_parse()
        select = '''SELECT {} FROM {} ORDER BY {} DESC'''.format(
            field_list, self.table_name, str(order_arg))
        select = connection.execute(select)
        return select.fetchall()

    def order_by_asc(self, order_arg):
        field_list = self.field_parse()
        select = '''SELECT {} FROM {} ORDER BY {} ASC'''.format(
            field_list, self.table_name, str(order_arg))
        select = connection.execute(select)
        return select.fetchall()

    def get_field_list(self, field):
        if len(field) > 0:
            field_list = [str(i) for i in field]
            for fild in field_list:
                if fild not in self.model_field().keys():
                    logging.info('Не допустимые аргументы поля field!')
                    break
        else:
            field_list = None
        return field_list

    def field(self, *field):
        fields = self.get_field_list(field)
        self.args = fields
        return self

    def field_parse(self):
        field_list = dict(self.__dict__)['args']
        if not field_list:
            field_list = '*'
        else:
            if len(field_list) > 1:
                field_list = ', '.join(field_list)
            else:
                field_list = field_list[0]
        self.args = ()
        return field_list

    def filter(self, **kwargs):
        filter_args = self.get_filter_args(kwargs)
        field_list = self.field_parse()
        select = '''SELECT {} FROM {} WHERE {}'''.format(
            field_list, self.table_name, ' AND '.join(filter_args))
        select = connection.execute(select)
        return select.fetchone()

    def get_filter_args(self, kwargs):
        filter_args = []
        for k, v in kwargs.items():
            filter_args.append(k + '=' + '"' + v  + '"' )
        return filter_args

    def between(self, *args):
        try:
            b_args = self.get_between_ars(args)
            field_list = self.field_parse()
            select = '''SELECT {} FROM {} WHERE {} BETWEEN {}'''.format(
                        field_list, self.table_name, b_args[0],
                         ' AND '.join(b_args[1:]))
            select = connection.execute(select)
            return select.fetchall()
            
        except TypeError:
            pass
        

    def get_between_ars(self, args):
        b_args = [i for i in args]
        if len(b_args) != 3:
            logging.info('Не допустимое колличество аргументов! Необходимо 3.')
        else:
            return self.btw_arg_match(b_args)

    def btw_arg_match(self, b_args):
        field = b_args[0]
        if field in self.model_field().keys() and self.model_field()[field].lower() == 'integer':
            return b_args
        else:
            logging.info('Недопустимый тип аргументов! Поле сортировки должно быть INTEGER.')



