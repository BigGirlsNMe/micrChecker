#these are imports of imaging libraries to manipulate check image
from PIL import Image, ImageDraw

# Legend
# C = Transit Symbol 4.2
# P = On Us Symbol 
# / = amount symbol
# - = dash symbol
# DPI always 200 for best binarized image
# pixels / dpi = inches
# inches * dpi = pixels
# Business checks
# 4.250'' * 200 dpi = 850 pixels - end of routing field delimeter
# 5.750'' * 200dpi = 1150 pixels - start of routing field delimeter
# Personal Check cut off
# 1205 pixels = maximum allowance for personal check
# 4.250'' * 200 dpi = 850 pixels - start of on us field delimeter
# 1.875'' * 200dpi = 375 pixels - end of on us field delimeter

def drawLines(linePos, img):
	#open new imagedraw library for image manipulate on img variable passed to method
	draw = ImageDraw.Draw(img)
	#Parameters for Drawline
	#(xy coordninates of start, xy coordinates of end), ink, width
	#PIL.ImageDraw.ImageDraw.line(xy, fill=None, width=0, joint=None)
	#draw.line((linePos, 0,linePos,img.height),fill='blue',width=5)
	draw.line((linePos, 0,linePos,img.height),(0),width=1)
	#draw.text((linePos+2),0, img.filename)

#check image this needs to be in the same folder as this script
#frontCheckImg = 'custtest.tiff'
frontCheckImg = 'mdtestimg.tiff'
# assign image to new variable for manipulation

#open image	and print some image details
img = Image.open(frontCheckImg)
print("Format of image = " + img.format + "\nMode of Image = " + img.mode + "\nDPI = ")
print(img.info['dpi'])

# (0,0) coordinate in imagedraw begins in top left corner of image. since ansi x9 standards place amount status delimeters from right edge of check, we subtract the difference of the standars from the width of the check to get the appropriate placement of our delimeter

#create delimeters in different locationd depending on size of check


if img.width > 1205: # check if business check and set appropriate delimeter placement for lines
	routingFieldDelStart = img.width - 1150 
	routingFieldDelEnd = img.width - 850 
	onUsFieldDelStart = img.width - 850
	onUSFieldDelEnd = img.width - 375
		
else:
	print('toosmallforbiz') #default to personal check size if image smaller than 1205 pixels. 
	routingFieldDelStart = img.width - 950#bad numbers all in her for personal check size  
	routingFieldDelEnd = img.width - 650 
	onUsFieldDelStart = img.width - 650
	onUSFieldDelEnd = img.width - 175

#drawlines	
drawLines(routingFieldDelStart,img)
drawLines(routingFieldDelEnd,img)
drawLines(onUSFieldDelEnd, img)
drawLines(onUsFieldDelStart, img)		
		
#show the image with default os imageviewer
img.show()
#save the new image to jpeg called DrawnOn
img.save('DrawnOn.jpeg' ,'jpeg')

	

