from turtle import Turtle
FONT = ("Courier", 17, "bold")

class Level():
    """ Level will dictate the game's pace"""
    def __init__(self):
        self.level = 1
    
    def level_up(self):
        self.level+=1
    
    def reset(self):
        self.level = 1
        
    def get_level(self):
        return self.level
    
    def increase_level(self):
        self.level+=1
        
    def __str__(self):
        return str(self.level)
    
    def __add__(self, number: int):
        self.level += number
        return self
        
    def __iadd__(self, number: int):
        self.value += number
        return self

class Scoreboard(Turtle):
    def __init__(self, lvl:Level):
        super().__init__()
        self.color("white")
        self.up()
        self.hideturtle()
        self.level = lvl
        self.write_scoreboard()

    def write_scoreboard(self):
        self.clear()        
        self.goto(-290,170)
        self.write(f"Level: {self.level}", align="left", font=FONT)
        
    def level_up(self):
        self.level.increase_level()
        self.write_scoreboard()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER",align="center", font=FONT)