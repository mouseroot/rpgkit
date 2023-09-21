import random

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
                slot.count += count
                return
        slot = InventorySlot(item_id,count)
        self.items.append(slot)

    def remove_item(self, item_id, count=1):
        slot = self.has_item(item_id)
        if slot:
            slot.count -= count
            if slot.count <= 0:
                self.items.remove(slot)

    def has_item(self, item_id):
        for slot in self.items:
            if slot.item == int(item_id):
                return slot
        return False
    
    def get_count(self, item_id):
        slot = self.has_item(item_id)
        if slot:
            return slot.count
        return 0

        

    

class Entity:
    def __init__(self, name, level=1,hp=50, _atk=1, _def=1):
        self.id = 0

        self.hp = hp
        self.maxhp = self.hp
        self.name = name

        self.level  = level
        self.exp = 1
        self.gold = 1

        self.stat_points = 0
        self.stat_attack = _atk
        self.stat_defense = _def

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
        dmg -= self.stat_defense
        if dmg <= 0:
            dmg = 0
        self.hp -= dmg
        if self.hp <= 0:
            self._dead = True
            self.hp = 0

    def add_item(self, item, count=1):
        self.inventory.add_item(item, count)

    def add_spell(self, spell):
        self.spells.append(spell)

    def add_skill(self, skill):
        self.skills.append(skill)

    def has_skill(self, skname):
        for skill in self.skills:
            if skill.name.lower() == skname:
                return skill
        return False
    
    def has_spell(self, spname):
        for spell in self.spells:
            if spell.name.lower() == spname:
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
        min_attack = int((self.stat_attack + weapon_damage) * (self.level))
        max_attack = int(min_attack * 1.6)  
        calculated_attack = int(random.randint(min_attack, max_attack))
        target.take_damage(calculated_attack)
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
                self.stat_attack += value
                self.stat_points -= value
            elif item.lower() == "defense":
                self.stat_defense += value
                self.stat_points -= value
            return True
        else:
            return False


class Character(Entity):
    def __init__(self,name,level,hp=50,_atk=1,_def=1):
        super().__init__(name,level,hp,_atk,_def)



class Enemy(Character):
    def __init__(self,name,level,hp,_atk=1,_def=1):
        super().__init__(name,level,hp,_atk,_def)
