# Image Processing
# Simple Face Recognition
# Author: Kavan Lam
# Date: Dec 5, 2020

detect_face = True
threshold = 19000000  # The ssd must not pass this value

def setup():
    global base_img
    global test_img
    
    size(100, 100)
    base_img = loadImage("Base.png")
    test_img = loadImage("newTest1.jpg")
    
def draw():
   global detect_face 
   
   if detect_face == True:
       detectFace()  # We should only do this one time
       detect_face = False

def detectFace():
    global base_img
    global test_img
    global ssd
    
    # We need to now load in the pixels
    base_img.loadPixels()
    test_img.loadPixels()
    
    # Calculate the Sum of Squared Differences
    ssd = 0  # If the ssd is very big then the images are not the same
    for index in range(len(base_img.pixels)):
        brightness_base_px = brightness(base_img.pixels[index])
        brightness_test_px = brightness(test_img.pixels[index])
        diff = brightness_base_px - brightness_test_px
        sqaure_diff = diff * diff
        ssd = ssd + sqaure_diff
        
    
    if ssd <= threshold:
        print("Same person")
    else:
        print("Not the same person")
