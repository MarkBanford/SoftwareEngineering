import unittest
import math


def circle_area(r):
    return math.pi * r ** 2


class TestCircleArea(unittest.TestCase):

    # Test case 1
    def test_circle_area_radius_1(self):
        result = circle_area(1)
        self.assertAlmostEqual(result, math.pi, delta=1e-9)

    # Test case 2
    def test_circle_area_radius_2(self):
        result = circle_area(2)
        self.assertAlmostEqual(result, 4 * math.pi, delta=1e-9)

    # Test case 3
    def test_circle_area_negative_radius(self):
        self.assertRaises(ValueError, circle_area, -2)

    # Test case 4
    def test_circle_area_string_radius(self):
        self.assertRaises(TypeError, circle_area, "a")


if __name__ == '__main__':
    unittest.main()
