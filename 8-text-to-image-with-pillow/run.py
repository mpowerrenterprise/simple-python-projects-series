import csv
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

with open("data.csv", 'r') as csvfile:
	data_reader = csv.reader(csvfile)
	for row in data_reader:

		img = Image.new("RGB", (650, 500), color="white")

		font = ImageFont.truetype("open-sans-regular.ttf",20)

		draw = ImageDraw.Draw(img)

		draw.text((20,20), f'01) First Name     =     {row[0]}', (0,0,0), font=font)

		draw.text((20,80), f'02) Last Name     =     {row[1]}', (0,0,0), font=font)

		draw.text((20,140), f'03) Age     =     {row[2]}', (0,0,0), font=font)

		draw.text((20,200), f'04) Designation     =     {row[3]}', (0,0,0), font=font)

		img.save(f"outputs/{row[0]}{row[1]}.png")


