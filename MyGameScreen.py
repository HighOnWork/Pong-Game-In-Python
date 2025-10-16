import turtle
from turtle import Screen

class MyScreen:
    def __init__(self):
        self.screen = Screen()
        self.screen.bgcolor("black")
        self.screen.setup(600, 600)
        self.screen.tracer(0)
