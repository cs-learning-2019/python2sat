# Focus Learning
# Python Level 2 Particle Motion Homework
# Feb 12, 2021
# Kavan Lam

# Below is the solution to the first question. There is no solution to the second question.

import math

x = 50
y = 400

def setup():
    size(1100, 900)
    
def draw():
    global x
    global y
    
    # Clear the previous frame
    background(0, 0, 0)
    
    # Adjust the axis so that (0, 0) is in the bottom left
    scale(1, -1)
    translate(0, -900)
    
    # Draw the ball
    ellipse(x, y, 50, 50)
    
    # Move the ball
    x = x + 1
    y = equation(x)
    
    
def equation(x):
    y = 100 * math.sin(x/10.0) + 0.8*x
    return y
