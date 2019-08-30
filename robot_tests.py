import unittest 
from robot import bounds, Robot
 
class SimpleTest(unittest.TestCase): 

  
    # Returns True or False.  
	def test_Bounds(self):
		self.assertEqual(bounds((0,1)), False, "Should be False")
		self.assertEqual(bounds((1,0)), False, "Should be False")
		self.assertEqual(bounds((6,1)), False, "Should be False")
		self.assertEqual(bounds((1,6)), False, "Should be False")
		
		self.assertEqual(bounds((1,1)), True, "Should be True")
		self.assertEqual(bounds((5,5)), True, "Should be True")
		self.assertEqual(bounds((2,4)), True, "Should be True")
	
	def test_setup(self):
		self.assertTrue(True)
  
	def test_move(self):
		t1 = Robot(1, 1, "EAST")
		t1.move()
		self.assertEqual(t1.pos, (2,1), "Should be (1,2)")
		
		t1 = Robot(1, 1, "WEST")
		t1.move()
		self.assertEqual(t1.pos, (1,1), "Should be (1,1)")
		
		t1 = Robot(1, 1, "NORTH")
		t1.move()
		self.assertEqual(t1.pos, (1,2), "Should be (1,1)")
		
		t1 = Robot(1, 1, "SOUTH")
		t1.move()
		self.assertEqual(t1.pos, (1,1), "Should be (1,1)")

	def test_left(self):
		t1 = Robot(1, 1, "EAST")
		t1.left()
		self.assertEqual(t1.orient.value, 0, "Should be NORTH:0")
		t1.left()
		self.assertEqual(t1.orient.value, 3, "Should be WEST:3")
		t1.left()
		self.assertEqual(t1.orient.value, 2, "Should be SOUTH:2")
		t1.left()
		self.assertEqual(t1.orient.value, 1, "Should be EAST:1")
	
	def test_right(self):
		t1 = Robot(1, 1, "NORTH")
		t1.right()
		self.assertEqual(t1.orient.value, 1, "Should be EAST:1")
		t1.right()
		self.assertEqual(t1.orient.value, 2, "Should be SOUTH:2")
		t1.right()
		self.assertEqual(t1.orient.value, 3, "Should be WEST:3")
		t1.right()
		self.assertEqual(t1.orient.value, 0, "Should be NORTH:0")
	
if __name__ == '__main__': 
    unittest.main() 
