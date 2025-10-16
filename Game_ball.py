from turtle import Turtle

class BallForGame(Turtle):
    def __init__(self):
        super().__init__()
        self.speed("fastest")
        self.hideturtle()
        self.color("white", "white")
        self.begin_fill()
        self.circle(5)
        self.end_fill()