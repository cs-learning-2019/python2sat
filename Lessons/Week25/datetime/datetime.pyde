# https://docs.python.org/3/library/datetime.html   <---- Look here 
import datetime

x = datetime.datetime.now()
print(x)
print(x.hour)
print(x.second)
print(x.microsecond)
print(x.strftime("%A"))

print("---------------------------------")
z = datetime.datetime.now()
diff = z - x  # diff is of type timedelta
print(diff.total_seconds())  

print("---------------------------------")
y = datetime.date.today()
print(y)






"""
# How can you comapre two python list when order does not matter
# 1) Sort both python list and then compare using ==
# 2) You can search for each name in x and see if it is in y. This only works if there are no duplicate names.
# 3) Use dictionaries or sets

x = ["john", "kelly", "bob", "sir"]
y = ["bob", "sir", "kelly",  "john", "sir"]
a = {}
b = {}
for index in range(len(x)):
    if x[index] in a:
        a[x[index]] = a[x[index]] + 1
    else:
        a[x[index]] = 1

for index in range(len(y)):
    if y[index] in b:
        b[y[index]] = b[y[index]] + 1
    else:
        b[y[index]] = 1

if a == b:
    print("They are the same")
else:
    print("They are different")

# Extra code (rough work)
x = ["john", "kelly", "bob", "sir"]
y = ["bob", "sir", "kelly",  "john"]

if x == y:
    print("They are the same")
else:
    print("They are different")
   

a = {"john", "kelly", "bob", "sir"}
b = {"bob", "sir", "kelly",  "john"}

if a == b:
    print("They are the same")
else:
    print("They are different")
"""
