a basic library for creating text based rpgs

## features

- easy to import
- world, character, item, npc, weapon, armor, spell and skill base classes

# Classes (base.py)

- World class is a container class that holds all the items, characters and various npcs
    - ability to load csv of items and characters

- Base Character class 
    - health, skills and inventory, 
    - base attack/defense
    - experience/levels
    - give/add items
    - deal/take damage

- Base Item class 
    - base value
    - maximum number of uses
    - use item

- Base NPC class extends characer class
    - adds dialog

- Weapon class extends item class
    - adds base damage

- armor class extends item class
    - adds base defense

- spell class
    - base cost

- skill class
    - level, 
    - experience
    - experience for next level

## Character Classes

- Warrior class - the warrior class is a bruteforce class that specializes in raw attack power over speed or accuracy.
    - Berzerker - the berzerker class specializes in extremly high damage at the cost of speed, accuracy and sometimes even your own health.

- Mage class - class of magic wielders that rely on arcane energy and power from other realms to craft raw attacks and spells


- Wizard class - a more robust class of magic wielder that relies on existing spells to accomplish thier goals

- Archer class - long range attacks, utilizing stealth and extreme accuracy, they are not strong, but they are deadly accurate from far away.

- Thief class - a class that specializes in being a jack of all trades, fast, accurate and capable of escaping the stickiest of situations

# Generate (generate.py)

- generate class

- male names list

## Road map
- plugin to ai for randomized characters and story
- web front-end for exploring current worlds