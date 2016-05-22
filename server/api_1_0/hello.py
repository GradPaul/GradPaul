# from flask import Blueprint, request, render_template



import requests
from flask import jsonify, request, g, abort, url_for, current_app
from flask.ext import restful
from flask_restful import Api, Resource, url_for
from . import api as api_bp
from ..models import *
import json

# from flask.views import MethodView



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


api.add_resource(HelloWorld, '/')
api.add_resource(teacher_item, '/teachers/<int:t_id>')
api.add_resource(teacher_list, '/teachers')
api.add_resource(course_item, '/courses/<int:c_id>')
api.add_resource(course_list, '/courses')
