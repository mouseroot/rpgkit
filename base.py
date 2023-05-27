FLAG_DELETE = 1
FLAG_DEAD = 2


class world:
    def __init__(self, name="Default World"):
        self.entities = []
        self.name = name

class character:
    def __init__(self, name, health=100):
        self.name = name
        self.health = health
        self.flags = []

    def take_damage(self, amt):
        self.health -= amt
        if self.health <= 0:
            self.flags.append(FLAG_DEAD)

class item:
    def __init__(self, name, value=1,max=1):
        self.name = name
        self.value = value
        self.count = 0
        self.max_count = max
        self.flags = []

    def use_item(self, target):
        self.count += 1
        if self.max_count >= self.count:
            self.flags.append(FLAG_DELETE)

class npc(character):
    def __init__(self, name):
        character.__init__(self, name)
        self.dialog = []

class weapon(item):
    def __init__(self, name, base_damage=1):
        item.__init__(self,name)
        self.base_damage = base_damage

    def use_item(self, target):
        target.take_damage(self.base_damage)
        super().use_item(target)

    
class armor(item):
    def __init__(self, name, value=1, count=1,defense=1):
        super().__init__(name, value, count)
        self.defense = defense
        self.using = False

class spell:
    def __init__(self, name, cost=1):
        self.name = name
        self.base_cost = cost

    def use_spell(self, target):
        pass