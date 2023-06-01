from base import warrior
from base import item,weapon
#Warrior class

class berzerker(warrior):
    def __init__(self, name, health=100):
        super().__init__(name, health)
        self.berzerk = 0

battle_axe = weapon("Battle Axe",base_damage=2)

