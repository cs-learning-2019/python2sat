# Python Focus Learning
# List and Dictionary Review
# Author: Kavan Lam
# Date: Oct 31, 2020

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
# Do not be afriad to search up different functions and method for list

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


# Lets see an example of where a 2D list can be helpful to organize data
# We have a school with many classes and each class have a list of student names
# So each sublist will represent one class
# Our goal is to find which class has the most students and which class has the least. We also need the average number of students per class.



# What about a 3D list? Can anyone think of an example of a 3D list being used?
# One example of 3D list is ____________________


# Alright so 1D lists are actual a lot more powerful than you think. In fact we can use them to 
# represent something called vectors. What are vectors you ask?
# Lets calculate the dot product between two vectors

# Lets do the sum of the differences

# Hmmmm what can we do with this?
# We can actually get a very simple object detection
# For example we can do faces!


################## Dictionary ##################
# WE WILL DO THIS NEXT TIME #
# Again lets see some basic operations with dictionaries and see how they work
# Convert a list of names into a dictionary
