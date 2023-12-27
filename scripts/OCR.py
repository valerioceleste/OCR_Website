from PIL import Image
import pytesseract

def perform_ocr(image_path, language):
    try:
        img = Image.open(image_path)
        text = pytesseract.image_to_string(img, lang=language)
        return text
    
    except Exception as e:
        return str(e)