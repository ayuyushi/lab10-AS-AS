import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    # def test_add(self): # 3 assertions
    #     fill in code

    # def test_subtract(self): # 3 assertions
    #     fill in code
    # ##########################

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(3, 4), 12)
        self.assertAlmostEqual(mul(-1.5, 4), -6)
        self.assertAlmostEqual(mul(2.25, 2.25), 5.0625)

    def test_divide(self): # 3 assertions
        self.assertAlmostEqual(div(5, 12), 2.4)
        self.assertAlmostEqual(mul(-2.25, -2.5), 1.1111111111111112)
        self.assertEqual(div(4, 12), 3)


    # ##########################

    ######## Partner 2
    # def test_divide_by_zero(self): # 1 assertion
    #     # call division function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     div(0, 5)
    #     fill in code
        with self.assertRaises(ZeroDivisionError):
            div(0, 10)

    # def test_logarithm(self): # 3 assertions
    #     fill in code

    # def test_log_invalid_base(self): # 1 assertion
    #     # use same technique from test_divide_by_zero
    #     fill in code
    # ##########################
    
    ######## Partner 1
    # def test_log_invalid_argument(self): # 1 assertion
    #     # call log function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     logarithm(0, 5)
    #     fill in code

    # def test_hypotenuse(self): # 3 assertions
    #     fill in code

    # def test_sqrt(self): # 3 assertions
    #     # Test for invalid argument, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #    square_root(NUM)
    #     # Test basic function
    #     fill in code
    ##########################

# Do not touch this

def test_add(self):
    self.assertEqual(add(1, 2), 3)
    self.assertEqual(add(90.5, 40), 130.5)
    self.assertEqual(add(-5, 2), -3)
def test_subtract(self):
    self.assertEqual(sub(3, 2), 1)
    self.assertEqual(sub(-5, 2), -7)
    self.assertEqual(sub(90.5, 40), 50.5)
def test_divide_by_zero(self):
    self.assertRaise(Z)
def test_logarithm(self):
    self.assertEqual(math.log(100, 10), 2)
    self.assertEqual(math.log(8, 2), 3)
    self.assertEqual(math.log(81, 3), 4)

def test_log_invalid_base(self):
    self.assertEqual(ValueError, math.log(100,1))
    self.assertEqual(ValueError, math.log(100,0))
    self.assertEqual(ValueError, math.log(100,-2))



if __name__ == "__main__":
    unittest.main()