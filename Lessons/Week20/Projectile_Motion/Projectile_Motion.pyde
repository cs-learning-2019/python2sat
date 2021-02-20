# Focus Learning Python Level 2
# Projectile Motion
# Kavan Lam
# Feb 20, 2021

x = 0
y = 0

def setup():
    size(1000, 1000)

def draw():
    global x
    global y
    
    scale(1, -1)
    translate(0, -900)
    
    # Clear the previous frame
    background(0, 0, 0)
    
    # Draw the ball
    ellipse(x, y, 50, 50)
    
    # Move the ball
    x = x + 2
    y = move_equation(x)
    
def move_equation(x):
    #y = ((-3 * (x ** 2) + (3 * x)) * 0.001) + 500  # Ball drops from gravity
    y = ((-4.9 * (x ** 2) + (4000 * x)) * 0.001)  # Ball flyies through the air
    #y = 50 * sin(x/10.0) + 500  # How to move in a wave
    return y
    
    
