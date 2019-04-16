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

ogImgGlobal = None
ogImgAltered = None
# (0,0) coordinate in imagedraw begins in top left corner of image. since ansi x9 standards place amount status delimeters from right edge of check, we subtract the difference of the standars from the width of the check to get the appropriate placement of our delimeter

def checkSize(img):
	if img.width > 1205: # check if business check 
		print("Check size is determined to be business check")
		routingFieldDelStart = img.width - 1150 
		routingFieldDelEnd = img.width - 850 
		onUsFieldDelStart = img.width - 850
		onUSFieldDelEnd = img.width - 375
	
#==================================================================
#defaults to personal check if check size not big enough for business
#TODO: change if 	
	else:
		print('Check size is determined to be personal check') #default to personal if small size
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
	return img
#==============================================================================
#Draw lines handled in this method
def drawLines(linePos, img):
	print "drawing line on image at",linePos,"pixels"
	#open new imagedraw library for image manipulate on img variable passed to method
	draw = ImageDraw.Draw(img)
	#Parameters for Drawline
	#(xy coordninates of start, xy coordinates of end), ink, width
	#PIL.ImageDraw.ImageDraw.line(xy, fill=None, width=0, joint=None)
	#====================================================
	#green color lines
	draw.line((linePos, 0,linePos,img.height),(0,128,0),width=2)
	#======================================================
	#Trying to write text describing each delimeter
	#draw.text((linePos+2),0, img.filename)
	return

#=================================================================================
# just a method to convert to RGB format for better image manipulation
def convertToRGB(img):
		imgRgb = img.convert("RGB")
		return imgRgb
		
		
		
#=====================================================================================		
#TODO need to fill out this method		does not work!!!
def saveImage():
	fout = tkFileDialog.asksaveasfile(mode='w', defaultextension=".tiff")
	text2save = str(self.text.get(0.0,END))
	fout.write(text2save)
	fout.close()
		
	if f is None: # asksaveasfile return None if dialog is closed with cancel
		return
	
#===============================================================================
# Creating Initializing UI components like title and app size
top = Tkinter.Tk()
top.title("micrChecker")
#top.geometry('600x750') probably not needed now
buttonFrame = Tkinter.Frame(top)
canvasFrame = Tkinter.Frame(top)
#=============================================================================
#open file explorer to select best binarized image from file explorer
def openFileExplore():
	file = tkFileDialog.askopenfile(parent=top,mode='rb',title='Upload BestBinarized Front')
	if file != None:
		img = Image.open(file)
		print"***Original Images Information***\nFormat of image = " ,img.format , "\nMode of Image = " , img.mode , "\nDPI = ", img.info['dpi']
		#checks if file selected is null and displays image on cavas and sets image open to global variable		
		displayOnCanvas(img)
		global ogImgGlobal
		ogImgGlobal = img
		file.close()
		return 
		
#============================================================
#display to Bottom canvas. this is slopply and should redo
def displayOnBottom(img):
	print"Displaying altered image to bottom canvas"
	imgSize = img.resize((425,175),Image.ANTIALIAS)
	print"Resizing image for ui width = ", imgSize.width,", height = ", imgSize.height
	tkpi = ImageTk.PhotoImage(imgSize)
	canvasBtm.create_image(250,175,image=tkpi)
	canvasBtm.image = tkpi # required or will be garbage collected
	return
#=============================================================
#display to Canvas
def displayOnCanvas(img):
	print"Displaying Original Image to top Canvas"
	imgSize = img.resize((425,175),Image.ANTIALIAS)
	print"Resizing image for ui width = ", imgSize.width,", height = ", imgSize.height
	tkpi = ImageTk.PhotoImage(imgSize)
	canvasTop.create_image(250,175,image=tkpi)
	canvasTop.image = tkpi
	return
	
#======================================================	
# does the work for drawing lines on button calls our other methods. 
def manipulateImage():
	imgRgb = convertToRGB(ogImgGlobal)
	drawnOnImg = checkSize(imgRgb)
	print"***Altered Image information***\nFormat of image = " ,imgRgb.format , "\nMode of Image = " , imgRgb.mode , "\nDPI = ", imgRgb.info['dpi']
	displayOnBottom(drawnOnImg)
#=========================================================
#pack components into ui
#working in here
canvasTop = Tkinter.Canvas(canvasFrame, width=500, height=300)
canvasBtm = Tkinter.Canvas(canvasFrame, width=500, height=300)
BUpload = Tkinter.Button (buttonFrame, text = 'Upload bestbinarized front', command = openFileExplore)
BConvert = Tkinter.Button(buttonFrame, text = 'Draw Delimeters', command= manipulateImage)
#BHelp = TkinterButton(top,text='Help",command = openHelp)
BSave = Tkinter.Button(buttonFrame,text='Save image',command = saveImage)

#=============================================================================

buttonFrame.pack(side='top',)
canvasFrame.pack(side='bottom',fill='y')
BUpload.pack(side='left',fill='x',padx=10)
BConvert.pack(side='left',padx=10)
BSave.pack(side='left',padx=10)
canvasTop.pack()
canvasBtm.pack()


#=============================================================

top.mainloop() #makes menu and does nothing until you interact with items

sys.exit("Stopping program")
