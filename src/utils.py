from PIL import Image, ImageGrab
from translate import Translator
import pytesseract
import re

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe' ## TODO: Use docker instead of requiring Tesseract to be installed on the host machine.

def extract_text_from_clipboard(source_lang): ## TODO: Look at first image in multi-clipboard instead of raising an error if the most recent clipboard item is not an image.
    image = ImageGrab.grabclipboard()
    if isinstance(image, Image.Image):
        return pytesseract.image_to_string(image, lang=source_lang)
    else:
        raise ValueError("No image found in clipboard")

def preprocess_text(text): ## TODO: Improve this function after testing against more input types.
    lines = text.split('\n')
    preprocessed_lines = []
    for line in lines:
        line = re.sub(r'\s+', ' ', line)  # Remove extra whitespaces
        line = re.sub(r'[!]', '', line)  # Remove exclamation marks
        line = re.sub(r'\b\d{2}:\d{2}\b', '', line)  # Remove timestamps in the format HH:MM
        line = re.sub(r'\b\d+\b', '', line)  # Remove strings that have only numbers
        line = re.sub(r'[^:]*:', '', line)  # Remove hero names and text before ':'
        line = line.strip()  # Normalize text
        preprocessed_lines.append(line)
    return '\n'.join(preprocessed_lines)

def translate_text(text, source_lang, target_language):
    translator = Translator(from_lang=source_lang, to_lang=target_language)
    translation = translator.translate(text)
    return translation