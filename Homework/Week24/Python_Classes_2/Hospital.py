class Hospital():
    def __init__(self, name, money):
        self.name = name
        self.money = money
        self.patients = []
        self.cures = []

    def buy_cure(self, the_virus):
        if self.money >= the_virus.cure_cost:
            self.money -= the_virus.cure_cost
            self.cures.append(the_virus)
            print("Cure for " + str(the_virus) + " bought.")
        else:
            print("Not enough money for " + str(the_virus) + " cure.")
    
    def admit_patient(self, person):
        if len(person.virus) == 0:
            print(person.name + ", you are not sick get out!")
        else:
            print(person.name + " admitted to the hospital.")
            self.patients.append(person)
            
    def process_patients(self):
        new_patients = []
        for person in self.patients:
            new_virus = []
            dead = False
            print("------------------------------------")
            print("Treating " + person.name)
            for bug in person.virus:
                if bug in self.cures:
                    print("Cured " + bug.name)    
                else:
                    print("Could not cure " + bug.name)
                    new_virus.append(bug)
                    if bug.is_deadly == True and dead == False:
                        print(person.name + " is no more")
                        dead = True
                        
            person.virus = new_virus
            # Only continue treating the patient if they are still sick and not dead
            if dead == False and len(person.virus) > 0:
                new_patients.append(person)
        
        self.patients = new_patients
    
    def get_all_info(self):
        print("Here is the info for all patients.")
        for person in self.patients:
            print(person)
            
    def add_money(self, extra_money):
        self.money += extra_money
