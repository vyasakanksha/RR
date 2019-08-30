"""
Goal: Toy Robot Simulator


_______________
|__|__|__|__|__|
|__|__|__|__|__|
|__|__|__|__|__|
|__|__|__|__|__|
|00|__|__|__|__|

Basic Functionality:
   * Init: function to place robot on board. Position + Orientation
* Left/Right: Increment/Decrement position by 1 mod 4 (4 directions)
   * Move: Increment/Decrement position by 1 depending on current orientation
   * Report: Print position and Orientation

   Special Functionality:
   * Bounds: This applied to place and move. If position is outside
   grid after the action, ignore it.
   * Place Robot first: Before the init function is called, everything else is ignored.

   Bonus Functionality:
   UI with buttons
   Shortest path

   Test Cases:
   *Unit Tests
   Bounds
   init
   move
   left
   right

   *Other Tests:
   Out of Bounds with Place:

   Out of Bounds with Move:

   Place not the first command:

   Place never called:

   No Errors:
   """


from enum import Enum


class Orientation(Enum):
   NORTH = 0
   EAST = 1
   SOUTH = 2
   WEST = 3

def bounds(pos):
   if pos[0] < 1 or pos[0] > 5 or pos[1] < 1 or pos[1] > 5:
      return False
   else:
      return True

class Robot:
   def __init__(self, x, y, f):
      pos = (x,y)
      if(not bounds(pos)):
         self.msg = "Out of bounds. No Action"
      else:
         try:
            self.pos = (x,y)
            self.orient = Orientation[f]
            self.msg = "PLACE {} {} {}".format(x, y, f)
         except KeyError:
            self.msg = "Incorect Input"

      print(self.msg)

   def left(self):
      val = (self.orient.value - 1) % 4
      self.orient = Orientation(val)
      self.msg = "LEFT"

   def right(self):
      val = (self.orient.value + 1) % 4
      self.orient = Orientation(val)
      self.msg = "RIGHT"


   def move(self):
      pos = {
         0: (self.pos[0], self.pos[1]+1),
         1: (self.pos[0]+1, self.pos[1]),
         2: (self.pos[0], self.pos[1]-1),
         3: (self.pos[0]-1, self.pos[1]),
      }[self.orient.value]

      if(not bounds(pos)):
         self.msg = "Out of bounds. No Action"
         print(self.msg)
      else:
         self.pos = pos
         self.msg = "MOVE"


   def report(self):
      print("position: {} facing {}".format(self.pos, self.orient.name))

if __name__ == "__main__":
   while(1):
      f = 0
      func = input("> ").split()
      try:
         if str(func[0]) == "PLACE":
            test = Robot(int(func[1]), int(func[2]), func[3])
         if str(func[0]) == "MOVE":
            test.move()
         if str(func[0]) == "LEFT":
            test.left()
         if str(func[0]) == "RIGHT":
            test.right()
         if str(func[0]) == "REPORT":
            test.report()
         else:
            print("Incorrect Command. No Action")
      except NameError:
         print("Error: Place the Robot on the Board")
      except AttributeError:
         print("Error: Place the Robot on the Board")
