import json
from .item import HealingItem, Weapon, Armor, Item, ResourceManager
from .crafting import Blueprint
from .entity import Enemy


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
            if item["id"] == id:
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
        bp = Blueprint(item_data["requirements"], item_data["result"])
        bp.id = item_data["id"]
        return bp

class ItemManager(ResourceManager):
    def __init__(self, fname):
        super().__init__(fname, "items")

    def spawn(self, data):
        if data["type"] == "item":
            i = Item(data["name"], data["value"])
            i.id = data["id"]
            return i
        elif data["type"] == "healing":
            hl = HealingItem(data["name"], data["value"], data["healing"])
            hl.id = data["id"]
            return hl
        elif data["type"] == "weapon":
            wep = Weapon(data["name"], data["value"], data["damage"])
            wep.id = data["id"]
            return wep
        elif data["type"] == "armor":
            arm = Armor(data["data"], data["value"], data["defense"])
            arm.id = data["id"]
            return arm

"""
--- Class ---

Item
    name
    uses
    _destroy
    use()

HealingItem(Item)
    health

Weapon(Item)
    damage

Entity
    name
    hp
    maxhp
    level
    exp
    inventory

    add_exp()
    next_level()
    add_item()
    

Character
    _atk
    _def
    stat_points

Enemy(Character)

World
    ents

Game
    world

--- Menu Interactions ---
    
Explore
    Encounter Enemies
    Encounter Random items
    Encounter random people
        Dialog
        Shops
        Enemies(in Diquise)
Hunt[Locked]

Stats
    Player stats
    wins/loses

Inventory
    Backpack
Save

Journal
    Lore/Story
    Fights
    Besteriary

Crafting[Locked]
    Blueprints
    Craft
    Break[Locked]
Rest
"""


class World:
    def __init__(self,name):
        self.name = name
        self.ents = []

    def spawnEntity(self, _type, args):
        ent = _type(*args)
        self.ents.append(ent)
        return ent

    def spawnItem(self,_type, args):
        item = _type(*args)
        self.ents.append(item)
        return item
    
world = World("Main")
