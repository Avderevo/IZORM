Python 3.5.2 (default, Nov 23 2017, 16:37:01) 
[GCC 5.4.0 20160609] on linux
Type "copyright", "credits" or "license()" for more information.
>>> class User(Base):
    __tablename__ = 'users'

    name = Column(String(255))
    password = Column(Integer)

    
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    class User(Base):
NameError: name 'Base' is not defined
>>> class Base():

    def __init__(self, *args, **kwargs):

        self.args = args
        self.kwargs = kwargs
    def priner(self):
        arg = [i for i in args]
        print(args)

        
>>> class User(Base):
    __tablename__ = 'users'

    name = Column(String(255))
    password = Column(Integer)

    
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    class User(Base):
  File "<pyshell#5>", line 4, in User
    name = Column(String(255))
NameError: name 'Column' is not defined
>>> class Column:
    def __init__(self, *args):
        self.args = args

        
>>> class User(Base):
    __tablename__ = 'users'

    name = Column(String(255))
    password = Column(Integer)

    
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    class User(Base):
  File "<pyshell#9>", line 4, in User
    name = Column(String(255))
NameError: name 'String' is not defined
>>> class User(Base):
    __tablename__ = 'users'

    name = (String(255))
    password = (Integer)

    
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    class User(Base):
  File "<pyshell#11>", line 4, in User
    name = (String(255))
NameError: name 'String' is not defined
>>> class Column:
	def__init__(self):
		
SyntaxError: invalid syntax
>>> class Column:
	def __init__(self):
		pass

	
>>> class Imteger:
	pass

>>> class String:
	def __init__(self, max_length=255):
	fieldtype = 'varchar({})' .format(max_length)
	
SyntaxError: expected an indented block
>>> class String:
	def __init__(self, max_length=255):
	    fieldtype = 'varchar({})' .format(max_length)

	    
>>> class User(Base):
    __tablename__ = 'users'

    name = (String(255))
    password = (Integer)

    
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    class User(Base):
  File "<pyshell#27>", line 5, in User
    password = (Integer)
NameError: name 'Integer' is not defined
>>> class Integer:
	def __init__(self):
		pass

	
>>> class User(Base):
    __tablename__ = 'users'

    name = (String(255))
    password = (Integer)

    
>>> base = Base()
>>> dir(base)
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'args', 'kwargs', 'priner']
>>> user = User()
>>> user.printer
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    user.printer
AttributeError: 'User' object has no attribute 'printer'
>>> user.printer()
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    user.printer()
AttributeError: 'User' object has no attribute 'printer'
>>> User().printer()
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    User().printer()
AttributeError: 'User' object has no attribute 'printer'
>>> user = User('yura', 1234)
>>> user._
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    user._
AttributeError: 'User' object has no attribute '_'
>>> user.__class__.__dict__
mappingproxy({'__doc__': None, '__tablename__': 'users', '__module__': '__main__', 'password': <class '__main__.Integer'>, 'name': <__main__.String object at 0x7f2fddf9c898>})
>>> user.__class__.__name__
'User'
>>> user.__class__.__tablename__
'users'
>>> user.__class__.name
<__main__.String object at 0x7f2fddf9c898>
>>> d = user.__class__.name
>>> d.__dict__
{}
>>> dir(d)
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']
>>> dir(user.__class__)
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__tablename__', '__weakref__', 'name', 'password', 'priner']
>>> user
<__main__.User object at 0x7f2fdcf242e8>
>>> user.__dict__
{'kwargs': {}, 'args': ('yura', 1234)}
>>> user.dict
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    user.dict
AttributeError: 'User' object has no attribute 'dict'
>>> user.__tablename__
'users'
>>> dir(user)
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__tablename__', '__weakref__', 'args', 'kwargs', 'name', 'password', 'priner']
>>> class User(Base):
    __tablename__ = 'users'

    name = Column(String(255))
    password = Column(Integer)

    
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    class User(Base):
  File "<pyshell#55>", line 4, in User
    name = Column(String(255))
TypeError: __init__() takes 1 positional argument but 2 were given
>>> class Column:
	def __init__(self, *args, *kwargs):
		self.args = args
		self.kwargs = kwargs

		
SyntaxError: invalid syntax
>>> 
>>> class Column:
	def __init__(self, *args, *kwargs):
		self.args = args
		self.kwargs = kwargs
		
SyntaxError: invalid syntax
>>> 
>>> class Column:
	def __init__(self, *args, **kwargs):
		self.args = args
		self.kwargs = kwargs

		
>>> class User(Base):
    __tablename__ = 'users'

    name = Column(String(255))
    password = Column(Integer)

    
>>> user = User('yuraavdeev', 1234567890)
>>> user
<__main__.User object at 0x7f2fdcf24160>
>>> user.__dict__
{'kwargs': {}, 'args': ('yuraavdeev', 1234567890)}
>>> user.__class__
<class '__main__.User'>
>>> user__dict__
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    user__dict__
NameError: name 'user__dict__' is not defined
>>> dir(user)
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__tablename__', '__weakref__', 'args', 'kwargs', 'name', 'password', 'priner']
>>> user.printer()
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    user.printer()
AttributeError: 'User' object has no attribute 'printer'
>>> user.priner()
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    user.priner()
  File "<pyshell#3>", line 8, in priner
    arg = [i for i in args]
