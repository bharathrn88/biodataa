from flask import Flask, render_template, request, redirect, jsonify, url_for
from utils.db import db
from models.resume import *

flask_app = Flask(__name__)
flask_app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///RESUME.db'
flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True


@flask_app.route('/')
def index():
    return render_template('index.html')


@flask_app.route('/login')
def login():
    login = Login.query.all()
    return render_template('login.html', content=login)


@flask_app.route('/logout')
def logout():
    return render_template('logout.html')


@flask_app.route('/resume')
def resume():
    return render_template('resume.html')


db.init_app(flask_app)
with flask_app.app_context():
    db.create_all()


@flask_app.route('/sub', methods=['POST'])
def sub():
    form_data = request.form.to_dict()
    print(f"form_data: {form_data}")
    email = form_data.get('email')
    password = form_data.get('password')
    login = Login(email=email, password=password)
    db.session.add(login)
    db.session.commit()
    print("submitted successfully")
    return redirect('/resume')





@flask_app.route('/subm', methods=['POST'])
def subm():
    form_data = request.form.to_dict()
    print(f"form_data: {form_data}")
    register_name = form_data.get('register_name')
    register_email = form_data.get('register_email')
    register_password = form_data.get('register_password')
    register = Register(name=register_name, email=register_email, password=register_password)
    db.session.add(register)
    db.session.commit()
    print("submitted successfully")
    return redirect('/login')


if __name__ == ' __main__ ':
    flask_app.run(
        host='127.0.0.1',
        port=8005,
        debug=True
    )