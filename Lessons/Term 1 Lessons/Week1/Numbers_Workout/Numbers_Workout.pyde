# Python Level 2
# Numbers Workout/Worksheet
# Sept 12, 2020
# Kavan Lam

import math  # import the math package

# Ex 1
x = 5.89
print(int(x))

y = 4
print(float(y))

print(int(round(x)))
print(round(7.8234567890, 5))

# Watch out you can not turn everything into an int or float
z = "54a"
# print(int(z)) will not work


# Ex2
print("-----------------------------------")
print(3//2)
print(7 % 2)
print(3 ** 3)

# Ex3
print("-----------------------------------")
print(abs(-4))
print(round(54.5))
print(math.floor(6.2))
print(math.floor(6.9))
print(math.ceil(6.2))
print(math.ceil(6.0))  # No effect if the decimal part is zero
print(math.sqrt(16))

############### Practice Questions ###############

# Question 1  
# A square number something like 1, 4, 9, 16, 25, 36 ....
def question1(n):
    pass
    
print(question1(27)) # should print 25
print(question1(17)) # should print 16
print(question1(25)) # should print 25

# Question 2
def question2(n):
    pass
    
print(question2(17))  # should print 15
print(question2(35))  # should print 35
print(question2(36))  # should print 35
