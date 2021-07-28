from turtle import Turtle
def square(t, sLength):
    """Draws a square with the given length."""
    for count in range(4):
        t.forward(sLength)
        t.left(90)

def hexagon(t, hLength):
    """Draws a hexagon with the given length."""
    for count in range(6):
        t.forward(hLength)
        t.left(60)

def main():
    t = Turtle()
    sLength = 100
    hLength = 100
    square(t, sLength)
    hexagon(t, hLength)

main()
