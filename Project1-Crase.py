"""
Program: Project1
Author: Cole Crase
This program draws a specified circle by turing 3 degrees and moving a given
distance 120 times. It also calculates the distance moved with the formual
below.
"""

from turtle import Turtle

def drawCircle(t, center, r):
    circumference = 2 * 3.14 * (r / 120)
    print("The circumference moved is ", circumference)
    for count in range(120):
        t.down()
        t.left(3)
        t.circle(r)
        (x, y) = center[-1]

def main():
    t = Turtle()
    drawCircle(t, [(120, 120)], 120)

main()
