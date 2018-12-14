from flask import Flask, request, render_template, jsonify
import analysis
import csv
import json
import pandas as pd 

app = Flask(__name__)

COUNTRIES = ["netherlands", "austria", "france", "italy", "kingdom", "spain"]

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/result', methods=['POST', 'GET'])
def result():
    if request.method == 'POST':
        pd.options.display.max_colwidth = 1000

        query = request.form['hotel_query']

        html = ''

        if any( s in query.lower() for s in COUNTRIES ):
            output = analysis.get_results(query)

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
                                                "<p>" + str( round(row['Average.Score'], 2) ) + "</p>" +
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
        else:
            html = '<p style="text-align: center;">Please use one of the listed country names in your query: Netherlands, Austria, France, Italy, Kingdom (United Kingdom), or Spain</p>'

        return render_template( 'result.html', output = html )