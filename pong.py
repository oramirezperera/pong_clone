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


# Main game loop
while True:
    window.update()