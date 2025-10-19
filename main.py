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
ping_pong_ball = BallForGame()
score_on_both_sides = ScoreboardGame()

def game_loop():
    score_on_both_sides.score()
    ping_pong_ball.if_on_top_or_bottom()
    Racket_left.coordinates('left')
    Racket_right.coordinates('right')
    if Racket_left.rectangle_top_y >= ping_pong_ball.ycor() >= Racket_left.rectangle_bottom_y and Racket_left.rectangle_other_x >= ping_pong_ball.xcor() >= Racket_left.rectangle_x:
        ping_pong_ball.ball_physics()
    if Racket_right.rectangle_top_y >= ping_pong_ball.ycor() >= Racket_right.rectangle_bottom_y and Racket_right.rectangle_other_x >= ping_pong_ball.xcor() >= Racket_right.rectangle_x:
        ping_pong_ball.ball_physics()
    new_screen.screen.onkeypress(Racket_left.move_up, "w")
    new_screen.screen.onkeypress(Racket_left.move_down, "s")
    new_screen.screen.onkeypress(Racket_right.move_up, "Up")
    new_screen.screen.onkeypress(Racket_right.move_down, "Down")
    if ping_pong_ball.xcor() >= 280:
        score_on_both_sides.left_score() 
        ping_pong_ball.goto(0, 0)
    elif ping_pong_ball.xcor() <= -290:
        score_on_both_sides.right_score()
        ping_pong_ball.goto(0, 0)
    ping_pong_ball.ball_move()
    new_screen.screen.update()
    new_screen.screen.ontimer(game_loop, 50)

Racket_right.location('right')
Racket_left.location('left')

turtle.update()

game_loop()

new_screen.screen.mainloop()

