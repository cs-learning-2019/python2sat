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

    def infect(self, the_virus):
        self.virus.append(the_virus)
        
    def __eq__(self, other_person):
        if self.name == other_person.name and self.age == other_person.age and set(self.virus) == set(other_person.virus):
            return True
        else:
            return False
