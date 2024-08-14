from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.board = Turtle()
        self.board.hideturtle()
        self.board.penup()
        self.board.color("white")
        self.board.goto(0,270)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.board.clear()
        self.board.write(f"Score : {self.score}", align="center", font=("Arial",24,"normal"))

    def game_over(self):
        self.goto(0, 0)
        self.color("white")
        self.write("Game Over",align="center", font=("Arial",24,"normal"))


    def increase_score(self):
        self.score += 1
        self.update_scoreboard()