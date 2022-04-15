from turtle import Turtle
import random


def round_to_multiple(number, multiple):
    return multiple * round(number / multiple)


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = round_to_multiple(random.randint(-280, 280), 20)
        random_y = round_to_multiple(random.randint(-280, 280), 20)
        self.goto(random_x, random_y)
