import random

class Item:
    def __init__(self, name, val):
        self.uuid = random.randint(1,97779)
        self.name = name
        self.value = val
        self.uses = 1
        self._destroy = False

    def use(self, target):
        print(f"Using {self.name} on {target.name}")
        if self.uses == 1:
            self._destroy = True

    def copy(self):
        return Item(self.name, self.value)

class HealingItem(Item):
    def __init__(self, name, val,healthVal):
        super().__init__(name, val)
        self.health = healthVal

    def use(self, target):
        super().use(target)
        boosted_health = random.randint(1,5)
        target.hp += self.health + boosted_health

        print(f"Healed {target.name} for {self.health + boosted_health} pts")

class Weapon(Item):
    def __init__(self, name,val,dmg):
        super().__init__(name, val)
        self.damage = dmg

    def use(self, target):
        target.hp -= self.damage + random.randint(1,6)

class RangedWeapon(Weapon):
    def __init__(self, name, val, dmg, range):
        super().__init__(name, val, dmg)
        self.range = range

class Armor(Item):
    def __init__(self, name, val, ddef):
        super().__init__(name, val)
        self.defense = ddef