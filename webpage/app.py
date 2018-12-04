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

        html = ""

        for index, row in output.iterrows():
            html = (html  + "<div class='hotel-row'>" +
                                "<div class='row result-labels'>" +
                                    "<div class='col-sm-6 name-label'>Hotel Name</div>" +
                                    "<div class='col-sm-3 score-label'>Average Rating</div>" +
                                    "<div class='col-sm-3 count-label'>Number of Reviews</div>" +
                                "</div>" +

                                "<div class='row hotel-row'>" +
                                    "<div class='col-sm-6 hotel-name'>" +
                                        "<p>" + row['Hotel.Name'] + "</p>" +
                                    "</div>" +

                                    "<div class='col-sm-3 hotel-score'>" +
                                        "<p>" + str( row['Average.Score'] ) + "</p>" +
                                    "</div>" +

                                    "<div class='col-sm-3 hotel-review-count'>" +
                                        "<p>" + str( row['Total.Reviews'] ) + "</p>" +
                                    "</div>" +

                                    "<div class='col-sm-12 hotel-address'>" +
                                        "<p><span class='address-label'>Address: </span>" + row['Hotel.Address'] + "</p>" +
                                    "</div>" +
                                "</div>"
                            "</div><hr>")

        return render_template( 'result.html', output = html )