#!/usr/bin/python3

"""
    ocr.py
    Use pytesseract python wrapper for OCR-tesseract
    Example use with basic configurations
    Accuracy can vary a lot according to image
    and can be improved through pre-processing (eg with cv2)
"""

import pytesseract
import sys
try:
    import Image
except ImportError:
    from PIL import Image


#path to OCR software main directory
path_tessOCR = 'H:\Softwares\TesseractOCR'

# !Tesseract configuration:
# Include the above line, if you don't have tesseract executable in your PATH
# Example tesseract_cmd: 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract'
pytesseract.pytesseract.tesseract_cmd = path_tessOCR +'\\' + 'tesseract'

# Example config: '--tessdata-dir "C:\\Program Files (x86)\\Tesseract-OCR\\tessdata"'
# It's important to add double quotes around the dir path.
#To be done in case problem of like: 'file can t be found'
tessdata_dir_config = '--tessdata-dir "{}\\tessdata"'.format(path_tessOCR)
#it is reported some errors if disk letters of tesseract folder and file are different

#!codec problem ? to enter in the cmd (Windows)
#one solution might be to ignore not utf 8 caracters (obviously erronous ?)
#chcp 65001

if __name__ == "__main__":
    if len(sys.argv) == 2:
        img = sys.argv[1]
        
    else:
        img = 'H:\Pictures\Lorem_Ipsum_Helvetica.png'

    text = pytesseract.image_to_string(Image.open(img),
                                       config=tessdata_dir_config)
    print(text)