from app import app
from flask import render_template, flash, redirect

dishes={}
ingredients=[]

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])

def index():
    return render_template('index.html')