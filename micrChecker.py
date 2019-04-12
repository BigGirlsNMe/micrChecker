#these are imports of imaging libraries to manipulate check image
from PIL import Image, ImageDraw, ImageTk
import Tkinter, tkFileDialog
import sys
#==============================================================================
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
#==============================================================
# create delimeters with different parameters depending on size of check
# variables set for business check


## change image to rgb type 8 bit add color dimension to draw lines on check image

def checkSize(img):
	print("\nChecksize method")
	if img.width > 1205: # check if business check 
		routingFieldDelStart = img.width - 1150 
		routingFieldDelEnd = img.width - 850 
		onUsFieldDelStart = img.width - 850
		onUSFieldDelEnd = img.width - 375
	
#==================================================================
#defaults to personal check if check size not big enough for business	
	else:
		print('toosmallforbiz') #default to personal if small size
		routingFieldDelStart = img.width - 950#bad numbers all in her for personal check size  
		routingFieldDelEnd = img.width - 650 
		onUsFieldDelStart = img.width - 650
		onUSFieldDelEnd = img.width - 175
	
#=======================================================================
# calls drawlines on whatever variables were set in the above conditions	
	drawLines(routingFieldDelStart,img)
	drawLines(routingFieldDelEnd,img)
	drawLines(onUSFieldDelEnd, img)
	drawLines(onUsFieldDelStart, img)
	img.save("Test.jpeg","jpeg")
	#img.show()
	return img
#==============================================================================
#Draw lines handled in this method
def drawLines(linePos, img):
	print("drawing lines on image here")
	#============================================
	#test
	#prob cannot convert here
	#imgRgb = img.convert("RGB")
	#==============================================
	#open new imagedraw library for image manipulate on img variable passed to method
	#=======================================
	draw = ImageDraw.Draw(img)
	#=======================================
	#drawrgb = ImageDraw.Draw(imgRgb)
	#Parameters for Drawline
	#(xy coordninates of start, xy coordinates of end), ink, width
	#PIL.ImageDraw.ImageDraw.line(xy, fill=None, width=0, joint=None)
	#draw.line((linePos, 0,linePos,img.height),128,width=5)
	#====================================================
	draw.line((linePos, 0,linePos,img.height),(0),width=2)
	#drawrgb.line((linePos, 0,linePos,imgRgb.height),fill=(255,0,0),width=2)
	#======================================================
	#draw.text((linePos+2),0, img.filename)
	return
#===============================================================================
# Creating Initializing UI components like title and app size
top = Tkinter.Tk()
top.title("micrChecker")
top.geometry('600x750')
canvasTop = Tkinter.Canvas(top, width=500, height=300)
canvasBtm = Tkinter.Canvas(top, width=500, height=300)
#=============================================================================
#open file explorer to select best binarized image from file explorer
def openFileExplore():
	file = tkFileDialog.askopenfile(parent=top,mode='rb',title='Upload BestBinarized Front')
	if file != None:
		img = Image.open(file)
		print(img.format + " image inside openFIleExplore")
		displayOnCanvas(img)
		#=================
		imgRgb = img.convert("RGB")
		#=================
		newImg = checkSize(imgRgb)
		#=========================
		print("New Image inside openFile ")
		displayOnBottom(newImg)
		#
		#get img ready for processing in here
		#
		file.close()
		#print "i got %d bytes from this file " % len(data)
		print "Exiting openFileExplore" + img.format
		top.mainloop()
		
#========================================================
#display to BottomSLopply redo
def displayOnBottom(img):
	print("This is inside diplay Bottom")
	imgSize = img.resize((425,175),Image.ANTIALIAS)
	print(imgSize.width)
	tkpi = ImageTk.PhotoImage(imgSize)
	canvasBtm.create_image(250,175,image=tkpi)
	canvasBtm.image = tkpi # required or will be garbage collected
	return
	
#======================================================	
		
#========================================================
#display to Canvas
def displayOnCanvas(img):
	print("This is inside diplay on Canvas")
	imgSize = img.resize((425,175),Image.ANTIALIAS)
	print("Image width after resize" )
	tkpi = ImageTk.PhotoImage(imgSize)
	canvasTop.create_image(250,175,image=tkpi)
	canvasTop.image = tkpi
	return
	
#======================================================	
#pack components into ui

BUpload = Tkinter.Button (top, text = 'Upload BestBinarized Front', command = openFileExplore)
#BConvert = Tkinter.Button(top, text = 'Draw delimeters', command= displayOnCanvas)
#BHelp = TkinterButton(top,text='Help",command = openHelp)
BUpload.pack(padx=10, pady=10)
canvasTop.pack(padx=10,pady=10)
canvasBtm.pack(padx=10,pady=10)
#BConvert.pack(padx=10, pady=10)

#=============================================================

top.mainloop() #makes menu and does nothing until you interact with items

sys.exit("Stopped")
#check image this needs to be in the same folder as this script
frontCheckImg = openFileExplore

#====================================================
#frontCheckImg = 'mdtestimg.tiff'
# assign image to new variable for manipulation

#open image	and print some image details
img = Image.open(frontCheckImg)
print("Format of image = " + img.format + "\nMode of Image = " + img.mode + "\nDPI = ")
print(img.info['dpi'])

# (0,0) coordinate in imagedraw begins in top left corner of image. since ansi x9 standards place amount status delimeters from right edge of check, we subtract the difference of the standars from the width of the check to get the appropriate placement of our delimeter


	
#========================================================================
#shows image produced and saves it 	
#show the image with default os imageviewer
img.show()
#save the new image to jpeg called DrawnOn
img.save('DrawnOn.jpeg' ,'jpeg')
