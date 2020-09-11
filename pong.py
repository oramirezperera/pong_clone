import turtle

window = turtle.Screen()
window.title('Pong clone')
window.bgcolor('black') #sets the background color of the window to black
window.setup(width=800, height=600) # The window will be 800 * 600
window.tracer(0) # speeds up the game by no self updating


# Main game loop
while True:
    window.update()