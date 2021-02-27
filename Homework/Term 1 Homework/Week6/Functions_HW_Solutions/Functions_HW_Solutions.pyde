# Focus Learning: Python Level 2
# Functions HW solutions
# Kavan Lam
# Oct 30, 2020

# Question 1
def circle_overlap(x1, y1, r1, x2, y2, r2):
    max_dist = r1 + r2  # The distance between the two circles must be less than or equal to this
    temp1 = (x1 - x2) ** 2.0
    temp2 = (y1 - y2) ** 2.0
    dist_between_centers = sqrt(temp1 + temp2)
    
    if dist_between_centers <= max_dist:
        print("Circles touching")
    else:
        print("Cicrles not touching")
        
circle_overlap(100, 100, 30, 150, 100, 20)
    
# Question 2
def q2(str1, str2):
    if len(str1) + len(str2) > 15:
        print("Strings too long")
    else:
        print("That is ok")
        
q2("Hello", "World")

# Question 3
def q3(x):
    num_of_prime = 0
    for num in str(x):
        temp = int(num)
        if is_prime(temp):
            num_of_prime += 1 
    
    return num_of_prime

def is_prime(number):
    if number == 0 or number == 1:
        return False
    
    for i in range(2, number):
        if number % i == 0:
            return False
    
    return True

print(q3(2345619))
    
