# IZORM

Simple SQLite orm for Python

## Installation

Create a new directory and clone the application.

```
$ git clone https://github.com/Avderevo/IZORM
```

## Use


Launch the python to start:

```
$ python3
```


## 1  Configure database

To configure the database import dbconfig

```
from isorm.dbconfig import connection
connection.connect('example.db')
```
if you start the connection without arguments, it will be connected __": memory:"__


## 2  Creating a Model

import the base class and classes for model fields

```
from izorm.base import Base
from izorm.fields import String, Integer, ForeignKey
```

create a class for the model User:

```
class User(Base):
    id = Integer(primary_key=True)
    name = String(nulable=False)
    fullname = String(nulable=False)
    age = Integer(nulable=True)
```
## 3  Creating a table in the database

```
user = User()
user.create()
```
## 4  Saving data to a table

```
u1 = User(name='', fullname='', age='32')
u1.save()

u2 = User(name='', fullname='', age='15')
u2.save()

u3 = User(name='', fullname='', age='45')
u3.save()
```
## 5  Querying data from a table

```
User.query.all()

User.query.filter(name='')

User.query.filed('name', 'fullname').order_by('age')

User.query.filed('name', 'fullname').order_by_desc('age')

User.query.between('age', '15', '32')

User.query.field('fullname').between('id', '1', '3')

User.query.field('fullname').filter(id='3')
```

## 6  Update

```
user = User(name='', fullname='', age='27')
user.update(id='3')
```
**_if   ``user.update()``   will be without arguments then all fields of the table will be updated_**

## 7  Delete

Delete the specified fields:
```
user = User()
user.delete(id='2')
```

Deleting all fields:

```
user = User()
user.delete()
'''





    
