import turtle

window = turtle.Screen()
window.title('Pong clone')
window.bgcolor('black') #sets the background color of the window to black
window.setup(width=800, height=600) # The window will be 800 * 600
window.tracer(0) # speeds up the game by no self updating


# Score
score_a = 0
score_b = 0



# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0) # This is the speed of the animation, not the paddle speed
paddle_a.shape('square') # By default square is 20px x 20px
paddle_a.color('white')
paddle_a.shapesize(stretch_wid=5, stretch_len=1) # This makes the square be 5 times greater than the default and keeps the len equal
paddle_a.penup() # This means that the turtle doesn\'t draws when it moves
paddle_a.goto(-350, 0) # Initialize at x = -350 on the left side of the windows and y = 0 means it\'s centered


# Paddle B
paddle_b = turtle.Turtle() # This means that you are starting a Turtle object
paddle_b.speed(0)
paddle_b.shape('square')
paddle_b.color('white')
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)


# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape('square')
ball.color('white')
ball.penup()
ball.goto(0, 0)
ball.dx = 0.2 # dx is delta x
ball.dy = 0.2 # dy is delta y and move 2 px


# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write('Player A: 0 | Player B: 0', align='center', font=('Courier', 24, 'normal'))

# Functions to make the paddles move
def paddle_a_up():
    y = paddle_a.ycor() # ycor() comes from the turtle module and returns the turtle\'s y coordinates
    y += 20
    paddle_a.sety(y) # sety() sets the y coordinate of the turtle to the float or int you pass through


def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)


# keyboard binding
window.listen() # This makes the window to listen keyword inputs
window.onkeypress(paddle_a_up, 'w')
window.onkeypress(paddle_a_down, 's')
window.onkeypress(paddle_b_up, 'Up')
window.onkeypress(paddle_b_down, 'Down')

# Main game loop
while True:
    window.update()

    # move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    elif ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    elif ball.xcor() > 390:
        ball.goto(0, 0) # If you got a point, the ball will return to the center
        ball.dx *= -1
        score_a += 1
        pen.clear() # Clears the window so you can update scores
        pen.write(f'Player A: {score_a} | Player B: {score_b}', align='center', font=('Courier', 24, 'normal'))

    elif ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write(f'Player A: {score_a} | Player B: {score_b}', align='center', font=('Courier', 24, 'normal'))

    # Paddle and ball collissions

    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() -40):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
