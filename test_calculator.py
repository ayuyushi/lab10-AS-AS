# https://github.com/ayuyushi/lab10-AS-AS.git
# Partner 1: Ayushi Srivastava
# Partner 2: Ava Savino

import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self):
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(90.5, 40), 130.5)
        self.assertEqual(add(-5, 2), -3)

    def test_subtract(self):
        self.assertEqual(subtract(3, 2), 1)
        self.assertEqual(subtract(-5, 2), -7)
        self.assertEqual(subtract(90.5, 40), 50.5)
    # ##########################

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(3, 4), 12)
        self.assertAlmostEqual(mul(-1.5, 4), -6)
        self.assertAlmostEqual(mul(2.25, 2.25), 5.0625)

    def test_divide(self): # 3 assertions
        self.assertAlmostEqual(div(5, 12), 2.4)
        self.assertAlmostEqual(div(-2.25, -2.5), 1.1111111111111112)
        self.assertEqual(div(4, 12), 3)


    # ##########################

    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
    #     # call division function inside, example:
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)
    #     fill in code

    def test_logarithm(self): # 3 assertions
        self.assertAlmostEqual(logarithm(10, 100), 2)
        self.assertAlmostEqual(logarithm(2, 8), 3)
        self.assertAlmostEqual(logarithm(3, 381, 4)

    def test_log_invalid_base(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(100,-2)
    # ##########################
    
    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
    #     # call log function inside, example:
        with self.assertRaises(ValueError):
            logarithm(0, 5)
    #     fill in code
    
    def test_hypotenuse(self): # 3 assertions
        self.assertAlmostEqual(hypotenuse(4, 3), 5)
        self.assertAlmostEqual(hypotenuse(-8, 3), 8.54400374531753)
        self.assertAlmostEqual(hypotenuse(8.9, 9.8), 13.238202294873727)

    def test_sqrt(self): # 3 assertions
    #     # Test for invalid argument, example:
        with self.assertRaises(ValueError):
            square_root(-192)
    #     # Test basic function
        self.assertEqual(square_root(16), 4)
        self.assertAlmostEqual(square_root(6.25), 2.5)
    ##########################

# Do not touch this





if __name__ == "__main__":
    unittest.main()