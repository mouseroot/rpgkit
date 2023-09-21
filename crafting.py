
class Blueprint:
    def __init__(self, name, req_items, result_item):
        self.id = 0
        self.name = name
        self.req_items = req_items
        self.result_item = result_item

    def can_craft(self, player):
        for item in self.req_items:
            item_count = int(self.req_items[item])         
            item_slot = player.inventory.has_item(item)
            if item_slot:
                count = player.inventory.get_count(item)
                if count >= item_count:
                    continue
                else:
                    return False
            else:
                return False
        return True


    def craft(self, player):
        if self.can_craft(player):
            for item in self.req_items:
                player.inventory.remove_item(item, int(self.req_items[item]))
            player.inventory.add_item(self.result_item)
            

        
