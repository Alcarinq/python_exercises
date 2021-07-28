import unittest


class Robot:
    def __init__(self, location, bearing):
        self.location = location
        self.bearing = bearing

    def move_robot_forward(self):
        self.location[1] += 1

    def change_location_to_left(self):
        if self.bearing == 'North':
            self.bearing = 'West'
        elif self.bearing == 'West':
            self.bearing = 'South'
        elif self.bearing == 'South':
            self.bearing = 'East'
        elif self.bearing == 'East':
            self.bearing = 'North'


class TestRobot(unittest.TestCase):
    def test_check_initial_coordinates(self):
        robot = Robot([0, 0], 'North')
        self.assertEqual(robot.location, [0, 0])
        self.assertEqual(robot.bearing, 'North')

    def test_check_robot_move(self):
        robot = Robot([0, 0], 'North')
        robot.move_robot_forward()
        self.assertEqual(robot.location, [0, 1])
        self.assertEqual(robot.bearing, 'North')

    def test_check_robot_move_twice(self):
        robot = Robot([0, 0], 'North')
        robot.move_robot_forward()
        robot.move_robot_forward()
        self.assertEqual(robot.location, [0, 2])
        self.assertEqual(robot.bearing, 'North')

    def test_change_location_to_left_from_north(self):
        robot = Robot([0, 0], 'North')
        robot.change_location_to_left()
        self.assertEqual(robot.location, [0, 0])
        self.assertEqual(robot.bearing, 'West')

    def test_change_location_to_left_from_west(self):
        robot = Robot([0, 0], 'West')
        robot.change_location_to_left()
        self.assertEqual(robot.location, [0, 0])
        self.assertEqual(robot.bearing, 'South')

    def test_change_location_to_left_from_south(self):
        robot = Robot([0, 0], 'South')
        robot.change_location_to_left()
        self.assertEqual(robot.location, [0, 0])
        self.assertEqual(robot.bearing, 'East')

    def test_change_location_to_left_from_east(self):
        robot = Robot([0, 0], 'East')
        robot.change_location_to_left()
        self.assertEqual(robot.location, [0, 0])
        self.assertEqual(robot.bearing, 'North')

