import pymongo
from flask import redirect,render_template, request, url_for

from my_app import app
from my_app.blog.models import TODOS
from my_app.blog.models import PasswordHelper
from my_app.blog.models import DBHelper

DB = DBHelper()
PH = PasswordHelper()


@app.route('/')
def index():
    return render_template('index.html')
@app.route('/home')

def home():
    return render_template('home.html', todos=TODOS)

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/register', methods=['POST'])
def register():
    email = request.form.get("Email")
    password = request.form.get("Password")
    if DB.get_user(email):
        return render_template('signup.html', onloadmessage="Email Already Registered.")
    password = str(password).encode('utf-8')
    salt = PH.get_salt()
    salt = str(salt).encode('utf-8')
    hashed = PH.get_hash(password + salt)
    DB.create_user(email, salt, hashed)
    return render_template('signup.html', onloadmessage="Registration success. Please login.")

@app.route('/login-page')
def login-page():
    return render_template('login-page.html')

@app.route('/login', methods=['POST'])
def login():
    email = request.form.get("Email")
    password = request.form.get("Password")
    if DB.get_user(email):
        redirect(url_for('home.html'))
    else:
        return render_template('login-page.html', onloadmessage="Incorrect Login Information")


@app.route('/add')
def add():
    return render_template('add.html', todos=TODOS)

@app.route('/submit', methods=['POST'])

def submit():
    for k,v in TODOS.items():
        TODOS[k] = request.form.get(k)
    return render_template('home.html', todos=TODOS)
