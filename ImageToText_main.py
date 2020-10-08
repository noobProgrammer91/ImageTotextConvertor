
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





