# Focus Learning: Python Level 2
# Numbers worksheet
# Kavan Lam
# Oct 3, 2020

# Find for strings
# Find will return -1 if it can not find what you are looking for
print("Jelly Byean".find("7"))  # Gives the index of the first "y" in the string

# Replace is helpful to change the string
print("Jelly Bean".replace("e", "lol"))

# We can index into a string [Start, End, Skip/Jump]
word = "Jelly Beans"
print(word[3:9:2])

# String Exercises
# Q1
print("---------------------------------------")
def question1(word):
    print(word.upper() + word.lower())

question1("ABC")

# Q2
# 1) No spaces
# 2) Needs to have @ and a .com or .ca
# 3) The .com or .ca must come after the @
# 4) No special characters  *{}[]&^%!/~
print("---------------------------------------")
def question2(email):
    # Test 1
    if email.find(" ") != -1:
        print(email + " is not a valid email")
        return  # get out of the function we are done
    
    # Test 2
    if email.find("@") == -1:
        print(email + " is not a valid email")
        return
    else:
        if email.find(".com") == -1 and email.find(".ca") == -1:
            print(email + " is not a valid email")
            return
    
    # Test 3
    if email.find(".com") == -1:
        if email.find(".ca") < email.find("@"):
            print(email + " is not a valid email")
            return
    else:
        if email.find(".com") < email.find("@"):
            print(email + " is not a valid email")
            return
    
    # Test 4
    bad = "*{}[]&^%!/~"
    for bad_chr in bad:
        if bad_chr in email:
            print(email + " is not a valid email")
            return
    
    
    print(email + " is a valid email")
    
question2("youa&recool@gmail.com")


# Q3
print("---------------------------------------")
def question3(word):
    num_of_a = word.count("A") + word.count("a") 
    print("The number of a's in " + word + " is " + str(num_of_a))

question3("I am so cool aa A Allo")



# Q4
print("---------------------------------------")
def question4(word):
    new_word = word.replace("a", "")
    print(new_word)
    
question4("aabbAABBcder")

    
