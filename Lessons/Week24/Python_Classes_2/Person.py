class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        self.virus = []

    def __str__(self):
        temp = "My name is " + self.name + " and I have...\n"
        for v in self.virus:
            temp = temp + str(v) + "\n"
        return temp
    
    def __eq__(self, person_2):
        if self.age == person_2.age and self.name == person_2.name and self.virus == person_2.virus:
            return True
        else:
            return False

    def infect(self, the_virus):
        self.virus.append(the_virus)
        
