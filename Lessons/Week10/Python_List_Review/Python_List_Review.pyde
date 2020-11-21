# Python Focus Learning
# List and Dictionary Review
# Author: Kavan Lam
# Date: Nov 21, 2020

################## LIST ##################
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
# Do not be afriad to search up different functions and methods for list

# Lets see how we can loop over Lists using loops
# Lets start with for loops
for num in x:
    print(num)

# Print a list in reverse
print("---------------------------------------")
x.reverse()
print(x)

# Make a new list using only the even index from original list
print("---------------------------------------")
original = [4, 5, 77, 99, 12, 0, 3]
new_list = []
for index in range(0, len(original)):
    if index % 2 == 0:
        new_list.append(original[index])  # append will add the new thing into the list
print(new_list)

# Take a list of numbers and break it down into two list. First list contains all numbers that are less than the average. Second list contains all other numbers.
print("---------------------------------------")
original = [4, 5, 77, 99, 12, 0, 3]
first_list = []
second_list = []
average_orig = sum(original) / len(original)
for number in original:
    if number < average_orig:
        first_list.append(number)
    else:
        second_list.append(number)
print("The average is " + str(average_orig))
print("The first list is " + str(first_list))
print("The second list is " + str(second_list))


# Often times we will have to deal with 2D list (for example a greyscale image)
# Lets see a simple example of a 2D list and how to index into it
print("---------------------------------------")
x = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(x[1][2])
print(x[-1][-1])

# Now lets see how we can find the transpose of a 2D list of numbers assuming the number of rows equals to the cols
# The transpose is taking all the rows and converting it into cols 
print("---------------------------------------")
x = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
row1 = []
row2 = []
row3 = []

for sublist in x:
    row1.append(sublist[0])
    row2.append(sublist[1])
    row3.append(sublist[2])

new_x = [row1, row2, row3]
print(new_x)


# Lets see an example of where a 2D list can be helpful to organize data
# We have a school with many classes and each class have a list of student names
# So each sublist will represent one class
# Our goal is to find which class has the most students.
print("---------------------------------------")
classes = [["Ho", "Yo"], ["Bob", "Kim", "Du"], ["Lee"], ["Abby", "Kid", "Ho", "Yo"]]
most_students = 0
most_index = 0

classroom_number = 1
for classroom in classes:
    if len(classroom) > most_students:
        most_students = len(classroom)
        most_index = classroom_number
    
    classroom_number = classroom_number + 1

print("Classroom number " + str(most_index) + " has the most students " + str(most_students))

# What about a 3D list? Can anyone think of an example of a 3D list being used?
# One example of 3D list is color images

# Alright so 1D lists are actual a lot more powerful than you think. In fact we can use them to 
# represent something called vectors. What are vectors you ask?
# Lets calculate the dot product between two vectors
print("---------------------------------------")
x = [1, 2, 3]
y = [4, 5, 0]
answer = 0
for i in range(3):
    answer = answer + (x[i] * y[i])
    
print("The dot product is " + str(answer))
    
# Lets do the sum of the differences
x = [2, 5, 6]
y = [1, 3, 4]
answer = 0
for i in range(3):
    answer = answer + (x[i] - y[i])
    
print("The sum of differences is " + str(answer))

# Hmmmm what can we do with this?
# We can actually get a very simple object detection
# For example we can do faces!

# We are going to do a project on this very soon


################## Dictionary ##################
# Again lets see some basic operations with dictionaries and see how they work
print("------------------------------------------------")
x = {"Bob": 10, "Stacy": 11, "John": 13}  # We no longer use index, instead we use the keys
print(x["Stacy"])
print(x["John"])
print("Johnny" in x)
# print(x["jahn"])  # You need to make sure the key exist
x["Yu"] = 35
x["John"] = 12
del x["Bob"]
print(x)
# In a Python Dictionary the keys are not allowed to be repeated

# Convert a list of names into a dictionary where the values are the frequencies
print("------------------------------------------------")
names = ["Ho", "John", "Cat", "Dog", "John", "Ho", "Cat", "John"]
def convertToDictionary(names):
    result = {}
    for name in names:
        if name in result:
            result[name] = result[name] + 1
        else:
            result[name] = 1
    
    print(result)

convertToDictionary(names)

# Remove all the duplicates from a list using a dictionary
print("------------------------------------------------")
names = ["Ho", "John", "Cat", "Dog", "John", "Ho", "Cat", "John"]
def removeDuplicate(names):
    result = {}
    for name in names:
        if name in result:
            result[name] = result[name] + 1
        else:
            result[name] = 1
    
    print(result.keys())   # .keys will give you a list of all the keys

removeDuplicate(names)

# Given two dictionaries combine them into one (both dictonaries are str-int pairs)
print("------------------------------------------------")
d1 = {"A" : 2, "B": 3, "C": 10}
d2 = {"C": 2, "A": 3, "D": 2}
def combineDictionary(d1, d2):
    for d2_key in d2.keys():
        if d2_key in d1:
            d1[d2_key] = d1[d2_key] + d2[d2_key]
        else:
            d1[d2_key] = d2[d2_key]
    
    print(d1)

combineDictionary(d1, d2)

# Given a dictonary convert it into a list (just use the values)
print("------------------------------------------------")
d = {"A" : 2, "B": 3, "C": 10, "D": 2}
def convertToList(d):
    return d.values()

print(convertToList(d))


# How can we check to see if a key is in a dictionary?
print("------------------------------------------------")
d = {"A" : 2, "B": 3, "C": 10, "D": 2}
def isInDictionary(d, targetKey):
    return (targetKey in d)

print(isInDictionary(d,  "Z"))


# How can we check to see if a value is in a dictionary?
print("------------------------------------------------")
d = {"A" : 2, "B": 3, "C": 10, "D": 2}
def isValueInDictionary(d, targetValue):
    return (targetValue in d.values())
    
print(isValueInDictionary(d,  10))


# In processing we can use it to create and store a map of different colors
colors = {"Red": (255, 0, 0), "Green": (0, 255, 0), "Blue":(0, 0, 255), "Yellow": (255, 255, 0), "Random": (125, 6, 90)}
def setup():
    size(900, 900)

def draw():
    fill(colors["Random"][0], colors["Random"][1], colors["Random"][2])  # colors["Green"]  ---> (0, 255, 0)  then (0, 255, 0) [1] --> 255
    # fill(0, 255, 0)
    rect(50, 50, 100, 100)

# Dictionaries have many real world applications
# 1) Transfering information
# 2) Phone look up
# 3) Lets take a look at google chrome inspector
# Can you think of any more?
