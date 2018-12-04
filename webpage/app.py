from flask import Flask, request, render_template, jsonify
import analysis
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
        output = analysis.get_results(query)

        html = ""

        for index, row in output.iterrows():
            html = (html  + "<a href='https://www.google.com/search?q=" + row['Hotel.Name'].strip() + "' target='_blank'>" + 
                                "<div class='hotel-row'>" +
                                    "<div class='row'>" +
                                        "<div class='col-sm-6 hotel-name'>" +
                                            "<p class='name-label'>Hotel Name</p>" +
                                            "<p>" + row['Hotel.Name'] + "</p>" +
                                        "</div>" +

                                        "<div class='col-sm-3 hotel-score'>" +
                                            "<p class='score-label'>Average Rating</p>" +
                                            "<p>" + str( row['Average.Score'] ) + "</p>" +
                                        "</div>" +

                                        "<div class='col-sm-3 hotel-review-count'>" +
                                            "<p class='count-label'>Number of Reviews</p>" +
                                            "<p>" + str( row['Total.Reviews'] ) + "</p>" +
                                        "</div>" +

                                        "<div class='col-sm-12 hotel-address'>" +
                                            "<p><span class='address-label'>Address: </span>" + row['Hotel.Address'] + "</p>" +
                                        "</div>" +
                                    "</div>"
                                "</div><hr>" +
                            "</a>")

        return render_template( 'result.html', output = html )