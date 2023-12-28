from flask import Flask, render_template, request, url_for
from scripts import OCR
from PIL import Image   
import pytesseract
import os

app = Flask(__name__, static_url_path='/static')

UPLOAD_FOLDER = os.path.join('static', 'uploads')
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

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

@app.route('/speech_to_text', methods=['GET','POST'])
def speech_to_text():
    return render_template('speech_to_text.html')

@app.route('/convert', methods=['POST'])
def img2txt():
    uploaded_file = request.files['image']
    language = request.form['language']

    if uploaded_file.filename != '':    
        img_path = os.path.join(app.config['UPLOAD_FOLDER'], 'temp_img.png')
        uploaded_file.save(img_path)
        extracted_text = OCR.perform_ocr(img_path, language)
        return render_template('result.html', extracted_text=extracted_text, temp_img=img_path)
    return "No file uploaded"










if __name__ == "__main__":  
    app.run(debug=True)