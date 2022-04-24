import os
from PIL import Image
import pytesseract


for filename in os.listdir('input/'):

	text = pytesseract.image_to_string(Image.open(f"input/{filename}"))

	file = open(f"output/{filename}.txt","w")
	file.writelines(text)
	file.close()
