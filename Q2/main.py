class Father:
    eyes = "blue eyes"
class Mother:
    hair = "black hair"
    
class You(Mother, Father):
    def describeyourself(self):
        print("I have", self.eyes, "and", self.hair)

you = You()
you.describeyourself()