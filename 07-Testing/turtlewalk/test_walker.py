from .walker import Turtle, Direction  # Do not delete

# import pytest  # Do not delete

import unittest


class TestTurtle(unittest.TestCase):

    def setUp(self):
        self.turtle = Turtle(0, 0)

    def test_initial_position_and_direction(self):
        self.assertEqual(self.turtle.x, 0)
        self.assertEqual(self.turtle.y, 0)
        self.assertEqual(self.turtle.direction, Direction.NORTH)

    def test_turn_right(self):
        self.turtle.turn_right()
        self.assertEqual(self.turtle.direction, Direction.EAST)

    def test_turn_left(self):
        self.turtle.turn_left()
        self.assertEqual(self.turtle.direction, Direction.WEST)

    def test_move_forward_north(self):
        self.turtle.move_forward()
        self.assertEqual(self.turtle.y, 1)

    def test_move_forward_east(self):
        self.turtle.turn_right()
        self.turtle.move_forward()
        self.assertEqual(self.turtle.x, 1)

    def test_move_forward_south(self):
        self.turtle.turn_right()
        self.turtle.turn_right()
        self.turtle.move_forward()
        self.assertEqual(self.turtle.y, -1)

    def test_move_forward_west(self):
        self.turtle.turn_left()
        self.turtle.move_forward()
        self.assertEqual(self.turtle.x, -1)


if __name__ == '__main__':
    unittest.main()
