# Focus Learning: Python Level 2
# Functions Review
# Author: Kavan Lam
# Date: Oct 24, 2020

# Let's see some simple example of functions and explain what they are
def simple(input1, input2):
    print("Starting simple function")
    print("The result is " + str(input1 + input2))
    print("Ending simple function")

simple("Kavan", "Lam")
print("----------------------------------")
simple(10, 5)
# simple(10, "Lam")  DO NOT DO THIS You can not add a int with a string



print("----------------------------------")
# Functions can sometimes be picky about what you give them
# You can use type() to get the data type of the inputs
def simple2(num):
    if type(num) == type(1) or type(num) == type(1.1):
        print(num + 5)
    else:
        print("Sorry you need to give me a number!")

simple2(5)
simple2("HHHH")



print("----------------------------------")
# Functions can also take in default values
def default(name1 = "John", name2 = "Silly"):
    print("Hi " + name1)
    print("Bye " + name2)

default("Kavan")



print("----------------------------------")
# Now let's take a look a functions calling other functions
def manager(num1, num2, num3 = 20.0):
    # We want to calculate ((2 * num1) + (num2 - num3) ** 2) / 5
    print((double_helper(num1) + exponent(num2, num3)) / 5.0)

def double_helper(x):
    return 2 * x

def exponent(y, z):
    return (y - z) ** 2

manager(1.0, 21.0)


# Finally lets see some hard examples of functions
# 1) Write a function that takes the information about a rect and one point and returns True if they intersect and False otherwise
print("----------------------------------")
def rect_intersect(x1, y1, l1, w1, x2, y2):
    if (x2 >= x1 and x2 <= x1 + l1) and (y2 >= y1 and y2 <= y1 + w1):
        return True
    else:
        return False
print(rect_intersect(10, 10, 40, 10, 25, 12))



print("----------------------------------")
# 2) Write a function to convert between KM and M
# 1km = 1000m
def KM_to_M(num_of_km):
    print(num_of_km * 1000)
KM_to_M(3.5)
