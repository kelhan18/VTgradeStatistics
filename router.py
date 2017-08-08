from flask import Flask
from flask import render_template
import pandas as pd

app = Flask(__name__, static_url_path='')

@app.route('/')
def show_home():
    return render_template('stats.html')
@app.route('/stats.html')
def show_main():

    return render_template('stats.html')

@app.route('/cs.html')

def show_cs():

    return render_template('cs.html')

@app.route('/contact.html')
def show_contact():

    return render_template('contact.html')

@app.route('/ece.html')
def show_cpe():
    return render_template('/ece.html')

@app.route('/aero.html')
def show_aero():
    return render_template('aero.html')

@app.route('/math.html')
def show_math():
    return render_template('math.html')

@app.route('/bit.html')
def show_bit():
    return render_template('bit.html')

@app.route('/finance.html')
def show_finance():
    return render_template('finance.html')

@app.route('/acis.html')
def show_accounting():
    return render_template('acis.html')

@app.route('/album.html')
def show_album():
    return render_template('album.html')

if __name__ == "__main__":
    app.run(debug=True, port=5050)
