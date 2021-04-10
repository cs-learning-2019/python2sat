import datetime as dt

"""
# Question 1
def future_30():
    current_time = dt.datetime.now()
    delta = dt.timedelta(minutes=30)
    new_time = current_time + delta
    print(new_time)
    print(new_time.time())
    print(new_time.strftime("%I:%M%p"))
    
future_30()
"""

"""
# Question 2
print("----------------------------------------")
def day_message():
    current_time = dt.datetime.now()
    day_name = current_time.strftime("%A")
    print("Today is " + day_name)
    if day_name == "Monday":
        print("Sad message")
    elif day_name == "Friday":
        print("Happy message")
    else:
        print("ok day")
    
day_message()

"""

# Question 3
print("----------------------------------------")
start_time = dt.datetime.now()
frames = 0
done = False

def setup():
    size(900, 900)
    frameRate(60)
    print("The target frame rate is " + str(frameRate))

def draw():
    global frames
    global start_time
    global done
    
    rect(100, 100, 200, 200)

    frames += 1
    end_time = dt.datetime.now()
    delta_time = end_time - start_time
    if delta_time.total_seconds() >= 1 and done == False:
        print("The measured or actual frame rate is " + str(frames))
        done = True
