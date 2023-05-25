class world:
    def __init__(self):
        pass

class character:
    def __init__(self, name, health):
        self.name = name
        self.health = health

class item:
    def __init__(self, name, value=1,count=1):
        self.name = name
        self.value = value
        self.count = count
        self.flags = []

    def use_item(self, target):
        self.count -= 1
        
