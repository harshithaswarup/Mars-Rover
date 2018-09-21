import unittest
from mars_roverr import Plateau
from mars_roverr import Rover
from mars_roverr import Directions


class TestString(unittest.TestCase):
    def test_direction(self):
        d = Directions(10,10,['x1'],0,0,'S','x1',['N','S','E','W']) 
        y = d.move_left('L')
        self.assertEqual(y,-1)

    def test_direction1(self):
        d = Directions(10,10,['x1'],0,0,'E','x1',['N','S','E','W']) 
        y = d.move_left('L')
        self.assertNotEqual(y,-1)

    def test_direction2(self):
        d = Directions(10,10,['x1'],0,0,'N','x1',['N','S','E','W']) 
        y = d.move_left('L')
        self.assertEqual(y,1)

    def test_direction3(self):
        d = Directions(10,10,['x1'],0,0,'W','x1',['N','S','E','W']) 
        y = d.move_left('L')
        self.assertEqual(y,-1)


class TestString_1(unittest.TestCase):
    def test_rover_direction(self):
        d = Directions(10,10,['x1'],0,0,'S','x1',['N','S','E','W']) 
        y = d.turn_left('L')
        self.assertEqual(y,'E')

    def test_rover_direction1(self):
        d = Directions(10,10,['x1'],0,0,'E','x1',['N','S','E','W'])
        y = d.turn_left('L')
        self.assertNotEqual(y,'E')

    def test_rover_direction2(self):
        d = Directions(10,10,['x1'],0,0,'W','x1',['N','S','E','W'])
        y = d.turn_right('R')
        self.assertEqual(y,'N')

    def test_rover_direction3(self):
        d = Directions(10,10,['x1'],0,0,'N','x1',['N','S','E','W'])
        y=d.turn_right('R')
        self.assertNotEqual(y,'N')
        
class TestString_2(unittest.TestCase):
    def test_add(self):
        d = Directions(10,10,['x1'],0,0,'S','x1',['N','S','E','W']) 
        rover = d.add_rover('x2')
        self.assertEqual(rover,['x1','x2'])

    def test_add_rover(self):
        d = Directions(10,10,['x1'],0,0,'S','x1',['N','S','E','W']) 
        rover = d.add_rover('x3')
        self.assertNotEqual(rover,['x1','x2'])

       
if __name__ == '__main__':
    unittest.main()

