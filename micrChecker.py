#these are imports of imaging libraries to manipulate check image
from PIL import Image, ImageDraw

def drawLines(linePos, img):
	#open new imagedraw library for image manipulate on img variable passed to method
	draw = ImageDraw.Draw(img)
	#Parameters for Drawline
	#(xy coordninates of start, xy coordinates of end), ink, width
	#PIL.ImageDraw.ImageDraw.line(xy, fill=None, width=0, joint=None)
	draw.line((linePos, 0,linePos,img.height),fill=10,width=3)

#this is a sample check image this needs to be in the same folder as this script
#frontCheckImg = '149e1354-7a75-48ef-82e1-412759516e4b.FrontImage.BestBinarized.48f9e6ba-fa3f-49c3-9bfe-2ba360b62a02.tiff'

#this is a testing image
frontCheckImg = 'purp.jpeg'
#open image	
img = Image.open(frontCheckImg)
# (0,0) coordinate in imagedraw begins in top left corner of image. since ansi x9 standards place amount status delimeters from right edge
#of check, we subtract the difference of the standars from the width of the check to get the appropriate placement of our delimeter
amountStatusDelStart = img.width - 35 #this 35 will be from ansi standards
amountStatusDelEnd = img.width - 55 #this 55 is also a sample 
# assign image to new variable for manipulation
new_img = img
drawLines(amountStatusDelStart,new_img)
drawLines(amountStatusDelEnd, new_img)
#show the image with default os imageviewer
new_img.show()
#save the new image to jpeg called DrawnOn
new_img.save('DrawnOn.jpeg' ,'jpeg')

	

