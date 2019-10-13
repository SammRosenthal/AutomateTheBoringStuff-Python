# this allows you to import methods and not have to call them with the ranomd.example()
from random import *

# this lets you run the method without appending random. unlike import random
import sys

# you can import modules like sys or random with pip (included with python installation)

# same thing
randint(1, 10)

# this cancels the program
# sys.exit()

def hello():
    print('Howdy')
    print("Howdy!")
    print('Hello there.')


hello()

def hello(name):
    print("hello " + name, end="")
    print("cat", "dog", "mouse", sep=" - ")


hello("sam")


hello("robert")
