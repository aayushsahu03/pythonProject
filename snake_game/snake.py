import time
from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20


class Snake:

    def __init__(self):
        self.segments = []
        self.segments_position = []
        self.create_snake()
        self.head = self.segments[0]
        self.head_mod()


    def create_snake(self):
        """

        :return:
        """
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        segment_1 = Turtle("square")
        segment_1.color("white")
        segment_1.shapesize(0.75, 0.75)
        segment_1.penup()
        segment_1.goto(position)
        self.segments.append(segment_1)
        self.segments_position.append(segment_1.position())

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def reset(self):
        for seg in self.segments:
            seg.goto(1000,100)

        self.segments.clear()
        self.create_snake()
        self.head =self.segments[0]
        self.head_mod()

    def head_mod(self):
        self.head.color("cyan")
        self.head.shape("circle")
        self.head.shapesize(1, 1)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() == 270:
            return
        else:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() == 90:
            return
        else:
            self.head.setheading(-90)

    def left(self):
        if self.head.heading() == 0:
            return
        else:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() == 180:
            return
        else:
            self.head.setheading(0)

