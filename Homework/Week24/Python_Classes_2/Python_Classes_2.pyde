# Focus Learning: Python Level 2
# Python Classes
# Kavan Lam
# Feb 19, 2021

"""
Alright now lets see another example of Python Classes. This time we will see an example
from the health care field. There will be multiple classes and they will all interact with
each other in some way. Lets first describe the problem we are trying to model then we will
create the required classes.
"""

"""
When working with multiple classes in different file make sure you save all your work before
running the code otherwise you will encounter issues.
"""

from Virus import *
from Person import *
from Hospital import *

# Create the viruses
ebola = Virus("Ebola", True, 1000)
covid = Virus("Covid", True, 2000)
lump = Virus("Lump", False, 1500)
bump = Virus("Bump", False, 1000000)

# Create the people
john = Person("John", 19, "Male")
kelly = Person("Kelly", 13, "Female")
bob = Person("Bob", 50, "Male")
mia = Person("Mia", 10, "Female")
sam = Person("Sam", 20, "Male")

# Infect people
john.infect(ebola)
john.infect(covid)
john.infect(lump)
print(john)

kelly.infect(lump)

bob.infect(lump)
bob.infect(covid)

sam.infect(bump)

# Create the hospital and buy cures
print("----------------------------------------")
hs = Hospital("GG HS", 4000)
hs.buy_cure(lump)
hs.buy_cure(covid)
hs.buy_cure(ebola)
hs.buy_cure(bump)

# Admit the people to the hospital
print("----------------------------------------")
hs.admit_patient(john)
hs.admit_patient(kelly)
hs.admit_patient(bob)
hs.admit_patient(mia)
hs.admit_patient(sam)

# Lets see what the hospital looks like right now
print("----------------------------------------")
hs.get_all_info()

# Now lets process the patients
print("----------------------------------------")
hs.process_patients()

# Finally lets see what the hospital looks like right now
print("----------------------------------------")
hs.get_all_info()
