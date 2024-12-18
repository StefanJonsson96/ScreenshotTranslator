##### How to use

#### 1 Download and install Tesseract OCR:

- Download the Tesseract installer from this link: https://github.com/UB-Mannheim/tesseract/wiki
- Run the installer and follow the installation instructions.
- Add Tesseract to your system's PATH:

Optional: Add more language support for Tesseract
- Git clone https://github.com/tesseract-ocr/tessdata
- Take for example rus.traineddata file and paste it in C:\Program Files\Tesseract-OCR\tessdata

##### 2 pip Install Python libraries:
```sh
pip install Pillow pytesseract translate Pillow pytesseract requests translate
``` 

##### 3 Screenshot what you need to translate

##### 3 Run in terminal 
```sh
cd ..\repos\ScreenshotTranslator\src
python main.py
```
### Example: Input: 
![Example Input](/ScreenshotTranslator\exampleInput.png) 

My scripts Output:
Translated Text: Z
156.79
You, are you fine with that
Chat
But if everything works out for you, then for the rest of your life you will fulfill all your dreams.
You're an eyesore

![Google Translate Output](/ScreenshotTranslator/google_translate_output.png)

It seems like Google Translate and the python library has issues with different lines, and neither approach is fool-proof.