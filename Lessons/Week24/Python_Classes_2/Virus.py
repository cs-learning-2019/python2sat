class Virus:
    def __init__(self, name, is_deadly, cure_cost):
        self.name = name
        self.is_deadly = is_deadly
        self.cure_cost = cure_cost

    def __str__(self):
        return self.name
    
    def __eq__(self, other_virus):
        if self.name == other_virus.name:
            return True
        else:
            return False
