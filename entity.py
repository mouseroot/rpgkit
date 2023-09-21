import random
from . import skills



class InventorySlot:
    def __init__(self, id, count):
        self.item = id
        self.count = count

class Inventory:
    def __init__(self):
        self.items = []
        self.count = 0

    def add_item(self, item_id, count=1):
        for slot in self.items:
            if slot.item == item_id:
                #print(f"Item exists, adding to existing slot")
                slot.count += count
                return
        #print("Creating a new slot")
        slot = InventorySlot(item_id,count)
        self.items.append(slot)
        

    

class Entity:
    def __init__(self, name, level=1,hp=50, atk=1,_def=1):
        self.id = 0

        self.hp = hp
        self.maxhp = self.hp
        self.name = name

        self.level  = level
        self.exp = 1
        self.gold = 1

        self.stat_points = 0
        self._atk = atk
        self._def = _def

        self.inventory = Inventory()
        self.blueprints = []
        self.weapon = None
        self.armor = None

        self.mana = 0
        self.maxmana = self.mana

        self.spells = []
        self.skills = []

        self._dead = False
        self._defending = False

    def show_inventory(self):
        for slot in self.inventory.items:
            yield slot

    def add_gold(self, amt):
        self.gold += amt

    def take_gold(self, amt):
        self.gold -= amt
        if self.gold <= 0:
            self.gold = 0

    def has_item(self, item_name):
        chk_item =  self.inventory.has_item(item_name)
        if chk_item:
            return chk_item
        else:
            return False
    
    def set_weapon(self, wep):
        self.weapon = wep

    def set_armor(self, arm):
        self.armor = arm

    def take_damage(self, dmg):
        dmg -= self._def
        if dmg <= 0:
            dmg = 0
        #print(f"{self.name} takes {dmg} damage")
        self.hp -= dmg
        if self.hp <= 0:
            #print(f"{self.name} has died")
            self._dead = True
            self.hp = 0

    def add_item(self, item, count=1):
        self.inventory.add_item(item, count)

    def add_spell(self, spell):
        self.spells.append(spell)

    def add_skill(self, skill):
        self.skills.append(skill)

    def has_skill(self, skname):
        skill = skills.lookup_skill(skname)
        if skill:
            return skill
        return False
    
    def has_spell(self, spname):
        spell = skills.lookup_spell(spname)
        if spell:
            return spell
        return False
    

    def add_exp(self, exp):
        self.exp += exp
        if self.exp >= self.next_level():
            self.level += 1
            return True

    def next_level(self, base_exp=10, exp_growth=1.8):
        exp_needed = base_exp * (exp_growth ** (self.level - 1))
        return int(exp_needed)
    
    def attack(self, target):
        weapon_damage = self.weapon.damage if self.weapon is not None else 0
        #print(f"Weapon: {self.weapon.name if self.weapon is not None else 'No Weapon'}")
        #print(f"Weapon Damage: {weapon_damage}")

        min_attack = int((self._atk + weapon_damage) * (self.level))
        max_attack = int(min_attack * 1.6)  # Adjust this factor as needed for your game balance
        #print(f"Damage Ranges: ({min_attack}/{max_attack})")
        calculated_attack = int(random.randint(min_attack, max_attack))
       #calculated_attack = int(calculated_attack)
        target.take_damage(calculated_attack)
        #print(f"Calculated Attack: {calculated_attack}")
        return calculated_attack
    
    def reset(self):
        self.hp = self.maxhp
        self.mana = self.maxmana

    def is_dead(self):
        return self._dead
    
    def get_exp(self):
        return abs(int((self.exp * 1.2) + random.randint(1,3) * self.level-1))
    
    def spend_stats(self, item, value):
        if self.stat_points >= value:
            if item.lower() == "health":
                self.maxhp += value
                self.stat_points -= value
            elif item.lower() == "attack":
                self._atk += value
                self.stat_points -= value
            elif item.lower() == "defense":
                self._def += value
                self.stat_points -= value
            return True
        else:
            return False


class Character(Entity):
    def __init__(self,name,level,hp=50,ak=1,df=1):
        super().__init__(name,level,hp,ak,df)



class Enemy(Character):
    def __init__(self,name,level,hp,_atk=1,ddef=1):
        super().__init__(name,level,hp,_atk,ddef)
