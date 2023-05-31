from base import warrior

#Warrior class

class berzerker(warrior):
    def __init__(self, name, health=100):
        super().__init__(name, health)
        self.berzerk = 0


