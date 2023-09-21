
class Blueprint:
    def __init__(self, req_items, result_item):
        self.req_items = req_items
        self.result_item = result_item

    def can_craft(self, player):
        return False

    def craft(self, player):
        print(f"Attempting to craft {self.result_item.name}")
        
