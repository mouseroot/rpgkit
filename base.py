import json
from .item import HealingItem, Weapon, RangedWeapon, Armor, Item
from .crafting import Blueprint
from .entity import Enemy

class Skill:
    def __init__(self, name) -> None:
        self.name = name

class Spell:
    def __init__(self, name, cost) -> None:
        self.name = name
        self.cost = cost

class ResourceManager:
    def __init__(self, fname, key):
        try:
            self.database = json.load(open(fname))[key]
        except FileNotFoundError:
            print(f"{fname} was not found")

    def by_name(self, name):
        for item in self.database:
            if item["name"].lower() == name:
                return item

    def by_id(self, id):
        for item in self.database:
            if item["id"] == int(id):
                return item
            
    def spawn(self, data):
        pass

    def spawn_from_id(self, id):
        return self.spawn(self.by_id(id)["id"])

    def spawn_from_name(self, name):
        return self.spawn(self.by_name(name))

class MonsterManager(ResourceManager):
    def __init__(self, item_database):
        super().__init__(item_database, "monsters")

    def spawn(self, data):
        en = Enemy(data["name"], data["level"], data["health"], data["attack"])
        en.id = data["id"]
        en.exp = data["exp"]
        return en
    
class BlueprintManager(ResourceManager):
    def __init__(self, fname):
        super().__init__(fname, "blueprints")

    def spawn(self, item_data):
        bp = Blueprint(item_data["name"], item_data["requirements"], item_data["result"])
        bp.id = item_data["id"]
        return bp

class ItemManager(ResourceManager):
    def __init__(self, fname):
        super().__init__(fname, "items")

    def spawn(self, data):
        if data["type"] == "item":
            item = Item(data["name"], data["value"])
            item.id = data["id"]
            return item
        
        elif data["type"] == "healing":
            heal_item = HealingItem(data["name"], data["value"], data["healing"])
            heal_item.id = data["id"]
            return heal_item
        
        elif data["type"] == "weapon":
            wep = Weapon(data["name"], data["value"], data["damage"])
            wep.id = data["id"]
            return wep
        
        elif data["type"] == "ranged weapon":
            r_wep = RangedWeapon(data["name"], data["value"], data["damage"], data["range"])
            r_wep.id = data["id"]
            return r_wep
        
        elif data["type"] == "armor":
            arm = Armor(data["data"], data["value"], data["defense"])
            arm.id = data["id"]
            return arm