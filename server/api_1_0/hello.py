# from flask import Blueprint, request, render_template



import requests
from flask import jsonify, request, g, abort, url_for, current_app
from flask.ext import restful
from flask_restful import Api, Resource, url_for
from . import api as api_bp
from ..models import *
from ..utils import *
import json



from flask.ext.restful import reqparse

parser = reqparse.RequestParser()


api = Api(api_bp)




class HelloWorld(restful.Resource):
    def get(self,):
        return {'hello': 'world'}





class teacher_item(restful.Resource):
    def get(self,t_id):
        teacher=Teacher.objects(teacher_id=t_id).first()
        return teacher.to_json()



class teacher_list(restful.Resource):
    def get(self):
        teachers=Teacher.objects()
        return teachers.to_json()

    def post(self):
        teacher_dict=request.json
        try:
            new_teacher=Teacher(teacher_id=teacher_dict['t_id'],\
            name=teacher_dict['name'],title=teacher_dict['title'])
            new_teacher.save()
        except BaseException,e:
            print e

        return jsonify(teacher_dict)



class teacher_item(restful.Resource):
    def get(self,t_id):
        teacher=Teacher.objects(teacher_id=t_id).first()
        return teacher.to_json()



class teacher_list(restful.Resource):
    def get(self):
        teachers=Teacher.objects()
        return teachers.to_json()

    def post(self):
        teacher_dict=request.json
        try:
            new_teacher=Teacher(teacher_id=teacher_dict['t_id'],\
            name=teacher_dict['name'],title=teacher_dict['title'])
            new_teacher.save()
        except BaseException,e:
            print e

        return jsonify(teacher_dict)




class course_item(restful.Resource):
    def get(self,c_id):
        course=Course.objects(course_id=c_id).first()
        return course.to_json()

class course_list(restful.Resource):
    def get(self):
        courses=Course.objects()
        return courses.to_json()

    def post(self):
        course_dict=request.json
        try:
            new_course=Course(course_id=teacher_dict['c_id'],\
            name=teacher_dict['name'],credit=teacher_dict['credit'],\
            department=teacher_dict['department'],teachers=teacher_dict['teachers'])
            new_course.save()
        except BaseException,e:
            print e

        return jsonify(course_dict)




class comment_item(restful.Resource):
    def get(self,c_id):
        comment=Comment.objects(comment_id=c_id).first()
        return comment.to_json()




class comment_list(restful.Resource):
    def get(self):
        comments=Comment.objects()
        return comments.to_json()

    def post(self):
        comment_dict=request.json
        try:
            new_comment=Comment(comment_id=comment_dict['co_id'],\
            teacher_id=comment_dict['t_id'],course_id=comment_dict['c_id'],\
            content=comment_dict['content'])
            new_comment.save()
        except BaseException,e:
            print e

        return jsonify(comment_dict)


class user_item(restful.Resource):
    def get(self,s_id):
        user=User.objects(student_id=s_id).first()
        return user.to_json()

class user_list(restful.Resource):
    def get(self):
        users=User.objects()
        return users.to_json()

    def post(self):
        user_dict=request.json
        try:
            new_user=User(student_id=user_dict['student_id'],\
            password=user_dict['password'],name=user_dict['name'])
            new_user.save()
        except BaseException,e:
            print e

        return jsonify(comment_dict)


api.add_resource(HelloWorld, '/')
api.add_resource(teacher_item, '/teachers/<int:t_id>')
api.add_resource(teacher_list, '/teachers')
api.add_resource(course_item, '/courses/<int:c_id>')
api.add_resource(course_list, '/courses')
api.add_resource(comment_item, '/comments/<int:comment_id>')
api.add_resource(comment_list, '/comments')

api.add_resource(user_item, '/users/<int:s_id>')

api.add_resource(user_list, '/users')

@api_bp.route('/user/signup', methods=['GET', 'POST'])
def signup():
    try:
        user_dict=request.json
        new_user=User(student_id=user_dict['student_id'],\
        password=user_dict['password'],name=user_dict['name'])
        new_user.save()
        return jsonify(success_code)
    except BaseException,e:
        return str(e)

@api_bp.route('/user/login', methods=['GET', 'POST'])
def login():
    try:
        user_dict=request.json
        s_id=user_dict['student_id']
        password=user_dict['password']
        user=User.objects(student_id=s_id).first()
        if user.verify_password(password):
            reply=success_code
            reply['access_token']=user.generate_auth_token()
            return jsonify(reply)
        else:
            return jsonify(wrong_pass_code)
    except BaseException,e:
        return jsonify(wrong_pass_code)
