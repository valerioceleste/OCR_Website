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

@app.route('/image_to_text/convert', methods=['POST'])
def img2txt():
    uploaded_file = request.files['image']
    language = request.form['language']

    if uploaded_file.filename != '':
        # Save the uploaded image temporarily
        img_path = 'temp_img.png'
        uploaded_file.save(img_path)

        # Perform OCR using pytesseract
        # extracted_text = pytesseract.image_to_string(Image.open(img_path), lang=language)

        # # Remove temporary image file
        # os.remove(img_path)

        return render_template('result.html', language=language)
    return "No file uploaded"








if __name__ == "__main__":  
    app.run(debug=True)