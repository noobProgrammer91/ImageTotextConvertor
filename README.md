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
MIT License

Copyright (c) 2020 Swastik Sarkar

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
