import turtle
from turtle import Turtle

RECTANGLE_HEIGHT = 50
RECTANGLE_BREADTH = 10

class RacketsForGame(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("black")
        self.pencolor("black")
        self.rectangle()
        self.shape("rectangle")
        self.color("white")


    def location(self, side):
        if side == 'right':
            self.goto(280, 0)
        else:
            self.goto(-280, 0)

    def rectangle(self):
        self.begin_fill()
        self.begin_poly()
        self.forward(RECTANGLE_BREADTH)
        self.seth(90)
        self.forward(RECTANGLE_HEIGHT)
        self.seth(180)
        self.forward(RECTANGLE_BREADTH)
        self.seth(270)
        self.forward(RECTANGLE_HEIGHT)
        self.end_poly()
        self.end_fill()
        turtle.update()
        turtle.register_shape("rectangle", self.get_poly())

    def move_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)
        self.coordinates()
    def move_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
        self.coordinates()
    def coordinates(self, side):
            self.rectangle_top_y = self.ycor() + 10
            if side == 'right':
                self.rectangle_bottom_y = self.ycor() - 62
            else:
                self.rectangle_bottom_y = self.ycor() - 60
            self.rectangle_x = self.xcor() - 10
            if side == 'left':
                self.rectangle_other_x = self.xcor() + 10
            else:    
                self.rectangle_other_x = self.xcor() + 20