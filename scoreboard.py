from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Courier', 20, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open('data.txt') as data:
            self.high_score = int(data.read())
        self.print_scoreboard()

    def print_scoreboard(self):
        self.clear()
        self.ht()
        self.penup()
        self.goto(x=0, y=270)
        self.write(f"Score: {self.score}  High Score: {self.high_score}", move=False, align=ALIGNMENT, font=FONT)

    def increment_score(self):
        self.score += 1
        self.print_scoreboard()

    def reset_scoreboard(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('data.txt', mode='w') as data:
                data.write(str(self.high_score))
        self.score = 0
        self.print_scoreboard()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", move=False, align=ALIGNMENT, font=FONT)
