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

- Item class has a base value and maximum number of uses

- npc class extends characer class, adds dialog

- weapon class extends item class, adds base_damage

- armor class extends item class, adds base_defense

- spell class has a base_cost

- skill class has level, exp and exp for next level

## Character Classes

- Warrior class

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