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
    for k,v in TODOS.items():
        TODOS[k] = request.form.get(k)
    return render_template('home.html', todos=TODOS)
