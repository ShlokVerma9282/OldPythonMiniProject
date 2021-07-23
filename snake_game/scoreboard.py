from turtle import Turtle


class Score_Board(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.penup()
        self.goto(0, 260)
        self.write(f"Score = {self.score}", align='center', font=('Courier', 24, "normal"))
        self.hideturtle()

    def food_eaten(self):
        self.score += 1
        self.clear()
        self.write(f"Score = {self.score}", align='center', font=('Courier', 24, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align='center', font=('Courier', 24, "normal"))
