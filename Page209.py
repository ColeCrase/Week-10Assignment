from turtle import Turtle
def drawSquare(t, x, y, length):
    """Draws a square with the given turtle t, an upper-left
    corner point (x, y), and a side's length."""
    t.up()
    t.goto(x, y)
    t.setheading(270)
    t.down()
    for count in range(4):
        t.forward(length)
        t.left(90)
def main ():
    t = Turtle()
    x = 50
    y = 100
    length = 120
    drawSquare(t, x, y, length)
main()
