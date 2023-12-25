from flask import Flask, render_template, request, url_for
from PIL import Image
import pytesseract
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', active_page = 'index')

@app.route('/solutions')
def solutions():
    return render_template('solutions.html', active_page = 'solutions')

@app.route('/about')
def about():
    return render_template('about.html', active_page = 'about')

@app.route('/image_to_text', methods=['GET','POST'])
def image_to_text():
    return render_template('image_to_text.html')


if __name__ == "__main__":  
    app.run(debug=True)