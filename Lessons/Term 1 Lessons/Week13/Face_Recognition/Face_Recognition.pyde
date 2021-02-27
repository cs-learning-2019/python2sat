# Image Processing
# Simple Face Recognition
# Author: Kavan Lam
# Date: Dec 12, 2020

detect_face = True
ssd_threshold = 19000000  # The ssd must not pass this value
ncc_threshold = 0.7  ###### YOU MIGHT WANT TO CHNAGE THE THRESHOLD

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
    global ssd_threshold
    
    # We need to now load in the pixels
    base_img.loadPixels()
    test_img.loadPixels()
    
    """
    # Calculate the Sum of Squared Differences (SSD)
    ssd = 0  # If the ssd is very big then the images are not the same
    for index in range(len(base_img.pixels)):
        brightness_base_px = brightness(base_img.pixels[index])
        brightness_test_px = brightness(test_img.pixels[index])
        diff = brightness_base_px - brightness_test_px
        sqaure_diff = diff * diff
        ssd = ssd + sqaure_diff
    if ssd <= ssd_threshold:
        print("Same person")
    else:
        print("Not the same person")
    """
    
    # Now try to use NCC and tell my if it is the same person or not
        
        
        
""" EXTRA TIPS
print(sqrt(174))   You can calculate the square root using the sqrt function

Do not forget to convert number to float before dividing otherwise you might get zero  For example, print(float(16) / float(17))
"""
