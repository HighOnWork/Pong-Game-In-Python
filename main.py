import turtle
import time
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

def game_loop():
    if ping_pong_ball.xcor() >= 280:
        return None
    ping_pong_ball.ball_move()
    new_screen.screen.update()
    new_screen.screen.ontimer(game_loop, 50)

Racket_right.location('right')
Racket_right.rectangle()
Racket_left.location('left')
Racket_left.rectangle()
turtle.update()

game_loop()

new_screen.screen.mainloop()
