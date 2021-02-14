from turtle import Turtle, Screen       # Library for displaying GUI window
from scoreboard import Scoreboard       # Custom Class object to display user scores
from paddle import Paddle               # Custom Class object to create user paddles
from ball import Ball                   # Custom Class object for game ball that moves and bounces
from brick_manager import BrickManager  # Custom class to autogenerate bricks
import time                             # Library for pausing between ball movements to create animation effect

# Initialise the screen and environment
p_score = 0                             # Initialise Player score
screen = Screen()                       # Initialise screen object
screen.setup(width=800, height=600)     # Set up screen dimensions
screen.bgcolor("black")                 # Set screen background colour to black
screen.title("Breakout")                # Set screen window title
screen.tracer(0)                        # Turn off automatic screen updates
scoreboard = Scoreboard()               # Initialise scoreboard object to show player scores
brick_manager = BrickManager()          # Initialise the brick manager
brick_manager.setup_bricks()            # Set up on-screen bricks
time_delay = 0.008                      # Set initial ball speed
winning_score = 3                       # Set points required to win game
FONT_SPLASH = ("Courier", 80, "bold")   # Font for displaying 'Breakout' splash screen
FONT_MSG = ("Courier", 40, "bold")      # Font for displaying messages in centre screen

# Initialise the paddle
p1 = Paddle((0, -250))              # Player Paddle starting position
ball = Ball((0, 0))                 # Ball starting position
screen.update()                     # Update screen to let users see these

# Set up key listeners
screen.listen()
screen.onkey(p1.paddle_left, "Left")      # Player Paddle Left Key
screen.onkey(p1.paddle_right, "Right")   # Player Paddle Right Key


# Welcome 'Splash Screen' message
def splash_screen(point=0):
    """Display Splash Screen 'Breakout' message at start of the game"""
    splash = Turtle()               # Initialise Turtle object
    splash.hideturtle()             # Stop displaying turtle object on screen
    splash.penup()                  # Ensure turtle isn't drawing on screen yet
    splash.speed(0)                 # Turn off any updating delays

    splash.color("white")                                       # Set message text colour to white
    splash.setposition(0, -50)                                  # Set position of splash screen welcome message
    splash.write("BREAKOUT", align="center", font=FONT_SPLASH)  # Set display font
    screen.update()                                             # Update screen for user to see splash message
    time.sleep(1)                                               # Keep on screen for 1 second
    splash.clear()                                              # Clear splash screen message


# Initialise game loop
game_on = True                      # Set game looping variable for continuous loop
splash_screen()                     # Display splash screen welcome message
while game_on:                      # Start continuous game loop until someone wins!

    # Continuously move ball
    ball.move()                     # Move ball forward in set movement direction based on game rules

    # Check for collision with Player Paddle
    if ball.ycor() <= -200 and p1.distance(ball) < 40:
        ball.y_dir = 1                  # Bounce ball back up
        time_delay *= 0.9               # Increase speed by 10%
        screen.update()                 # Update screen for user
        ball.move()                     # Move ball back


    # Check for collision with a brick
    for brick in brick_manager.all_bricks:  # Loop through all bricks
        if ball.distance(brick) < 14:        # Check if ball hits a brick
            if brick.active == 1:
                ball.bounce()                   # Bounce ball vertically
                p_score += 1                    # Add 1 to player score
                scoreboard.refresh(p_score)     # Refresh scoreboard
                brick.color("black")            # Set brick to be invisible
                brick.active = 0                # Set brick to be inactive
                screen.update()                 # Update screen

    # Check if Player lost
    if ball.ycor() < -250:          # Check if ball crossed bottom of screen
        scoreboard.game_over()      # Show updated score on screen

    # Update screen
    time.sleep(time_delay)              # Pause game to facilitate visual animation
    screen.update()                     # Update screen

screen.exitonclick()                    # Keep game on screen until user clicks on the screen