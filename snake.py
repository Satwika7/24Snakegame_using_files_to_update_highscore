from turtle import Turtle,Screen
scr = Screen()
POSITIONS = [(0,0),(0,-20),(0,-40)]

class Snake:

    def __init__(self):
        self.all_segments = []
        #self.all_positions = []
        self.create_snake()

    def create_snake(self):
        for each_square in range(3):
            self.add_segment(POSITIONS[each_square])



    def add_segment(self,position):
        snake = Turtle()
        snake.color("white")
        snake.shape("square")
        snake.penup()
        snake.goto(position)
        self.all_segments.append(snake)
        #self.all_positions.append(position)

    def extend(self):
        self.add_segment(self.all_segments[-1].position())

    def move(self):
        for each_position in range(len(self.all_segments) - 1):
            self.all_segments[len(self.all_segments) - 1 - each_position].goto(self.all_segments[len(self.all_segments) - 2 - each_position].position())

        self.all_segments[0].forward(20)

    def up(self):
        if self.all_segments[0].heading()!= 270.0:
             self.all_segments[0].setheading(90)

    def down(self):
        if self.all_segments[0].heading() !=90.0:
            self.all_segments[0].setheading(270)

    def right(self):
        if self.all_segments[0].heading() != 180.0:
            self.all_segments[0].setheading(0)

    def left(self):
        if self.all_segments[0].heading() != 0.0:
            self.all_segments[0].setheading(180)


