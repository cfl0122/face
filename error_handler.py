
from flask import Blueprint, render_template, redirect,session,request,abort
exception = Blueprint('exception',__name__)
@exception.app_errorhandler(404)
def error(e):
    resp =''
    return resp
