import pygame as pg
from math import sin, cos, radians
from time import sleep

class Automata:
	def __init__(self, w, h, screen):
		self.w, self.h = w, h
		self.screen = screen
		self.grid = [[ 0 for i in range(self.w)] for j in range(self.h)]
		self.ant = [int(self.w/2), int(self.h/2)]
		self.head = [0, -1]

	def lt(self):
		a = radians(-90)
		x = int(self.head[0] *cos(a) - self.head[1] *sin(a))
		y = int(self.head[0] *sin(a) + self.head[1] *cos(a))
		self.head = [x, y]
	
	def rt(self):
		a = radians(90)
		x = int(self.head[0] *cos(a) - self.head[1] *sin(a))
		y = int(self.head[0] *sin(a) + self.head[1] *cos(a))
		self.head = [x, y]

	def fd(self):
		new_x = self.ant[0] + self.head[0]
		new_y = self.ant[1] + self.head[1]
		self.ant = [new_x, new_y]

	def update(self):
		if self.grid[self.ant[0]][self.ant[1]] == 0:
			self.grid[self.ant[0]][self.ant[1]] = 1
			pg.draw.circle(self.screen, color('white'), (self.ant[0]*4, self.ant[1]*4), 2, 2)
			self.rt()
			self.fd()

		if self.grid[self.ant[0]][self.ant[1]] == 1:
			self.grid[self.ant[0]][self.ant[1]] = 0
			pg.draw.circle(self.screen, color('black'), (self.ant[0]*4, self.ant[1]*4), 2, 2)
			self.lt()
			self.fd()



pg.init()
running = True
w, h = 100, 100
color = pg.Color
screen = pg.display.set_mode((w*4,h*4))

LA = Automata(w , h, screen)

while running:
	for event in pg.event.get():
		if event.type == pg.QUIT:
			running = False
	try:
		LA.update()
	except Exception:
		pass
	pg.display.flip()
	#sleep(0.3)
	#screen.fill(color('black'))

pg.quit()
