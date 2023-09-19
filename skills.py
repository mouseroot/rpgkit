import random
from .item import *
from . import base

def lookup_skill(self, sname):
    sname = sname.lower()
    if sname == "punch":
        return base.skill_punch
    elif sname == "bash":
        return base.skill_bash
    elif sname == "crafting":
        return base.skill_crafting
    
def lookup_spell(self, spname):
    spname = spname.lower()
    if spname == "healing 1":
        return base.spell_healing
    elif spname == "healing 2":
        return base.spell_healing2
    

class Skill:
    def __init__(self, name) -> None:
        self.name = name

class Spell:
    def __init__(self, name, cost) -> None:
        self.name = name
        self.cost = cost

