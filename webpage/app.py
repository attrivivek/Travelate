from flask import Flask, request, render_template, jsonify
import hello
import csv
import json
import pandas as pd 

app = Flask(__name__)

# @app.route('/')
# @app.route('/index')
# def index():
#     text = "Works!"
#     return render_template('index.html', output = text)

# This is the initial application the local server runs
@app.route('/')
def index():
   return render_template('index.html')

@app.route('/result', methods = ['POST', 'GET'])
def result():
    if request.method == 'POST':
        pd.options.display.max_colwidth = 1000
        # This variable is not used but kept for archival purposes for now
        data = pd.read_csv('../data/hotels_3.csv')

        # Update this to replicate a query being submitted by the user
        query  = "Hotels in the Netherlands with Great Bedrooms"
        output = hello.test_func(query)

        return render_template('result.html', output = output.to_html(escape = False))