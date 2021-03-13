# Focus Learning: Python Level 2
# Classes HW 1 Solutions
# Kavan Lam
# Feb 11, 2021

# Question 1
"""
Object-oriented programming is a way of programming in which you think about software
as a collection of objects working together to accomplish something. It is very natural
for people to think about parts of software as different objects.
"""

# Question 2
class Car:
    def __init__(self, name, car_color, age):
        self.name = name
        self.car_color = car_color
        self.age = age
    
    def increase_age(self):
        self.age = str(int(self.age) + 1)

car1 = Car("Kia", "Red", "10")
car1.increase_age()
print(car1.age)

# Question 3
class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * (self.radius ** 2.0)
    
    def diameter(self):
        return 2.0 * self.radius
    
    def circumference(self):
        return 2.0 * 3.14 * self.radius
        
        
        
        
        
        
