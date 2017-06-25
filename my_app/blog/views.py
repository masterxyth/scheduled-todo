from flask import render_template, request
from my_app import app
from my_app.blog.models import TODOS

@app.route('/')
@app.route('/home')

def home():
    return render_template('home.html', todos=TODOS)

@app.route('/add')
def add():
    return render_template('add.html', todos=TODOS)

@app.route('/submit', methods=['POST'])

def submit():
    TODOS['8:00AM - 9:00AM'] = request.form.get('8:00AM - 9:00AM')
    TODOS['9:00AM - 10:00AM'] = request.form.get('9:00AM - 10:00AM')
    TODOS['10:00AM - 11:00AM'] = request.form.get('10:00AM - 11:00AM')
    TODOS['11:00AM - 12:00PM'] = request.form.get('11:00AM - 12:00PM')
    TODOS['12:00PM - 1:00PM'] = request.form.get('12:00PM - 1:00PM')
    TODOS['1:00PM - 2:00PM'] = request.form.get('1:00PM - 2:00PM')
    TODOS['2:00PM - 3:00PM'] = request.form.get('2:00PM - 3:00PM')
    TODOS['3:00PM - 4:00PM'] = request.form.get('3:00PM - 4:00PM')
    TODOS['4:00PM - 5:00PM'] = request.form.get('4:00PM - 5:00PM')
    TODOS['5:00PM - 6:00PM'] = request.form.get('5:00PM - 6:00PM')
    TODOS['6:00PM - 7:00PM'] = request.form.get('6:00PM - 7:00PM')
    TODOS['7:00PM - 8:00PM'] = request.form.get('7:00PM - 8:00PM')
    TODOS['8:00PM - 9:00PM'] = request.form.get('8:00PM - 9:00PM')
    TODOS['9:00PM - 10:00PM'] = request.form.get('9:00PM - 10:00PM')
    TODOS['10:00PM - 11:00PM'] = request.form.get('10:00PM - 11:00PM')
    return render_template('home.html', todos=TODOS)
