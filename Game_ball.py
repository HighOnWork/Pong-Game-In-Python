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
    
    def ball_physics(self, dist_value_l, dist_value_r):
        if dist_value_l <= 10 or dist_value_r <= 10:
            new_angle = 180 - self.tiltangle()
            self.tilt(new_angle)
            self.x_move *= -1