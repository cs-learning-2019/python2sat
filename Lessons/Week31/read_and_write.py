# Reading and writing text files in Python

print("Please enter your name")
name = input()

file = open("demo_file.txt", "w")
file.write(name)
file.close()


file = open("demo_file.txt", "r")
name = file.readline()
print("The name you set from before is: " + name)
