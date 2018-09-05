from base import Base
from fields import String, Integer, ForeignKey
from dbconfig import connection


class User(Base):
    id = Integer(primary_key=True)
    name = String(nulable=False)
    fullname = String()
    password = Integer(nulable=False)


class Post(Base):
    id = Integer(primary_key=True)
    title = String(nulable=False)
    user_id = ForeignKey('user')




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


def table2(post):
    post.create()
    p1 = Post(title='python', user_id='1')
    p2 = Post(title='kotiki', user_id='2')
    p3 = Post(title='elka', user_id='3')
    p4 = Post(title='zayki', user_id='4')
  


    user_list = [p1, p2, p3, p4]
    for user in user_list:
        user.save()
    return post
