from flask import Flask, request, render_template
import hello

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
        output = hello.test_func(request.form)
        return render_template('result.html', output = output)