a basic library for creating text based rpgs

## features

- easy to import
- world, character, item, npc, weapon, armor, spell and skill base classes

# Classes (base.py)

- World class is a container class that holds all the items, characters and various npcs
    - ability to load csv of items and characters
    -


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

- Warrior class
    - Berzerker

- Mage class
    

- Wizard class

- Archer class

- Thief class

# Generate (generate.py)

- generate class

- male names list

## Road map
- plugin to ai for randomized characters and story
- web front-end for exploring current worlds