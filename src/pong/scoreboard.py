from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self, shape: str = "classic", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.color("white")
        self.up()
        self.hideturtle()
        self.p1_score = 0
        self.p2_score = 0
        self.write_scoreboard()

    def write_scoreboard(self):
        self.clear()
        self.goto(-100,200)
        self.write(self.p1_score, align="center", font=("Courier", 60, "normal"))
        self.goto(100,200)
        self.write(self.p2_score, align="center", font=("Courier", 60, "normal"))

    def p1_point(self):
        self.p1_score+=1
        self.write_scoreboard()

    def p2_point(self):
        self.p2_score+=1
        self.write_scoreboard()
