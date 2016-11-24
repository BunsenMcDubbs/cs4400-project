from flask import Blueprint, request, url_for, jsonify
import mysql.connector

from app.models import User

api = Blueprint('api', __name__)

@api.route('/')
def home():
    return jsonify(hello='world')

@api.route('/user/new', methods=['POST'])
def create_user():
    print request.form
    print request.form['username'],request.form['email'],request.form['password']
    status = 'ok'
    error = None
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']
    print request.form['username']
    new_user = User(username, password, email)
    print new_user
    try:
        new_user.save()
    except mysql.connector.Error as err:
        status = 'not ok'
        error = err
    return jsonify(status=status, error=error)

@api.route('/auth/login')
def login():
    return jsonify(error='not yet implemented')

@api.route('/auth/logout')
def logout():
    return jsonify(error='not yet implemented')
