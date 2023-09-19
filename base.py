import random
""" 
--- Monsters ---
Ant 1/1
Rat 2/1
Roach 1/1
Mole 2/1
Orc 3/2
Bear 4/3
Troll 5/4
Skeleton 3/3
Zombie 2/3
"""
from .crafting import *
from .item import *
from .entity import *
from .skills import *

# Monsters
ant = Enemy("Ant",1,10,1,1)
ant.exp = 1

rat = Enemy("Rat",1,18,2,1)
rat.exp = 3

roach = Enemy("Roach",1,5,1,1)
roach.exp = 4

mole = Enemy("Mole",1,14,2,1)
mole.exp = 6

orc = Enemy("Orc",2,25,3,2)
orc.exp = 11

bear = Enemy("Bear",2,31,4,3)
bear.exp = 15

troll = Enemy("Troll",3,44,5,4)
troll.exp = 21

skeleton = Enemy("Skeleton",2,21,3,3)
skeleton.exp = 18

zombie = Enemy("Zombie",2,21,2,3)
zombie.exp = 16

# Items
potion = HealingItem("Potion",3,5)
lg_potion = HealingItem("Large Potion",7,15)
xlg_potion = HealingItem("XLarge Potion",15,50)

mana_potion = HealingItem("Mana Potion",4,7)
mana_lg_potion = HealingItem("Large Mana Potion",9,17)
mana_xlg_potion = HealingItem("XLarge Mana Potion",15,31)

glass_shard = Item("Glass Shard",1)
ruler = Item("Ruler",1)
protractor = Item("Protractor",1)
bottle = Item("Bottle",7)

# Weapons
stick = Weapon("Stick",1,1)
rod = Weapon("Rod",3,3)
wooden_sword = Weapon("Wooden Sword",5,8)
sword = Weapon("Sword",17,12)

# Ranged Weapon
pistol = RangedWeapon("Pistol",15,14,100)
rifle = RangedWeapon("Rifle",20,21,350)
heal_rifle = RangedWeapon("Healing Rifle",999,999,999)

# Armor
shirt = Armor("Shirt",1,2)
vest = Armor("Vest",5,5)
thin_armor = Armor("Thin Armor",3,11)
medium_armor = Armor("Medium Armor",5,17)
heavy_armor = Armor("Heavy Armor",27,30)

# Blueprints
blueprint_lg_potion = Blueprint([{
    'potion':2
}],lg_potion)

blueprint_xlg_potion = Blueprint([{
    'potion':4
}],xlg_potion)

blueprint_bottle = Blueprint([{
    'glass_shard':4
}],bottle)

blueprint_heal_rifle = Blueprint([{
    'bottle':1,
    'potion':4,
    'rifle':1
}],heal_rifle)


skill_punch = Skill("Punch")
skill_bash = Skill("Bash")
skill_crafting = Skill("Crafting")

spell_healing = Spell("Healing I",5)
spell_healing2 = Spell("Healing II",15)


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

--- Monsters ---
Ant 1/1
Rat 2/1
Roach 1/1
Mole 2/1
Orc 3/2
Bear 4/3
Troll 5/4
Skeleton 3/3
Zombie 2/3

--- Skills ---


--- Spells ---


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