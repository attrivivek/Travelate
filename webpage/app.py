from flask import Flask, request, render_template

app = Flask(__name__)

# @app.route('/')
# @app.route('/index')
# def index():
#     text = "Works!"
#     return render_template('index.html', output = text)

@app.route('/')
def index():
   return render_template('index.html')

@app.route('/result', methods = ['POST', 'GET'])
def result():
    if request.method == 'POST':
        result = request.form
        return render_template('result.html', output = result)