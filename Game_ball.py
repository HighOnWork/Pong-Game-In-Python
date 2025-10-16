from turtle import Turtle

class BallForGame(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.showturtle()
        self.color("white")
        self.shape("circle")
        self.x_move = 10

    def ball_move(self):
        self.goto(self.xcor() + self.x_move, self.ycor())