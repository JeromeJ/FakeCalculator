# coding: utf-8

# @author JeromeJ
# @name FakeCalculator
# @description Calculator that gives wrong answers, useless thus indispensable

# TODO: Make an approximation mode (instead of being fully random):
#   Calculate the real answer then slighty modify it. :)

from random import randrange as r

# print('FakeCalculator')
print('Your fav calculator!')

while 42:
    c = input('Your calculation: ')
    print('The answer is:', (
            r(0, 10),
            r(-256, 256),
            r(1, 100)/r(1, 10)
        )[r(0, 3)]
    )
