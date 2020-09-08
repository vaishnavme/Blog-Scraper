import os, sys
# file structure import
from os.path import dirname, join, abspath
sys.path.insert(0, abspath(join(dirname(__file__),'..')))

# flask
from flask import Flask, render_template

# API calls
from api.analyticDS import analyticData
from api.webMarkiting import webMark
from api.webdev import webio




app = Flask(__name__)


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', title = 'Home')

@app.route("/about")
def about():
    return render_template('about.html', title ='About')

@app.route('/avds')
def data_science():
    data = analyticData()
    return render_template('datascience.html',data=data)

@app.route('/webm')
def web_markiting():
    data = webMark()
    return render_template('webmarketing.html',data=data)

@app.route('/desio')
def web_design():
    data = webio()
    return render_template('webdev.html',data=data)

if __name__ == '__main__':
    app.run(debug=True)