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
    Dist_from_left = ping_pong_ball.distance(Racket_left)
    Dist_from_Right = ping_pong_ball.distance(Racket_right)
    ping_pong_ball.ball_physics(dist_value_l=Dist_from_left, dist_value_r=Dist_from_Right)
    new_screen.screen.onkeypress(Racket_left.move_up, "w")
    new_screen.screen.onkeypress(Racket_left.move_down, "s")
    new_screen.screen.onkeypress(Racket_right.move_up, "Up")
    new_screen.screen.onkeypress(Racket_right.move_down, "Down")
    if ping_pong_ball.xcor() >= 280:
        return None
    ping_pong_ball.ball_move()
    new_screen.screen.update()
    new_screen.screen.ontimer(game_loop, 50)

Racket_right.location('right')
Racket_left.location('left')

turtle.update()

game_loop()

new_screen.screen.mainloop()
