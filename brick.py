from turtle import Turtle


class Brick(Turtle):

    def __init__(self, col, xpos, ypos):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.color(col)
        self.penup()
        self.setpos(xpos, ypos)
        self.active = 1
