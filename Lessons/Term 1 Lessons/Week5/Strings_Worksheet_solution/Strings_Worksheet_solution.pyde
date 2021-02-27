# Focus Learning: Python Level 2
# Numbers worksheet
# Kavan Lam
# Oct 17, 2020

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

# Q5
print("---------------------------------------")
def question5(word):
    new_word = word[::-1]
    print(new_word)
    
question5("My Python Code")


# Q6
print("---------------------------------------")
def question6(word):
    word_len = len(word)
    
    # Lets get all the even characters
    even = word[::2]
    
    # Lets get all the odd characters
    odd = word[1::2]
    
    new_word = list(word)
    turn = 1
    for i in range(word_len):
        if turn == 1:
            new_word[i] = odd[0]
            odd = odd[1:]
        else:
            new_word[i] = even[0]
            even = even[1:]
        turn = turn * -1
    
    print("".join(new_word))
            
question6("python")

# Q7
print("---------------------------------------")
def question7(word):
    list_of_character = list(word)
    list_of_character.sort()
    print("".join(list_of_character))
    
question7("python")

# Q8
print("---------------------------------------")
def question8(word):
    if word == word[::-1]:
        return True
    else:
        return False
    
print(question8("racecar"))

# Q9
print("---------------------------------------")
def question9(word):
    # The first line
    print(word)
    
    # Fill in the middle lines
    middle_characters = word[1:-1]
    for i in range(len(middle_characters)):
        print(middle_characters[i] + (" " * len(middle_characters)) + middle_characters[len(middle_characters) - i - 1])
    
    # The last line
    print(word[::-1])
    
question9("Python")










    
