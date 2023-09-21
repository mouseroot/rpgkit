# rpgkit
A small library for building text-based rpgs

```
Item
    name
    uses
    _destroy
    use()

HealingItem(Item)
    health

Weapon(Item)
    damage

Entity
    name
    hp
    maxhp
    level
    exp
    inventory

    add_exp()
    next_level()
    add_item()
    

Character
    _atk
    _def
    stat_points

Enemy(Character)

World
    ents

Game
    world

--- Menu Interactions ---
    
Explore
    Encounter Enemies
    Encounter Random items
    Encounter random people
        Dialog
        Shops
        Enemies(in Diquise)
Hunt[Locked]

Stats
    Player stats
    wins/loses

Inventory
    Backpack
Save

Journal
    Lore/Story
    Fights
    Besteriary

Crafting[Locked]
    Blueprints
    Craft
    Break[Locked]
Rest
```