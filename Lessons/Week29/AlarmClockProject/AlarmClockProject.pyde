# Focus Learning Python Level 2
# Alarm Clock Project
# Kavan Lam
# May 6, 2021

from Clock import * 
from AlarmClock import *

mode = 1  # 1 -> Clock  -1 -> Alarm Clock
setting = 0  # 0->Hour  1->Min  2->Sec  3->AM_PM  4->Month  5->Day  6->Year  
clock = Clock()
alarmClock = AlarmClock()

def setup():
    global font1
    
    size(800, 500)
    font1 = loadFont("BodoniMT-48.vlw")

def draw():
    global mode
    
    if mode == 1:
        draw_clock()
    else:
        draw_alarm_clock()
   
def draw_clock():
    global clock
    global font1
    global setting
    
    # Update the time
    clock.update_time()
    
    # Clear the previous frame and set the background
    if clock.is_afternoon():
        background(0, 0, 200)
    else:
        background(200, 250, 0)
    
    # Draw the time and date
    pushStyle()
    textAlign(CENTER)
    fill(0, 0, 0)
    textFont(font1, 70)
    text(clock.Hour + ":" + clock.Min + ":" + clock.Sec + " " + clock.AM_PM, 400, 200)
    text(clock.Month + " " + clock.Day + ", " + clock.Year, 400, 300)
    popStyle()
    
def draw_alarm_clock():
    global clock
    global alarmClock
    global font1
    
    # Update the time
    clock.update_time()
    
    # Clear the previous frame and set the background
    background(0, 0, 0)
    
    # Draw the time and date
    pushStyle()
    textAlign(CENTER)
    fill(255, 0, 0)
    textFont(font1, 30)
    text("Current Time", 700, 40)
    text(clock.Hour + ":" + clock.Min + ":" + clock.Sec + " " + clock.AM_PM, 700, 80)
    text(clock.Month + " " + clock.Day + ", " + clock.Year, 700, 120)
    popStyle()
    
    # Draw circle
    pushStyle()
    fill(0, 255, 0)
    ellipse(300, 230, 420, 420)
    popStyle()
    
    # Check alarm
    if alarmClock.isAlarmClockSet():
        result = alarmClock.timeTargetReached()
        if result[0] == True:
            print("Boom")
            alarmClock.stopAlarm()
        else:
            # Draw circle
            pushStyle()
            fill(0, 0, 255)
            radius = result[1] * 420
            ellipse(300, 230, radius, radius)
            popStyle()
    
    # Draw the alarm time and date
    pushStyle()
    textAlign(CENTER)
    fill(255, 255, 0)
    textFont(font1, 70)
    text("Alarm Time", 300, 150)
    text(alarmClock.Hour + ":" + alarmClock.Min + ":" + alarmClock.Sec + " " + alarmClock.AM_PM, 300, 230)
    text(alarmClock.Month + " " + alarmClock.Day + ", " + alarmClock.Year, 300, 310)
    popStyle()
    
    # Draw a line accroding to setting
    pushStyle()
    stroke(255, 0, 0)
    strokeWeight(3)
    if setting == 0:
        line(120, 235, 180, 235)
    elif setting == 1:
        line(210, 235, 270, 235)
    elif setting == 2:
        line(300, 235, 360, 235)
    elif setting == 3:
        line(390, 235, 480, 235)
    elif setting == 4:
        line(100, 335, 220, 335)
    elif setting == 5:
        line(250, 335, 320, 335)
    elif setting == 6:
        line(350, 335, 480, 335)
    popStyle()
    
        
    
def keyPressed():
    global mode
    global setting
    
    if key == "T" or key == "t":
        mode = mode * -1
        if mode == -1:
            alarmClock.update_time()
    
    # We need to check for arrow key usage in alarm mode
    if mode == -1:
        if not alarmClock.isAlarmClockSet():
            if keyCode == RIGHT:
                setting = (setting + 1) % 7
            elif keyCode == UP:
                if setting == 0:
                    alarmClock.increaseHour()
                elif setting == 1:
                    alarmClock.increaseMin()
                elif setting == 2:
                    alarmClock.increaseSec()
                elif setting == 3:
                    alarmClock.toggle_AM_PM()
                elif setting == 4:
                    alarmClock.increaseMonth()
                elif setting == 5:
                    alarmClock.increaseDay()
                elif setting == 6:
                    alarmClock.increaseYear()
        
        if keyCode == 32:  # Space bar
            if alarmClock.isSet == False:
                alarmClock.startAlarm()
            else:
                alarmClock.stopAlarm()
        
        
