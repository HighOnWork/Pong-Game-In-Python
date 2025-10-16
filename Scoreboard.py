from turtle import Turtle

FONT_SIZE = 30
FONT_TYPE = 'Arial'
FONT_KIND = 'bold'
UPPER_SCREEN_EDGE = 250
ALIGNMENT_OF_TEXT = 'center'
SCORE = (0, 0)

class ScoreboardGame(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.goto(0, UPPER_SCREEN_EDGE)
        self.color("white")
        self.write(SCORE, align=ALIGNMENT_OF_TEXT, font=(FONT_TYPE, FONT_SIZE, FONT_KIND))
