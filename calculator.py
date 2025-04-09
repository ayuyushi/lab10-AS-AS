"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math

# First example
def add(a, b): 
    return a + b

def multiply(a, b): 
    return a * b

def divide(a, b): 
    try:
        return b / a
        if a == 0:
            raise ZeroDivisionError 

def logarithm(a, b): loga(b)
    try:
        return math.log(b, a)
        if b <= 0 or a <= 0:
            raise ValueError


def exponent(a, b): 
    return a ** b

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError
    return b / a

def log(a, b):
    if a <= 0 or a == 1:
        raise ValueError
    if b <=0:
        raise ValueError
    return math.log(b, a)

def exp(a, b):
    return a ** b

