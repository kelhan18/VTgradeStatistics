from flask import Flask
from flask import render_template
import pandas as pd

app = Flask(__name__, static_url_path='')

@app.route('/')
def show_main():

    return render_template('index.html')

@app.route('/cs')

def show_cs():

    return render_template('cs.html')

@app.route('/contact')
def show_contact():

    return render_template('contact.html')

@app.route('/ece')
def show_cpe():
    return render_template('ece.html')

@app.route('/aero')
def show_aero():
    return render_template('aero.html')

@app.route('/math')
def show_math():
    return render_template('math.html')

@app.route('/bit')
def show_bit():
    return render_template('bit.html')

@app.route('/finance')
def show_finance():
    return render_template('finance.html')

@app.route('/accounting')
def show_accounting():
    return render_template('acis.html')

if __name__ == "__main__":
    app.run(debug=True, port=5050)
