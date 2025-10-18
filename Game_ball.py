from turtle import Turtle

ROTATION_VALUE = 40

class BallForGame(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.showturtle()
        self.color("white")
        self.shape("circle")
        self.x_move = 10
        self.right(ROTATION_VALUE)

    def ball_move(self):
        if self.x_move == 10:
            self.forward(self.x_move)
        else:
            self.backward(self.x_move)
    
    def ball_physics(self):
        new_angle = 180 - ROTATION_VALUE
        if new_angle == 0:
            new_angle = 90
        if new_angle <= 90:
            self.left(new_angle)
        else:
            self.right(new_angle)
        self.x_move *= -1