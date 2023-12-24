from flask import Flask, render_template, request, url_for
import pytesseract
from PIL import Image

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', active_page = 'index')

@app.route('/about')
def about():
    return render_template('about.html', active_page = 'about')

if __name__ == "__main__":
    app.run(debug=True)