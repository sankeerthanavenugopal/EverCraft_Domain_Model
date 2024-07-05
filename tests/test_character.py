import pytest
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

