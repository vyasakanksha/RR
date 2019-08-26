""" 
Goal: Toy Robot Simulator 

 
_______________
|__|__|__|__|__|
|__|__|__|__|__|
|__|__|__|__|__|
|__|__|__|__|__|
|00|__|__|__|__|
"""


from enum import Enum


class Orientation(Enum):
   NORTH = 0
   EAST = 1
   SOUTH = 2
   WEST = 3


class Robot:
	def __init__(self, pos = (0,0), orient = Orientation.NORTH):
		self.pos = pos
		self.orient = orient

	def place(self, x, y, f):
		self.pos = (x,y)
		self.orient = Orientation[f]

	def left(self):
		val = (self.orient.value - 1) % 4 
		self.orient = Orientation(val)

	def right(self):
		val = (self.orient.value + 1) % 4 
		self.orient = Orientation(val)

	def move(self):
		self.pos = { 
		  0: (self.pos[0], self.pos[1]+1), 
		  1: (self.pos[0]+1, self.pos[1]), 
		  2: (self.pos[0], self.pos[1]-1), 
		  3: (self.pos[0]-1, self.pos[1]), 
		}[self.orient.value]

	def report(self):
		print("position: {} facing {}".format(self.pos, self.orient.name))


test = Robot()
test.place(4,5,"WEST")
test.left()
test.left()
test.left()
test.move()
test.report()
