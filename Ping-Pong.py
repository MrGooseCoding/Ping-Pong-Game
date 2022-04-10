import turtle
import random
from time import sleep

# Ball class
class ball(turtle.Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.penup()
        self.shape('circle')
        self.goto(0, 0)
        self.dx = 1
        self.dy = 1
        self.speed(0)
        self.color('white') 

# Paddle class
class paddle(turtle.Turtle):
    def __init__(self, side):
        super().__init__()
        self.state = None
        self.penup()
        self.shape('square')
        self.goto(-360 if side == 'left' else 360, 0)
        self.color('white')
        self.shapesize(5, 1)
        return

    def up(self):
        if self.state == 'Up':
            y = self.ycor()
            self.goto(self.xcor(), y+2)
            pass

    def down(self):
        if self.state == 'Down':
            y = self.ycor()
            self.goto(self.xcor(), y-2)
            pass

    def change_state_up(self):
        self.state = 'Up'

    def change_state_down(self):
        self.state = 'Down'

    def change_state_none(self):
        self.state = None

wn = turtle.Screen()
wn.title("Pong by @MrGooseCoding")
wn.setup(height=600, width=800)
wn.bgcolor('black')
wn.tracer(0, 0)
paddle_a = paddle('left')
paddle_b = paddle('right')
ball = ball()

# Loop
while True:
    wn.listen()
    # Listening for the key press
    wn.onkeypress(paddle_a.change_state_up, 'w')
    wn.onkeyrelease(paddle_a.change_state_none, 'w')
    wn.onkeypress(paddle_a.change_state_down, 's')
    wn.onkeyrelease(paddle_a.change_state_none, 's')
    paddle_a.up()
    paddle_a.down()
    wn.onkeypress(paddle_b.change_state_up, 'Up')
    wn.onkeyrelease(paddle_b.change_state_none, 'Up')
    wn.onkeypress(paddle_b.change_state_down, 'Down')
    wn.onkeyrelease(paddle_b.change_state_none, 'Down')
    paddle_b.up()
    paddle_b.down()
    
    # Moving the ball
    ball.sety(ball.ycor() + ball.dy)
    ball.setx(ball.xcor() + ball.dx)

    #Border Checking
    if ball.ycor() > 290:
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.dy *= -1

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1

    # Collisions
    if (ball.xcor() > 340 and ball.xcor() < 350 and(ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() -50)):
        ball.setx(340)
        ball.dx *= -1 if ball.ycor() > paddle_b.ycor() -10 and ball.ycor() < paddle_b.ycor() +10 else -1*random.randrange(5, 15)/10
    
    if (ball.xcor() < -340 and ball.xcor()>-350 and(ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() -50)):
        ball.setx(-340)
        ball.dx *= -1 if ball.ycor() > paddle_a.ycor() -10 and ball.ycor() < paddle_a.ycor() +10 else -1*random.randrange(5, 15)/10

    wn.update()