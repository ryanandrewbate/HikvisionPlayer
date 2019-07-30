import pygame
from PIL import Image

class ScreenGrid:


	screen = None

	out_width = 0
	out_height = 0
	rows = 0
	cols = 0
	col_size = 0
	row_size = 0
	cell_count = 0
	scale = (0,0)
	error_image = None
	coords = []
	font = None

	def __init__(self,rows,cols):
		self.rows = rows
		self.cols = cols
	
		pygame.init()
		pygame.mouse.set_visible(0)
	
		self.width =  pygame.display.Info().current_w
		self.height = pygame.display.Info().current_h
		self.screen = pygame.display.set_mode((self.width,self.height))
		self.font = pygame.font.Font('ApercuPro-Mono.ttf', 24) 


		self.calcGrid()
		self.calcCoords()
		self.preGenErrorImage()
		self.showSplash()

		print(self.coords)

	def calcGrid(self):
		self.col_size = self.width//self.cols
		self.row_size = self.height//self.rows
		self.scale = (self.col_size, self.row_size)
		self.cell_count = self.rows * self.cols

	def calcCoords(self):
		images = []
		for cell in range(self.cell_count):
			x = (cell % self.cols) * self.col_size
			y = (cell // self.rows) * self.row_size
			images.insert(cell,(x,y))
		
		text = []
		offset_x = self.col_size//2
		offset_y = (self.row_size//8)*7
		for cell in images:
			text.append(((cell[0] + offset_x),(cell[1] + offset_y)))
		self.coords = [images,text]

	def showSplash(self):
		pygame.display.set_caption('CCTV Viewer')
		self.screen.fill((0,0,0))
		pygame.display.update()

	def preGenErrorImage(self):
		pil_image = Image.open("error.jpg")
		pre_scale = pygame.image.fromstring(pil_image.tobytes(), pil_image.size, pil_image.mode)
		self.error_image = pygame.transform.scale(pre_scale, self.scale)

	def getScreen(self):
		return self.screen

	def showImage(self,image,cell):
		unscaled = pygame.image.fromstring(image.tobytes(), image.size, image.mode)
		scaled = pygame.transform.scale(unscaled, (self.scale))
		self.showInCell(scaled,cell)


	def showInCell(self,surface,cell):
		self.screen.blit(surface,self.coords[0][cell])
		pygame.display.update()

	def showError(self,cell):
		self.screen.blit(self.error_image,self.coords[0][cell])
		pygame.display.update()

	def showLabel(self,text,cell):
		label = self.font.render(text, True, (255,255,255), (26,26,26))
		labelBox = label.get_rect()
		labelBox.center = self.coords[1][cell]
		self.screen.blit(label, labelBox) 
		pygame.display.update()


		