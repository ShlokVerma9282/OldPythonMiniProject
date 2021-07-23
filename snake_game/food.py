import random
from turtle import Turtle


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.color('blue')
        self.speed('fastest')
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.refresh()

    def refresh(self):
        rew_x = random.randint(-280, 280)
        rew_y = random.randint(-280, 280)
        self.goto(rew_x, rew_y)

