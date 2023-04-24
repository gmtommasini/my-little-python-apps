from turtle import Turtle


class Ball(Turtle):
    def __init__(self, shape: str = "classic", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape='circle')
        self.color('cyan')
        self.up()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1
    
    def reset_position(self):
        self.goto(0,0)
        self.move_speed = 0.1
        self.bounce_x()

    def move(self):
        self.goto(self.xcor()+ self.x_move, self.ycor()+self.y_move)

    def increase_speed(self):
        self.move_speed *= 0.9

    def bounce_y(self):
        self.y_move *= -1
        self.increase_speed()

    def bounce_x(self):
        self.x_move *= -1
        self.increase_speed()
