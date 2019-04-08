#these are imports of imaging libraries to manipulate check image
from PIL import Image, ImageDraw

#C = Transit Symbol4.2
#P = On Us Symbol 
#/ = amount symbol
#- = dash symbol
# DPI always 200 for best binarized image
# pixels / dpi = inches
# inches * dpi = pixels
#4.250'' * 200 dpi = 850 pixels - end of routing field delimeter
#5.750'' * 200dpi = 1150 pixels - start of routing field delimeter
#4.250'' * 200 dpi = 850 pixels - start of on us field delimeter
# 1.875'' * 200dpi = 375 pixels - end of on us field delimeter

def drawLines(linePos, img):
	#open new imagedraw library for image manipulate on img variable passed to method
	draw = ImageDraw.Draw(img)
	#Parameters for Drawline
	#(xy coordninates of start, xy coordinates of end), ink, width
	#PIL.ImageDraw.ImageDraw.line(xy, fill=None, width=0, joint=None)
	#draw.line((linePos, 0,linePos,img.height),fill='blue',width=5)
	draw.line((linePos, 0,linePos,img.height),(0),width=1)

#this is a sample check image this needs to be in the same folder as this script
frontCheckImg = 'custtest.tiff'
#frontCheckImg = 'mdtestimg.tiff'
# assign image to new variable for manipulation


#open image and print some image details
img = Image.open(frontCheckImg)
new_img = img
print("Format of image = " + img.format + "\nMode of Image = " + img.mode + "\nDPI = ")
print(img.info['dpi'])

# (0,0) coordinate in imagedraw begins in top left corner of image. since ansi x9 standards place amount status delimeters from right edge of check, we subtract the difference of the standars from the width of the check to get the appropriate placement of our delimeter

#create delimeters in different locationd depending on size of check


#if (img.width > business check) # check if business check 
routingFieldDelStart = img.width - 1150 
routingFieldDelEnd = img.width - 850 
onUsFieldDelStart = img.width - 850
onUSFieldDelEnd = img.width - 375
	#drawLines(routingFieldDelStart,new_img)
	#drawLines(routingFieldDelEnd,new_img)
	#if (img.width>8.750'')
	#print(check is out of spec too wide)
#
#

#if (img.width = personal check) # default to personal as md classifies smallers business checks as personal
	#whatever logic for personal check
	#routingFieldDelStart = img.width - 505 #this 35 will be from ansi standards
	#routingFieldDelEnd = img.width - 1005 #this 55 is also a sample  size in pixels
	#drawLines(routingFieldDelStart,new_img)
	#drawLines(routingFieldDelEnd,new_img)

drawLines(routingFieldDelStart,new_img)
drawLines(routingFieldDelEnd,new_img)
drawLines(onUSFieldDelEnd, new_img)
drawLines(onUsFieldDelStart, new_img)
#show the image with default os imageviewer
new_img.show()
#save the new image to jpeg called DrawnOn
new_img.save('DrawnOn.jpeg' ,'jpeg')

	

