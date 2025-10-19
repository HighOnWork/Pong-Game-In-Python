from turtle import Turtle
import random

ROTATION_VALUE = 40

class BallForGame(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.showturtle()
        self.color("white")
        self.shape("circle")
        self.x_move = 10
        self.flag = False

    def ball_move(self):
        self.forward(self.x_move)
    
    def ball_physics(self):
        new_heading = 180 - self.heading()
        new_heading += random.randint(-10, 10)
        self.setheading(new_heading % 360)

    def if_on_top_or_bottom(self):
        if self.ycor() <= -290:
            self.flag = True
            new_heading = 150
            new_heading += random.randint(-10, 10)
        elif self.ycor() >= 290:
            self.flag = True
            new_heading = 200
            new_heading += random.randint(-10, 10)
        if self.flag:
            self.setheading(new_heading)
            self.flag = False