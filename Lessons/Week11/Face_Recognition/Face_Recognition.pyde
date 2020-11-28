# Image Processing
# Simple Face Recognition
# Author: Kavan Lam
# Date: Nov 28,2020

detect_face = True

def setup():
    global base_img
    global test_img
    
    size(100, 100)
    base_img = loadImage("Base.png")
    test_img = loadImage("Test1.png")
    
def draw():
   global detect_face 
   
   if detect_face == True:
       detectFace()  # We should only do this one time
       detect_face = False

def detectFace():
    global base_img
    global test_img
    
    # We need to now load in the pixels
    base_img.loadPixels()
    test_img.loadPixels()
    
    # Calculate the Sum of Squared Differences
    for index in range(len(base_img.pixels)):
        # We will save this for next class







"""
Helpful Functions and notes
1) createImage(200,200,RGB) -- Create blank color image
2) loadImage("file.jpg")
3) image(img, locx, locy, sizex, sizey)
4) tint(brightness, alpha) or tint(R, G, B, alpha)
5) loadPixels() -- loads the pixels from the object to the pixels array
6) updatePixels() -- update the object with the pixels inside the pixels array
7) The pixels array in 1D (so 2D projected onto 1D)
8) Because of 7, location = x + (y * width). Width is left to right
9) color(greyscale value 0-255) or color(R, G, B)
10) use red(), green(), blue() to extract components from color
11) constrain(x,0,255) -- make x between 0 and 255
12) brightness(img.pixels[loc]) -- gives a num from 0 to 255 that represents the brightness of a pixel


def setup():
    global img
    size(472, 314)
    img = loadImage("girl.JPG")
    
# Edge Detection
def draw():
    # We are going to look at both image's pixels
    img.loadPixels()
    img_new = createImage(img.width,img.height,RGB)
    img_new.loadPixels()
    
    threshold = 10
    
    for x in range(img.width):
        for y in range(img.height):
            # Pixel location and color
            loc = x + y*img.width
            pix = img.pixels[loc]
    
            # Pixel to the left location and color
            leftLoc = (x-1) + y*img.width
            leftPix = img.pixels[leftLoc]
            
            # Pixel to the top location and color
            topLoc = x + ((y-1)*img.width)
            topPix = img.pixels[topLoc]
    
            # New color is difference between pixel and left neighbor
            diff1 = abs(brightness(pix) - brightness(leftPix))
            diff2 = abs(brightness(pix) - brightness(topPix))
            diff = (diff1 + diff2) // 2
            if diff > threshold:
                img_new.pixels[loc] = color(diff *10)
            else:
                img_new.pixels[loc] = color(0)
    
    # We changed the pixels in destination
    img_new.updatePixels()
    # Display the destination
    image(img_new,0,0)
"""
