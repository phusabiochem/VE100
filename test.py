from PIL import ImageTk, Image, ImageDraw, ImageFont

MODE_CHECK = 26

fr_coordinate = open('/home/pi/VE100/coordinates.txt')
x_coordinate_17 = int(fr_coordinate.readline())
x_coordinate_26 = int(fr_coordinate.readline().strip('\n'))
y_coordinate = int(fr_coordinate.readline().strip('\n'))

edit_img = Image.open('/home/pi/Desktop/26.png')
img = ImageDraw.Draw(edit_img)
shape = [(1024, 768), (0,550)]
img.rectangle(shape, fill ="lightgray", outline="lightgray")
img_font_1 = ImageFont.truetype("/home/pi/VE100/arial.ttf", 15)
img_font_2 = ImageFont.truetype("/home/pi/VE100/arial.ttf", 23)

if (MODE_CHECK == 17):
	x_coordinate = x_coordinate_17
	for i in range(0,9):
		img.text((x_coordinate,y_coordinate), str(i+1), font=img_font_1, fill=(0,255,0))
		x_coordinate += 49

	x_coordinate = x_coordinate - 49 + 67
	for i in range(9,18):
		img.text((x_coordinate,y_coordinate), str(i+1), font=img_font_1, fill=(0,255,0))
		# ~ if(i<18):
			# ~ x_coordinate += 26
		# ~ elif(i==18):
			# ~ x_coordinate += 30
		# ~ else:
		x_coordinate += 49
else:
	x_coordinate = x_coordinate_26
	for i in range(0,13):
		img.text((x_coordinate,y_coordinate), str(i+1), font=img_font_1, fill=(0,255,0))
		x_coordinate += 32

	x_coordinate = x_coordinate -32 + 77
	for i in range(13,26):
		img.text((x_coordinate,y_coordinate), str(i+1), font=img_font_1, fill=(0,255,0))
		# ~ if(i<18):
			# ~ x_coordinate += 26
		# ~ elif(i==18):
			# ~ x_coordinate += 30
		# ~ else:
		x_coordinate += 32
	
edit_img.save('/home/pi/Desktop/edit_img.png','png')
