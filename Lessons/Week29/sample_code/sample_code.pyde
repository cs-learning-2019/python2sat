import datetime as dt
add_library("minim")

section = 1

def setup():
    global minim
    global bomb_sound_effect
    global dog
    
    size(600, 600)
    
    # Load in sound effects
    minim = Minim(this)
    bomb_sound_effect = minim.loadFile("Bomb.wav")
    
    # Load in images
    dog = loadImage("dog.jpg")

def draw():
    global bomb_sound_effect
    global section
    
    background(255, 0, 255)
    
    if section == 1:
        section1()
    else:
        section2()
    
def section1():
    # Part 1 --- Simple time and date
    current_time = dt.datetime.now()
    current_month = current_time.strftime("%B")
    current_seconds = current_time.strftime("%S")
    current_min = current_time.strftime("%M")
    
    textSize(30)
    text(current_seconds, 200, 200)
    text(current_month, 100, 300)
    text(current_min, 100, 200)
    
    bomb_sound_effect.setGain(-30)  # Decrease the volume of the sound effect
    bomb_sound_effect.play()
    
    tint(255, 130, 190, 255)  # Use the last number to change the transparency
    image(dog, 100, 400, 200, 100)

def section2():
    # Part 2 --- Alarm Clock
    pass
    

def keyPressed():
    global section
    
    if key == "T" or key == "t":
        if section == 1:
            section = 2
        else:
            section = 1
            
def mousePressed():
    # You only need this for section 2
    pass







    
    
    
