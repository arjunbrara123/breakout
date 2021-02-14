from turtle import Turtle                               # Import Turtle library for class inheritance


class Paddle(Turtle):

    def __init__(self, pos):
        """Initialise 'Paddle' object as subclass of 'Turtle' object"""
        super().__init__()                              # Call 'turtle' initiation
        self.penup()                                    # Stop displaying trail
        self.shapesize(stretch_wid=1, stretch_len=5)    # Stretch turtle to create a 'paddle' shape
        self.color("white")                             # Set colour to white
        self.shape("square")                            # Set paddle shape
        self.setpos(pos)                                # Move paddle to desired position on screen

    def paddle_left(self):
        """Move a paddle left"""
        self.setx(self.xcor() - 60)                     # Move paddle left 60 paces

    def paddle_right(self):
        """Move a paddle right"""
        self.setx(self.xcor() + 60)                     # Move paddle right 60 paces