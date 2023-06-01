from base import mage

ELEMENT_NEUTRAL = "neutral"
ELEMENT_FIRE = "fire"
ELEMENT_WATER = "water"
ELEMENT_EARTH = "earth"
ELEMENT_AIR = "air"
ELEMENT_ETHER = "ether"


class druid(mage):
    def __init__(self, name, health=100):
        super().__init__(name, health)
        self.nature_buff = 0


class elemental(mage):
    def __init__(self, name, health=100):
        super().__init__(name, health)
        self.element = ELEMENT_NEUTRAL