# Python Image to Text Covertor v.1.1.0

This program is going to scan an image for any type of text present in it. We can then collect the extracted text and save in a text file. Both JPEG and png files are supoprted.

## Installation

You will need two modules for the program to work.
1. Pytesseract
2. Pillow

You also have to download an executable file called tesseract.exe and install it in your machine. Here is the link:

[https://github.com/UB-Mannheim/tesseract/wiki]()

## Installing the modules

```bash
pip install pytesseract
pip install pillow
```

## Usage

```python

#Importing the modules
import pytesseract
from PIL import Image

#We have to include the installation path of tesseract.exe file
pytesseract.pytesseract.tesseract_cmd =r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

#This will read the image file
img = Image.open('C:\\Users\\KharabNaHona\\Desktop\\test.png')

#The text will be extracted and stored
text = pytesseract.image_to_string(img)

#Opening a text file in write mode
file =open('C:\\Users\\KharabNaHona\\Desktop\\1234.txt','w')

#Passing the value of the variable 'text' that contains the extracted text
file.write(text)

#It is always a good practice to close a file after opening it.
file.close()
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
