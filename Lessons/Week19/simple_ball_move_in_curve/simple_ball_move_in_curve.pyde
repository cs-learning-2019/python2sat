# Simple example
x_ball = 0
y_ball = 0

def setup():
    size(900, 900)
    
def draw():
    global x_ball
    global y_ball
    # Make sure that (0, 0) is in the bottom left corner, (900, 900) will be the top right corner
    scale(1, -1)
    translate(0, -900)
    
    # Clear the previous frame
    background(0, 0, 0)
    
    # Draw the ball
    ellipse(x_ball, y_ball, 50, 50)
    
    # Move the ball
    x_ball = x_ball + 10
    y_ball = equation(x_ball)
    
def equation(x):
    y = x * x * 0.001
    return y
