# Python Focus Learning
# List Review
# Author: Kavan Lam
# Date: July 4, 2020

# Lets start of with the basic operations/functionalities for List
x = [50, 60, 10, 10, 50, 6, 9]
print(x[0])
print(x[3])
print(x[-1])
print(x[0:5])
print(x)
x[5] = 60
print(x)
print("-------------------------------------------")


# There are many functions and methods that we can use when it comes to a List. Lets see some of these
print(len(x))
print(max(x))
print(min(x))
x.sort()
print(x)
print("---------------------------------------")

# Lets see how we can loop over Lists using loops
# Lets start with for loops
for num in x:
    print(num)

print("-----------------------------------------")

# Lets now do it using a while loop
index = 0
while index < len(x):
    print(x[index])
    index = index + 1


# Alright now lets use what we learned to split a List of Strings and ints into a List of just Strings and another List of just ints
y = [1, 4, 6, "Kavan", "John", 50, "Kelly"]
names = []
numbers = []
for thing in y:
    if type(thing) == type("string"):
        names.append(thing)
    else:
        numbers.append(thing)

print(names)
print(numbers)    

print("-----------------------------------------")
# There is also this call method you can use on Strings called split
x = "Hello world life is so cool"
y = x.split(" ")
print(y[-1])
