class PartyAnimal:
    x = 0
    name = ""
    def __init__(self, nam):
        self.name = nam
        print (self.name, "Constructed")
    
    def party(self):
        self.x = self.x + 1
        print (self.name, "party count", self.x)
        
    def __del__(self):
        print ("I am destructed", self.name)

s = PartyAnimal("Sally")
s.party()

j = PartyAnimal("Jim")
j.party()
s.party()