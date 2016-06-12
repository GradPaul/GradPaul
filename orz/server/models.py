from . import db
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from mongoengine import *
import datetime
class User(Document):
    # obj_id = ObjectIdField()
    student_id=IntField(required=True)
    password = StringField()
    name = StringField()
    ctime=DateTimeField(default=datetime.datetime.now)

    def verify_password(self, password):
        return self.password == password

    def generate_auth_token(self, expiration=3600):
        s = Serializer('SECRET_KEY',
                       expires_in=expiration)
        return s.dumps({'id': self.student_id}).decode('ascii')

    @staticmethod
    def verify_auth_token(token):
        s = Serializer('SECRET_KEY')
        try:
            data = s.loads(token)
        except:
            return None
        return User.objects(student_id=data['id']).first()


class Teacher(Document):
    # obj_id = ObjectIdField()
    teacher_id=IntField()
    name = StringField()
    title = StringField()
    ctime=DateTimeField(default=datetime.datetime.now)


class Course(Document):
    # obj_id = ObjectIdField()
    course_id=IntField(required=True)
    credit=IntField()
    name = StringField()
    department = StringField()
    teachers = ListField()
    ctime=DateTimeField(default=datetime.datetime.now)

class Comment(Document):
    content_id=IntField(required=True)
    student_id=IntField(required=True)
    course_id=IntField(required=True)
    teacher_id=IntField(required=True)
    content = StringField()
    ctime=DateTimeField(default=datetime.datetime.now)
