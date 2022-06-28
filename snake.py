from turtle import Turtle
START_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20 # the width of segment(square) is 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()

    def create_snake(self):
        for position in START_POSITIONS:
            new_segment = Turtle(shape="square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)

    def move(self):
        for seg_num in range(len(self.segments)-1, 0, -1): # make snake body move follow by its head
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(20)

    def up(self):
        if self.segments[0].heading() != DOWN:
            self.segments[0].setheading(UP)
    
    def left(self):
        if self.segments[0].heading() != RIGHT:
            self.segments[0].setheading(LEFT)
    
    def down(self):
        if self.segments[0].heading() != UP:
            self.segments[0].setheading(DOWN)
    
    def right(self):
        if self.segments[0].heading() != LEFT:
            self.segments[0].setheading(RIGHT)
        