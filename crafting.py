from .item import *
from . import base

def lookup_item(item_name):
    item_name = item_name.lower()
    if item_name == "potion":
        return base.potion
    elif item_name == "lg_potion":
        return base.lg_potion
    elif item_name == "xlg_potion":
        return base.xlg_potion

class Blueprint:
    def __init__(self, req_items, result_item):
        self.req_items = req_items
        self.result_item = result_item

    def can_craft(self, player):
        okay = True
        for pair in self.req_items:
            for k_name in pair:
                #print(f"Do you have {pair[k_name]} of {k_name}?")
                req_count = pair[k_name]
                #print(f"We need {req_count}")
                cnt = player.inventory.get_item_count(k_name)
                if cnt >= req_count:
                    okay = True
                else:
                    okay = False
        return okay

    def craft(self, player):
        print(f"Attempting to craft {self.result_item.name}")
        if self.can_craft(player):
            #print(f"Can Craft")
            for item in self.req_items:
                for key in item:
                    #req_count = self.req_items[key]
                    #print(f"Searching for {item[key]} of {key}")
                    slot = player.has_item(key)
                    
                    if slot:
                        slot.count -= item[key]
                        player.inventory.update()
            player.add_item(self.result_item)
        else:
            #print("CANT")
            return False
