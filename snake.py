from turtle import Turtle
MOVE_DISTANCE = 20
UP = 90
LEFT = 180
DOWN = 270
RIGHT = 0
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
SHAPE = "turtle"
COLOR = "pink"


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.speed = MOVE_DISTANCE

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def reset_snake(self):
        for seg in self.segments:
            seg.goto(10000, 10000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def add_segment(self, position):
        snake = Turtle(shape=SHAPE)
        snake.penup()
        snake.color(COLOR)
        snake.setpos(position)
        self.segments.append(snake)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_head = self.segments[seg_num - 1].heading()
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].seth(new_head)
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(self.speed)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.seth(UP)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.seth(LEFT)

    def down(self):
        if self.head.heading() != UP:
            self.head.seth(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.seth(RIGHT)

    # def pause(self):
    #     if self.speed == MOVE_DISTANCE:
    #         self.speed = 0
    #     elif self.speed == 0:
    #         self.speed = MOVE_DISTANCE
    #