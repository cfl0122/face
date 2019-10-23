import base64
import numpy as np
import json
import pickle
import time
import os
from flask import Flask,abort
from sqlalchemy.dialects.mssql import TIMESTAMP
#
# from flask_sqlalchemy import SQLAlchemy
# a=np.linspace(0,99,100).reshape(5,20)
# print(a)
# from flask import Flask
# app=Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///e:/user/bzl.db'
# db=SQLAlchemy(app)
#
#
# class Role(db.Model):
#     __tablename__ = "roles"
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(64), unique=True)
#
#     def __repr__(self):
#         """非必须, 用于在调试或测试时, 返回一个具有可读性的字符串表示模型."""
#         return '<Role %r>' % self.name
#
# class User(db.Model):
#     __tablename__ = 'users'
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(64), unique=True, index=True)
#
#     def __repr__(self):
#         """非必须, 用于在调试或测试时, 返回一个具有可读性的字符串表示模型."""
#         return '<Role %r>' % self.username
#
#
# db.create_all()


a=2530071209
b=time.localtime(a)




print(b)



