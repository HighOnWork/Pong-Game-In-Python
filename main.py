import turtle
from turtle import Screen, Turtle
from MyGameScreen import MyScreen
from Scoreboard import ScoreboardGame
from Game_ball import BallForGame
from Rackets import RacketsForGame

new_screen = MyScreen()
Racket_left = RacketsForGame()
Racket_right = RacketsForGame()
my_score = ScoreboardGame()
ping_pong_ball = BallForGame()

Racket_right.location('right')
Racket_right.rectangle()
Racket_left.location('left')
Racket_left.rectangle()

# now keep the window open
turtle.mainloop()