NameError: name 'args' is not defined
>>> class Base():

    def __init__(self, *args, **kwargs):

        self.args = args
        self.kwargs = kwargs
    def priner(self):
        arg = [i for i in self.args]
        print(args)

        
>>> user.priner()
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    user.priner()
  File "<pyshell#3>", line 8, in priner
    arg = [i for i in args]
NameError: name 'args' is not defined
>>> class User(Base):
    __tablename__ = 'users'

    name = Column(String(255))
    password = Column(Integer)

    
>>> user = User('yuraavdeev', 1234567890)
>>> user.priner()
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    user.priner()
  File "<pyshell#73>", line 9, in priner
    print(args)
NameError: name 'args' is not defined
>>> class Base():

    def __init__(self, *args, **kwargs):

        self.args = args
        self.kwargs = kwargs
    def priner(self):
        arg = [i for i in self.args]
        print(arg)

        
>>> class User(Base):
    __tablename__ = 'users'

    name = Column(String(255))
    password = Column(Integer)

    
>>> user = User('yuraavdeev', 1234567890)
>>> user.priner()
['yuraavdeev', 1234567890]
>>> user.__
Traceback (most recent call last):
  File "<pyshell#85>", line 1, in <module>
    user.__
AttributeError: 'User' object has no attribute '__'
>>> user.__class__.password
<__main__.Column object at 0x7f2fdcf24c88>
>>> user.__class__
<class '__main__.User'>
>>> dir(user.__class__)
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__tablename__', '__weakref__', 'name', 'password', 'priner']
>>> user.__doc__
>>> user.__hash__
<method-wrapper '__hash__' of User object at 0x7f2fdcf24ac8>
>>> user.__subclasshook__
<built-in method __subclasshook__ of type object at 0x14715d8>
>>> c = <built-in method __subclasshook__ of type object at 0x14715d8>
SyntaxError: invalid syntax
>>> c= user.__subclasshook__
>>> dir(c)
['__call__', '__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__module__', '__name__', '__ne__', '__new__', '__qualname__', '__reduce__', '__reduce_ex__', '__repr__', '__self__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__text_signature__']
>>> c.__class__
<class 'builtin_function_or_method'>
>>> c.__dict__
Traceback (most recent call last):
  File "<pyshell#96>", line 1, in <module>
    c.__dict__
AttributeError: 'builtin_function_or_method' object has no attribute '__dict__'
>>> user.__class__.__dict__
mappingproxy({'__doc__': None, '__tablename__': 'users', '__module__': '__main__', 'password': <__main__.Column object at 0x7f2fdcf24c88>, 'name': <__main__.Column object at 0x7f2fdcf24978>})
>>> class String:
	def __init__(self, max_length=255):
	    self.fieldtype = 'varchar({})' .format(max_length)

	    
>>> class Integer:
	def __init__(self):
		
		self.fieldtype ='integer'

		
>>> Cclass User(Base):
    __tablename__ = 'users'

    name = Integer()
    password = String(max_lengh = 55)
    
SyntaxError: invalid syntax
>>> class User(Base):
    __tablename__ = 'users'

    name = Integer()
    password = String(max_lengh = 55)

    
Traceback (most recent call last):
  File "<pyshell#104>", line 1, in <module>
    class User(Base):
  File "<pyshell#104>", line 5, in User
    password = String(max_lengh = 55)
TypeError: __init__() got an unexpected keyword argument 'max_lengh'
>>> Cclass User(Base):
    __tablename__ = 'users'

    name = Integer()
    password = String(max_length = 55)
    
SyntaxError: invalid syntax
>>> 
>>> Cclass User(Base):
    __tablename__ = 'users'

    name = Integer()
    password = String(max_length = 55)
    
SyntaxError: invalid syntax
>>> class User(Base):
    __tablename__ = 'users'

    name = Integer()
    password = String(max_length = 55)

    
>>> user = User(123456, "urasffffeddwd')
	    
SyntaxError: EOL while scanning string literal
>>> user = User(123456, "urasffffeddwd")
>>> user.__class__.__dict__
mappingproxy({'__doc__': None, '__tablename__': 'users', '__module__': '__main__', 'password': <__main__.String object at 0x7f2fdcf2b160>, 'name': <__main__.Integer object at 0x7f2fdcf24f28>})
>>> user.__dict__
{'kwargs': {}, 'args': (123456, 'urasffffeddwd')}
>>> pas = user.__class__._
Traceback (most recent call last):
  File "<pyshell#114>", line 1, in <module>
    pas = user.__class__._
AttributeError: type object 'User' has no attribute '_'
>>> user.__class__.__class__
<class 'type'>
>>> pa = user.__class__.__dict__['password']
>>> pa
<__main__.String object at 0x7f2fdcf2b160>
>>> dir(pa)
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'fieldtype']
>>> pa.__dict__
{'fieldtype': 'varchar(55)'}
>>> user1 = User()
>>> user1.
SyntaxError: invalid syntax
>>> user1.args
()
>>> user1.__class__.__dict__
mappingproxy({'__doc__': None, '__tablename__': 'users', '__module__': '__main__', 'password': <__main__.String object at 0x7f2fdcf2b160>, 'name': <__main__.Integer object at 0x7f2fdcf24f28>})
>>> user1.__dict__
{'kwargs': {}, 'args': ()}
>>> dir(user1.__class__)
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__tablename__', '__weakref__', 'name', 'password', 'priner']
>>> 
