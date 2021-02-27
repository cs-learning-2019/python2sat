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
print("-----------------------------------")
def question1(n):
    temp = math.sqrt(n)
    temp_round_down = math.floor(temp) ** 2 # or int(temp)
    temp_round_up = math.ceil(temp) ** 2
    if n - temp_round_down < temp_round_up - n:
        return temp_round_down
    else:
        return temp_round_up
        
print(question1(27)) # should print 25
print(question1(17)) # should print 16
print(question1(25)) # should print 25

# Question 2
print("-----------------------------------")
def question2(n):
    temp = n / 5
    temp_round_down = math.floor(temp) * 5 # or int(temp)
    temp_round_up = math.ceil(temp) * 5
    if n - temp_round_down < temp_round_up - n:
        return temp_round_down
    else:
        return temp_round_up
    
print(question2(17))  # should print 15
print(question2(35))  # should print 35
print(question2(36))  # should print 35

# Question 3
print("-----------------------------------")
def question3(n):
    number_of_full_rows = n // 5
    left_over = n % 5
    
    for i in range(number_of_full_rows):
        print("XXXXX")
    
    print("X" * left_over)

question3(17)

# Question 4
print("-----------------------------------")
def question4(n):
    print("Who's turn is it")
    print(">" + str(n))
    
    print("It is team " + str(-1 * n + 11) + "'s turn")
    
question4(7) 

# Question 5
print("-----------------------------------")
def question5(n):
    if n == 2:
        print("Prime")
        return None
    elif n == 1:
        print("Not Prime")
        return None
        
    for i in range(2, n):
        if n % i == 0:
            print("Not Prime")
            return None
    
    print("Prime")
    
question5(10) 


# Question 6 HW
print("-----------------------------------")
def question6(binary_string):
    #binary_string = "0111"
    #pieces = list(binary_string)
    
    total_num = 0
    exponent = 0
    binary_string = binary_string[::-1]
    for bit in binary_string:
        if bit == "1":
            total_num = total_num + (2 ** exponent)
        exponent = exponent + 1
    
    return total_num
        
print(question6("0111"))  # Should print 7
print(question6("00010")) # Should print 2
print(question6("00011")) # Should print 3

# Question 7 HW
print("-----------------------------------")
def question7(n):
    # Find the largest exponent possible
    exponent = 0
    while(2 ** exponent <= n):
       exponent =  exponent + 1
    exponent = exponent - 1 
    
    # Now find the binary string
    string = ""
    while (n > 0):
        if n - (2 ** exponent) >= 0:
            n = n - (2 ** exponent)
            string = string + "1"
        else:
            string = string + "0"
        exponent = exponent - 1 
    
    return string
print(question7(7))  # Should print 111
print(question7(2)) # Should print 1
print(question7(13)) # Should print 1101
    

# Question 8 HW
print("-----------------------------------")
def question8(x, y):
    x_divisors = []
    for i in range(1, x+1):
        if x % i == 0:
            x_divisors.append(i)
    
    y_divisors = []
    for i in range(1, y+1):
        if y % i == 0:
            y_divisors.append(i)
            
    y_divisors.reverse()
    x_divisors.reverse()
    
    if x < y:
        for num in x_divisors:
            if num in y_divisors:
                return num
    else:
        for num in y_divisors:
            if num in x_divisors:
                return num
        
    
print(question8(7, 6))  # Should print 1
print(question8(2, 4)) # Should print 2
print(question8(10, 5)) # Should print 5
    
    
    
    
    
    
    
