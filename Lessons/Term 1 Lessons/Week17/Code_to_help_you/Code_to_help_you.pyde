"""
x = [100, 200]
y = [200, 700]

if len(x) > 0:
    x.pop()
    y.pop()

print(x)
print(y)
"""


# Drawing the circles
x = [100, 200]
y = [200, 700]
R = [255, 255]
G = [0, 255]
B = [0, 0]
radius = [10, 50]
move_x = [-1, 6]
move_y = [5, -2]

def setup():
    size(900, 900)
    
def draw():
    background(255, 255, 255)
    
    # Loop over all the circles
    # DRAW CIRCLES
    for index in range(0, len(x)):
        # Draw one of the circles
        pushStyle()
        fill(R[index], G[index], B[index], 100)
        ellipse(x[index], y[index], radius[index], radius[index])
        popStyle()
    move_circles()
        
def move_circles():
    global x
    global y
    global move_x
    global move_y
    for index in range(0, len(x)):
        x[index] = x[index] + move_x[index]
        y[index] = y[index] + move_y[index]
        
        
        
