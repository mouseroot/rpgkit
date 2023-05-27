import random
from .base import *

NAME_LIST_MALE = [
    "albert","adam","andrew","arron",
    "benny","ben","bill","bernie","barron",
    "carl","charles","chad",
    "derrik","dan","devin","dillon",
    "evan","eric","gary","henry"]

class generate:
    def __init__(self,name) -> None:
        self.gen_world = None
        self.name = name

    def create_world(self, ent_count):
        self.gen_world = world(self.name)
        for _ in range(int(ent_count)):
            char = character(random.choice(NAME_LIST_MALE),health=random.randint(90,100))
            n = npc(random.choice(NAME_LIST_MALE))
            self.gen_world.add_entity(random.choice[char,n])


gen = generate("Main")