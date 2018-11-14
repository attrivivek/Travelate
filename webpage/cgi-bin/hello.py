from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('index.html')

@app.route('/')

def my_form_post():
    if request.method=='POST':
        text = request.form['hotel_query']
        return render_template('index.html', text=text)

app.run(port = 5000)