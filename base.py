class world:
    def __init__(self):
        pass

class character:
    def __init__(self, name, health=100):
        self.name = name
        self.health = health
        self.flags = []

    def take_damage(self, amt):
        self.health -= amt

class item:
    def __init__(self, name, value=1,count=1):
        self.name = name
        self.value = value
        self.count = count
        self.flags = []

    def use_item(self, target):
        self.count -= 1
        
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

    