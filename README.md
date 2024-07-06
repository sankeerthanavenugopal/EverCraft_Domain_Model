# EverCraft
EverCraft is a simple MMORPG (Massively Multiplayer Online Role-Playing Game) character creation and management system. It allows you to create characters with various classes, races, and equipment, and simulate attacks between them. The system supports character attributes, leveling, alignment, and combat mechanics.

## Features
* Character Creation: Create characters with unique names, alignments, classes, and races.
* Attributes: Characters have six core attributes (Strength, Dexterity, Constitution, Wisdom, Intelligence, Charisma) with modifiers.
* Classes: Different classes (Fighter, Rogue, Monk, Paladin) with unique abilities and restrictions.
* Races: Various races (Human, Orc, Dwarf, Elf, Halfling) with specific bonuses and penalties.
* Combat Mechanics: Characters can attack each other, calculate damage, and apply critical hits.
* Equipment: Characters can wield weapons, wear armor, and use shields and items to enhance their capabilities.
* Leveling: Characters gain experience points and level up, increasing their hit points and combat effectiveness.
  
## Usage
 
```python
from character import Character
 
# Define weapons, armors, and items
longsword = {'name': 'Longsword', 'damage': 5, 'attack_bonus': 0}
waraxe = {'name': '+2 Waraxe', 'damage': 6, 'attack_bonus': 2, 'crit_multiplier': 3, 'rogue_crit_multiplier': 4}
elven_longsword = {'name': 'Elven Longsword', 'damage': 5, 'attack_bonus': 1, 'bonus_vs_orc': 2, 'bonus_vs_elf_and_orc': 5}
nun_chucks = {'name': 'Nun Chucks', 'damage': 6, 'attack_bonus': -4, 'monk_bonus': -4}
 
leather_armor = {'name': 'Leather Armor', 'armor_class': 2, 'type': 'Leather'}
plate_armor = {'name': 'Plate Armor', 'armor_class': 8, 'type': 'Plate'}
elven_chain_mail = {'name': 'Elven Chain Mail', 'armor_class': 5, 'type': 'Chain', 'elf_bonus': 3, 'attack_bonus': 1, 'damage_bonus': 1}
 
shield = {'name': 'Shield', 'armor_class': 3, 'attack_penalty': 4}
ring_of_protection = {'type': 'ring_of_protection', 'armor_class': 2}
belt_of_giant_strength = {'type': 'belt_of_giant_strength', 'strength_bonus': 4}
amulet_of_heavens = {'type': 'amulet_of_heavens', 'bonus_vs_neutral': 1, 'bonus_vs_evil': 2}
 
# Create characters
fighter = Character(name="Aragorn", alignment="Good", class_name="Fighter", race="Human")
rogue = Character(name="Legolas", alignment="Neutral", class_name="Rogue", race="Elf")
monk = Character(name="Bruce", alignment="Neutral", class_name="Monk", race="Dwarf")
paladin = Character(name="Arthur", alignment="Good", class_name="Paladin", race="Halfling")
orc = Character(name="Orc", alignment="Evil", class_name="Warrior", race="Orc")
 
# Equip characters
fighter.wield_weapon(longsword)
rogue.wield_weapon(elven_longsword)
monk.wield_weapon(nun_chucks)
paladin.wield_weapon(waraxe)
fighter.wear_armor(plate_armor)
rogue.wear_armor(elven_chain_mail)
fighter.equip_shield(shield)
 
# Simulate an attack
fighter.attack(orc)
```
 
## Running Tests
To run the tests, use pytest. Make sure you have it installed in your virtual environment.
 
1. Install pytest:
```bash
pip install pytest
```
 
2. Run tests
```bash
pytest tests
```
 
This will discover and run all the tests in the repository, providing output about which tests passed and which failed.
