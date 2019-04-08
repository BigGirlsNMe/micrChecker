#these are imports of imaging libraries to manipulate check image
from PIL import Image, ImageDraw

#C = Transit Symbol
#P = On Us Symbol 
#/ = amount symbol
#- = dash symbol



def drawLines(linePos, img):
	#open new imagedraw library for image manipulate on img variable passed to method
	draw = ImageDraw.Draw(img)
	#Parameters for Drawline
	#(xy coordninates of start, xy coordinates of end), ink, width
	#PIL.ImageDraw.ImageDraw.line(xy, fill=None, width=0, joint=None)
	#draw.line((linePos, 0,linePos,img.height),fill='blue',width=5)
	draw.line((linePos, 0,linePos,img.height),(0),width=1)

#this is a sample check image this needs to be in the same folder as this script
frontCheckImg = '149e1354-7a75-48ef-82e1-412759516e4b.FrontImage.BestBinarized.48f9e6ba-fa3f-49c3-9bfe-2ba360b62a02.tiff'
# assign image to new variable for manipulation


#this is a testing image
#frontCheckImg = 'purp.jpeg'

#open image	and print some image details
img = Image.open(frontCheckImg)
new_img = img
print("Format of image = " + img.format + "\nMode of Image = " + img.mode)

# (0,0) coordinate in imagedraw begins in top left corner of image. since ansi x9 standards place amount status delimeters from right edge of check, we subtract the difference of the standars from the width of the check to get the appropriate placement of our delimeter

#TODO
#create delimeters in different locationd depending on size of check
#if (img.width > business check) # check if business check 
amountStatusDelStart = img.width - 505 #this 35 will be from ansi standards
amountStatusDelEnd = img.width - 1005 #this 55 is also a sample  size in pixels
	#drawLines(amountStatusDelStart,new_img)
	#drawLines(amountStatusDelEnd,new_img)
#
#

#if (img.width = personal check) # default to personal as md classifies smallers business checks as personal
	#whatever logic for personal check
	#amountStatusDelStart = img.width - 505 #this 35 will be from ansi standards
	#amountStatusDelEnd = img.width - 1005 #this 55 is also a sample  size in pixels
	#drawLines(amountStatusDelStart,new_img)
	#drawLines(amountStatusDelEnd,new_img)

drawLines(amountStatusDelStart,new_img)
drawLines(amountStatusDelEnd,new_img)
#show the image with default os imageviewer
new_img.show()
#save the new image to jpeg called DrawnOn
new_img.save('DrawnOn.jpeg' ,'jpeg')

	

