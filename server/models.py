from . import db
from mongoengine import *
import datetime
class User(Document):
    # obj_id = ObjectIdField()
    student_id=IntField(required=True)
    password = StringField()
    name = StringField()
    ctime=DateTimeField(default=datetime.datetime.now)

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
    # obj_id = ObjectIdField()
    student_id=IntField(required=True)
    course_id=IntField(required=True)
    teacher_id=IntField(required=True)
    content = StringField()
    ctime=DateTimeField(default=datetime.datetime.now)
