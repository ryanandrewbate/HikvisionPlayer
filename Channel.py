import time
from PIL import Image

class Channel:

	number = -1
	apiNo = -1
	cell = -1
	client = None
	labelText = ""
	inError = False
	screengrid = None
	scale = (0,0)
	error_image = None
	coord = (0,0)
	label_coord = (0,0)

	def __init__(self, no, cell, client, screengrid):

		self.number = no
		self.cell = cell
		self.client = client
		self.apiNo = str(no)+"01"
		self.labelText = 'Channel '+str(no)
		self.screengrid = screengrid


	def getImage(self):
		response = self.client.Streaming.channels[self.apiNo].picture(method='get', type='opaque_data')
		original = Image.open(response.raw)
		return original

	def showImage(self, image):
		self.screengrid.showImage(image,self.cell)

	def showError(self):
		self.screengrid.showError(self.cell)

	def showLabel(self, text = ""):
		if(text == ""):
			text = self.labelText
		self.screengrid.showLabel(text, self.cell)

	def run(self):
		# Attempt to load in remote image, or replace with error image and carry on.
		try:
			image = self.getImage()
			self.showImage(image)
			self.showLabel()
			self.inError = False
		except:
			self.showError()
			self.showLabel("Error loading this channel")
			inError = True

