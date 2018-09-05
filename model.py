from base import Base
from fields import String, Integer, ForeignKey
from dbconfig import connection


class User(Base):
    id = Integer(primary_key=True)
    name = String(nulable=False)
    fullname = String()
    password = Integer(nulable=False)


def table(user):

    connection.connect()
    user.create()
    u1 = User(name='yura', fullname='avdeev', password='100')
    u2 = User(name='kot', fullname='matroskin', password='200')
    u3 = User(name='ded', fullname='moroz', password='300')
    u4 = User(name='ded', fullname='mozay', password='400')

    user_list = [u1, u2, u3, u4]
    for user in user_list:
        user.save()
    return user




'''

class Post(Base):

    name = String(nulable=True)
    password = Integer(nulable=False)


if __name__ == "__main__":
    engine = create_engine(":memory:")
    c = engine.cursor()
    User().create_table(c)

    user = User("yura", "avdeev", "123")

    user.table_add(c)


'''