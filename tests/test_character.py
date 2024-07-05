import pytest
from src.character import Character
import random 

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

    random.seed(15)  # Force the roll to be 15 for consistent test result
    assert attacker.attack(defender) is True

def test_attack_failure():
    attacker = Character("Aragorn", "Good")
    defender = Character("Orc", "Evil")
    defender.armor_class = 15

    random.seed(10)  # Force the roll to be 10 for consistent test result
    assert attacker.attack(defender) is False
