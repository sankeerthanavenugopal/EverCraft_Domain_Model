import pytest
import random
from unittest.mock import patch
from src.character import Character

def test_character_creation():
    character = Character("Aragorn", "Good")
    assert character.get_name() == "Aragorn"
    assert character.get_alignment() == "Good"

def test_set_name():
    character = Character("Aragorn", "Good")
    character.set_name("Legolas")
    assert character.get_name() == "Legolas"

def test_set_alignment(): 
    character = Character("Aragorn", "Good")
    character.set_alignment("Neutral")
    assert character.get_alignment() == "Neutral"

def test_default_armor_class():
    character = Character("Aragorn", "Good")
    assert character.get_armor_class() == 10

def test_default_hit_points():
    character = Character("Aragorn", "Good")
    assert character.get_hit_points() == 5

def test_attack_success():
    attacker = Character("Aragorn", "Good")
    defender = Character("Orc", "Evil")
    defender.armor_class = 10

    with patch('random.randint', return_value=15):
        assert attacker.attack(defender) is True

def test_attack_failure():
    attacker = Character("Aragorn", "Good")
    defender = Character("Orc", "Evil", race="Orc")
    
    with patch('random.randint', return_value=10):
        assert attacker.attack(defender) is False

def test_take_damage():
    character = Character("Aragorn", "Good")
    character.take_damage(3)
    assert character.get_hit_points() == 2

def test_critical_hit():
    attacker = Character("Aragorn", "Good")
    defender = Character("Orc", "Evil")
    defender.armor_class = 10

    with patch('random.randint', return_value=20):
        assert attacker.attack(defender) is True
        assert defender.get_hit_points() == 3

def test_gain_experience():
    attacker = Character("Aragorn", "Good")
    defender = Character("Orc", "Evil")
    defender.armor_class = 10
    
    with patch('random.randint', return_value=15):
        attacker.attack(defender)
        assert attacker.experience == 10

def test_level_up():
    character = Character("Aragorn", "Good")
    character.gain_experience(1000)
    assert character.level == 2
    assert character.get_hit_points() == 10 + character.get_modifier(character.constitution)

def test_ability_scores_default():
    character = Character("Aragorn", "Good")
    assert character.strength == 10
    assert character.dexterity == 10
    assert character.constitution == 10
    assert character.wisdom == 10
    assert character.intelligence == 10
    assert character.charisma == 10

def test_ability_modifiers():
    character = Character("Aragorn", "Good")
    assert character.get_modifier(10) == 0
    assert character.get_modifier(8) == -1
    assert character.get_modifier(15) == 2
    assert character.get_modifier(20) == 5

def test_paladin_alignment():
    character = Character("Arthur", "Neutral", class_name="Paladin")
    assert character.get_alignment() == "Good"

def test_rogue_alignment():
    character = Character("Robin", "Good", class_name="Rogue")
    assert character.get_alignment() == "Neutral"

def test_halfling_alignment():
    character = Character("Frodo", "Evil", race="Halfling")
    assert character.get_alignment() == "Neutral"

def test_orc_race_modifiers():
    character = Character("Thrall", "Neutral", race="Orc")
    assert character.strength == 12
    assert character.intelligence == 9
    assert character.wisdom == 9
    assert character.charisma == 9
    assert character.get_armor_class() == 12  # 10 base + 2 thick hide

def test_dwarf_race_modifiers():
    character = Character("Gimli", "Good", race="Dwarf")
    assert character.constitution == 11
    assert character.charisma == 9

def test_elf_race_modifiers():
    character = Character("Legolas", "Good", race="Elf")
    assert character.dexterity == 11
    assert character.constitution == 9

def test_halfling_race_modifiers():
    character = Character("Sam", "Good", race="Halfling")
    assert character.dexterity == 11
    assert character.strength == 9

def test_weapon_wield():
    character = Character("Aragorn", "Good")
    longsword = {'name': 'Longsword', 'damage': 5, 'attack_bonus': 0}
    character.wield_weapon(longsword)
    assert character.weapon == longsword

def test_armor_wear():
    character = Character("Aragorn", "Good")
    leather_armor = {'name': 'Leather Armor', 'armor_class': 2, 'type': 'Leather'}
    character.wear_armor(leather_armor)
    assert character.armor == leather_armor
    assert character.get_armor_class() == 12  # 10 base + 2 leather armor

def test_shield_equip():
    character = Character("Aragorn", "Good")
    shield = {'name': 'Shield', 'armor_class': 3, 'attack_penalty': 4}
    character.equip_shield(shield)
    assert character.shield == shield
    assert character.get_armor_class() == 13  # 10 base + 3 shield

def test_add_item():
    character = Character("Aragorn", "Good")
    ring_of_protection = {'type': 'ring_of_protection', 'armor_class': 2}
    character.add_item(ring_of_protection)
    assert ring_of_protection in character.items
    assert character.get_armor_class() == 14  # 10 base + 2 ring of protection + 2 dex

def test_orc_elf_interaction():
    elf = Character("Legolas", "Good", race="Elf")
    elf.wield_weapon({'name': 'Elven Longsword', 'damage': 5, 'attack_bonus': 1, 'bonus_vs_orc': 2, 'bonus_vs_elf_and_orc': 5})
    orc = Character("Thrall", "Evil", race="Orc")
    assert elf.attack(orc)  # Elves get bonus vs. Orcs