import random

class Character:
    def __init__(self, name, alignment, class_name="Default", race="Human"):
        self.name = name
        self.class_name = class_name
        self.race = race
        self.alignment = self.set_initial_alignment(alignment)
        self.strength = 10
        self.dexterity = 10
        self.constitution = 10
        self.wisdom = 10
        self.intelligence = 10
        self.charisma = 10
        self.armor_class = 0
        self.apply_race_modifiers()
        self.experience = 0
        self.level = 1
        self.armor_class = self.armor_class + 10 + self.get_modifier(self.dexterity) + self.get_additional_ac_modifier()
        self.hit_points = self.calculate_initial_hit_points()
        self.alive = True
        self.weapon = None
        self.armor = None
        self.shield = None
        self.items = []

    def set_initial_alignment(self, alignment):
        if self.class_name == "Rogue" and alignment == "Good":
            return "Neutral"
        if self.class_name == "Paladin" and alignment != "Good":
            return "Good"
        if self.race == "Halfling" and alignment == "Evil":
            return "Neutral"
        return alignment

    def apply_race_modifiers(self):
        if self.race == "Orc":
            self.strength += 2
            self.intelligence -= 1
            self.wisdom -= 1
            self.charisma -= 1
            self.armor_class += 2  # Thick hide adds to armor class
        elif self.race == "Dwarf":
            self.constitution += 1
            self.charisma -= 1
        elif self.race == "Elf":
            self.dexterity += 1
            self.constitution -= 1
        elif self.race == "Halfling":
            self.dexterity += 1
            self.strength -= 1

    def calculate_initial_hit_points(self):
        base_hp = {
            'Fighter': 10,
            'Rogue': 5,
            'Monk': 6,
            'Paladin': 8    
        }.get(self.class_name, 5)
        return base_hp + self.get_modifier(self.constitution) 
    
    def get_additional_ac_modifier(self):
        if self.class_name == "Monk" and self.get_modifier(self.wisdom) > 0:
            return self.get_modifier(self.wisdom)
        return 0

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_alignment(self):
        return self.alignment

    def set_alignment(self, alignment):
        if self.class_name == "Rogue" and alignment == "Good":
            self.alignment = "Neutral"
        elif self.class_name == "Paladin":
            self.alignment = "Good"
        elif self.race == "Halfling" and alignment == "Evil":
            self.alignment = "Neutral"
        else:
            self.alignment = alignment

    def get_armor_class(self):
        base_ac = self.armor_class
        if self.armor:
            base_ac += self.armor.get('armor_class', 0)
            if self.armor.get('elf_bonus', 0) and self.race == "Elf":
                base_ac += self.armor['elf_bonus']
        if self.shield:
            base_ac += self.shield.get('armor_class', 0)
        for item in self.items:
            if item['type'] == 'ring_of_protection':
                base_ac += item['armor_class']
        return base_ac

    def get_hit_points(self):
        return self.hit_points
    
    def attack(self, opponent):
        roll = random.randint(1, 20) + self.get_attack_bonus(opponent)
        opponent_ac = opponent.get_armor_class() - (opponent.get_modifier(opponent.dexterity) if self.class_name == 'Rogue' and opponent.get_modifier(opponent.dexterity) > 0 else 0)
        print(roll)
        print(opponent_ac)
        if self.race == "Elf" and opponent.race == "Orc":
            opponent_ac -= 2
        print(f"Roll: {roll}, Opponent Armor Class: {opponent_ac}")
        if roll == 20:  # Check for critical hit
            damage = self.calculate_damage(critical=True, opponent=opponent)
            opponent.take_damage(damage)
            self.gain_experience(10)
            return True
        elif roll >= opponent_ac:  # Check if the attack hits
            damage = self.calculate_damage(opponent=opponent)
            opponent.take_damage(damage)
            self.gain_experience(10)
            return True
        return False  # Attack misses
    
    def get_attack_bonus(self, opponent):
        base_bonus = self.get_modifier(self.strength)
        if self.class_name == 'Rogue':
            base_bonus = self.get_modifier(self.dexterity)
        if self.class_name == "Paladin" and opponent.alignment == "Evil":
            base_bonus += 2
        if self.class_name == "Monk":
            if self.level % 2 == 0 or self.level % 3 == 0:
                base_bonus += 1
        if self.class_name == 'Rogue' and self.level % 2 == 0:
            base_bonus += 1
        if self.class_name == 'Fighter' or self.class_name == 'Paladin':
            base_bonus += 1
        if self.race == "Dwarf" and opponent.race == "Orc":
            base_bonus += 2
        if self.weapon:
            base_bonus += self.weapon.get('attack_bonus', 0)
            if self.weapon.get('name') == 'Nun Chucks' and self.class_name != "Monk":
                base_bonus += self.weapon.get('monk_bonus', 0)
            if self.weapon.get('bonus_vs_orc', 0) and opponent.race == "Orc":
                base_bonus += self.weapon['bonus_vs_orc']
            if self.weapon.get('bonus_vs_elf_and_orc', 0) and self.race == "Elf" and opponent.race == "Orc":
                base_bonus += self.weapon['bonus_vs_elf_and_orc']
        if self.armor and self.armor.get('attack_bonus', 0) and self.race == "Elf":
            base_bonus += self.armor['attack_bonus']
        if self.shield and 'attack_penalty' in self.shield:
            base_bonus -= self.shield['attack_penalty']
        for item in self.items:
            if item['type'] == 'amulet_of_heavens':
                if opponent.alignment == "Neutral":
                    base_bonus += item['bonus_vs_neutral']
                elif opponent.alignment == "Evil":
                    base_bonus += item['bonus_vs_evil']
                if self.class_name == "Paladin":
                    if opponent.alignment == "Neutral":
                        base_bonus += item['bonus_vs_neutral']  # Double bonus for Paladins
                    elif opponent.alignment == "Evil":
                        base_bonus += item['bonus_vs_evil']  # Double bonus for Paladins
        return base_bonus
 
    def calculate_damage(self, critical=False, opponent=None):
        base_damage = 1 + self.get_modifier(self.strength)
        if self.class_name == "Monk":
            base_damage = 3
        if self.weapon:
            base_damage += self.weapon.get('damage', 0)
            if critical:
                crit_multiplier = self.weapon.get('crit_multiplier', 2)
                if self.class_name == "Rogue":
                    crit_multiplier = self.weapon.get('rogue_crit_multiplier', 3)
                base_damage = max(base_damage * crit_multiplier, 1)
            if self.weapon.get('bonus_vs_orc', 0) and opponent.race == "Orc":
                base_damage += self.weapon['bonus_vs_orc']
            if self.weapon.get('bonus_vs_elf_and_orc', 0) and self.race == "Elf" and opponent.race == "Orc":
                base_damage += self.weapon['bonus_vs_elf_and_orc']
        elif critical:
            if self.class_name == "Rogue":
                base_damage = max(base_damage * 3, 1)
            elif self.class_name == "Paladin" and opponent and opponent.alignment == "Evil":
                base_damage = max(base_damage * 3, 1)
            else:
                base_damage = max(base_damage * 2, 1)
        if self.armor and self.armor.get('damage_bonus', 0) and self.race == "Elf":
            base_damage += self.armor['damage_bonus']
        for item in self.items:
            if item['type'] == 'amulet_of_heavens':
                if opponent.alignment == "Neutral":
                    base_damage += item['bonus_vs_neutral']
                elif opponent.alignment == "Evil":
                    base_damage += item['bonus_vs_evil']
                if self.class_name == "Paladin":
                    if opponent.alignment == "Neutral":
                        base_damage += item['bonus_vs_neutral']  # Double bonus for Paladins
                    elif opponent.alignment == "Evil":
                        base_damage += item['bonus_vs_evil']  # Double bonus for Paladins
        return max(base_damage, 1)

    def take_damage(self, damage):
        if self.armor and 'damage_reduction' in self.armor:
            damage -= self.armor['damage_reduction']
        self.hit_points -= damage
        if self.hit_points <= 0:
            self.hit_points = 0
            self.alive = False

    def get_modifier(self, ability_score):
        return (ability_score - 10) // 2

    def gain_experience(self, points):
        self.experience += points
        self.check_level_up()

    def check_level_up(self):
        if self.experience >= self.level * 1000:
            self.level_up()

    def level_up(self):
        self.level += 1
        hp_gain = 5 + self.get_modifier(self.constitution)
        if self.class_name == "Fighter":
            hp_gain += 5
        if self.class_name == "Paladin":
            hp_gain += 3
        if self.race == "Dwarf" and self.get_modifier(self.constitution) > 0:
            hp_gain += self.get_modifier(self.constitution)
        self.hit_points += hp_gain
        if self.level % 2 == 0:
            self.armor_class += 1

    def wield_weapon(self, weapon):
        self.weapon = weapon

    def wear_armor(self, armor):
        if (self.class_name == 'Fighter' or self.race == 'Dwarf') and armor['type'] == 'Plate':
            self.armor = armor
        elif self.class_name != 'Fighter' and armor['type'] == 'Plate':
            print("Cannot wear Plate armor")
        else:
            self.armor = armor

    def equip_shield(self, shield):
        self.shield = shield

    def add_item(self, item):
        self.items.append(item)
        if item['type'] == 'ring_of_protection':
            self.armor_class += item['armor_class']
        if item['type'] == 'belt_of_giant_strength':
            self.strength += item['strength_bonus']
        if item['type'] == 'amulet_of_heavens':
            pass  # Handled in attack and damage calculations

    def __repr__(self):
        return f"Character({self.name}, Level {self.level}, HP {self.hit_points}, XP {self.experience}, Class {self.class_name}, Race {self.race})"
