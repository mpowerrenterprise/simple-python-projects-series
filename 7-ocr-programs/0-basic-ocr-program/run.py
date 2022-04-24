from PIL import Image
import pytesseract

text = pytesseract.image_to_string(Image.open("test-image.png"))

print(text)