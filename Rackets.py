import turtle
from turtle import Turtle

RECTANGLE_HEIGHT = 50
RECTANGLE_BREADTH = 10

class RacketsForGame(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.pencolor("white")
        self.hideturtle()

    def location(self, side):
        if side == 'right':
            self.goto(280, 0)
        else:
            self.goto(-297, 0)
    def rectangle(self):
        self.begin_fill()
        self.forward(RECTANGLE_BREADTH)
        self.seth(90)
        self.forward(RECTANGLE_HEIGHT)
        self.seth(180)
        self.forward(RECTANGLE_BREADTH)
        self.seth(270)
        self.forward(RECTANGLE_HEIGHT)
        self.end_fill()
        turtle.update()

