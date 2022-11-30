from turtle import  Screen
import time
from snake import Snake
from food import Food
from scoreboard import Score
scr = Screen()
scr.setup(width=600,height=600)
scr.bgcolor("black")
scr.title("Snake Game")
scr.tracer(0)
snakes = Snake()
food = Food()
score = Score()
scr.listen()

scr.onkey(key="Up",fun=snakes.up)
scr.onkey(key="Down",fun=snakes.down)
scr.onkey(key="Left",fun=snakes.left)
scr.onkey(key="Right",fun=snakes.right)

game_on = True

while game_on:
        scr.update()
        time.sleep(0.1)
        snakes.move()

        #detect collision with food
        if snakes.all_segments[0].distance(food) <= 15:
                score.update_score()
                food.refresh()
                snakes.extend()

        #detect collision with wall

        x = snakes.all_segments[0].xcor()
        y = snakes.all_segments[0].ycor()
        if x>290 or x<-290 or y>290 or y<-290 :
                game_on = False
                score.game_over()

        #detect collision with its tail
        for segment in snakes.all_segments[1:]:
                if snakes.all_segments[0].distance(segment)<10:
                        game_on = False
                        score.game_over()


















scr.exitonclick()