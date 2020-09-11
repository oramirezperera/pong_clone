import turtle

window = turtle.Screen()
window.title('Pong clone')
window.bgcolor('black') #sets the background color of the window to black
window.setup(width=800, height=600) # The window will be 800 * 600
window.tracer(0) # speeds up the game by no self updating

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