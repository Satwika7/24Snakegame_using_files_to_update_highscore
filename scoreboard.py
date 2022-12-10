from turtle import Turtle
ALIGNMNET = "right"
FONT = ('arial', 12, 'normal')

class Score(Turtle):

     def __init__(self):
         super().__init__()
         self.score = -1
         with open("data.txt") as data:
             content = data.read()
         self.highscore= content
         self.color("white")
         self.penup()
         self.hideturtle()

         self.update_score()

     def game_over(self):
         self.goto(0,0)
         self.write("GAME OVER", align=ALIGNMNET, font=FONT)

     def update_score(self):

         self.clear()
         self.score += 1
         self.goto(0, 280)
         self.write(f"score : {self.score}", align=ALIGNMNET, font=FONT)

         self.goto(120,280)
         self.write(f"High Score:{self.highscore}",align=ALIGNMNET, font=FONT)

     def update_highscore(self):
         if self.score>int(self.highscore):
             with open("data.txt",mode="w") as data:
                data.write(str(self.score))


