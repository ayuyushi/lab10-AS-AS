"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math

# First example
def square_root(a): 
    math.sqrt(a)
     if a < 0:
        raise ValueError

def hypotenuse(a, b): 
    math.hypot(a, b)

def add(a, b): 
    return a + b

def logarithm(a, b): loga(b)
    try:
        return math.log(b, a)
        if b <= 0 or a <= 0:
            raise ValueError

def add(a, b):
    return a + b

def mul(a, b):
    return a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError
    return b / a

def exp(a, b):
    return a ** b

