from base import wizard

class cleric(wizard):
    def __init__(self, name, health=100):
        super().__init__(name, health)
        self.healing = 0

class shade(wizard):
    def __init__(self, name, health=100):
        super().__init__(name, health)
        self.undead_power = 0