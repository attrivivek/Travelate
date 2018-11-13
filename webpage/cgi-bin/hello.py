from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('index.html')

@app.route('/', methods=['GET'])
def my_form_post():
    text = request.form['hotel_query']
    processed_text = text.upper()
    return processed_text

app.run(port = 5000)