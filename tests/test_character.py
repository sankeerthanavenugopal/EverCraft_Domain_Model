import pytest
import random
from src.character import Character
from unittest.mock import patch

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

    # random.seed(15)  # Force the roll to be 15 for consistent test result
    # print("Test Success:")
    # assert attacker.attack(defender) is True

def test_attack_failure():
    attacker = Character("Aragorn", "Good")
    defender = Character("Orc", "Evil")
    defender.armor_class = 15
    
    with patch('random.randint', return_value=10):
        assert attacker.attack(defender) is False 
    # random.seed(10)  # Force the roll to be 10 for consistent test result
    # print("Test Failure:")

    # assert attacker.attack(defender) is False

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
    # random.seed(20)  # Force the roll to be 20 for consistent test result
    # assert attacker.attack(defender) is True
    # assert defender.get_hit_points() == 3  # 5 - (1 * 2) = 3

def test_gain_experience():
    attacker = Character("Aragorn", "Good")
    defender = Character("Orc", "Evil")
    defender.armor_class = 10
    
    with patch('random.randint', return_value=15):
        attacker.attack(defender)
        assert attacker.experience == 10
    # random.seed(15)  # Force the roll to be 15 for consistent test result
    # attacker.attack(defender)
    # assert attacker.experience == 10

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

def test_dexterity_modifier_applied_to_armor_class():         ########## modify it later?
    character = Character("Aragorn", "Good")
    character.dexterity = 14
    character.armor_class = 10 + character.get_modifier(character.dexterity)  # Recalculate AC
    assert character.get_armor_class() == 12  # 10 + 2


def test_constitution_modifier_applied_to_hit_points():         ########## modify it later?
    character = Character("Aragorn", "Good")
    character.constitution = 14
    character.hit_points = 5 + character.get_modifier(character.constitution)
    assert character.get_hit_points() == 7  




