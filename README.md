a basic library for creating text based rpgs

## features

- easy to import
- world, character, item, npc, weapon, armor, spell and skill base classes

# Classes (base.py)

- World class is a container class that holds all the items, characters and various npcs

- Character class has health, skills and inventory, base attack/defense

- Item class has a base value and maximum number of uses

- npc class extends characer class, adds dialog

- weapon class extends item class, adds base_damage

- armor class extends item class, adds base_defense

- spell class has a base_cost

- skill class has level, exp and exp for next level

# Generate (generate.py)

- generate class

- male names list

## Road map
- plugin to ai for randomized characters and story
- web front-end for exploring current worlds