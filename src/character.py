import random

class Character:
    def __init__(self, name, alignment):
        self.name = name
        self.alignment = alignment
        self.strength = 10
        self.dexterity = 10
        self.constitution = 10
        self.wisdom = 10
        self.intelligence = 10
        self.charisma = 10
        self.experience = 0
        self.level = 1
        self.armor_class = 10 + self.get_modifier(self.dexterity)
        self.hit_points = 5 + self.get_modifier(self.constitution)

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_alignment(self):
        return self.alignment

    def set_alignment(self, alignment):
        self.alignment = alignment

    def get_armor_class(self):
        return self.armor_class

    def get_hit_points(self):
        return self.hit_points
 
    def attack(self, opponent):
        roll = random.randint(1, 20) + self.get_modifier(self.strength)       # add strength modifier to attack roll?
        print(f"Roll: {roll}, Opponent Armor Class: {opponent.get_armor_class()}")
        if roll == 20:
            damage = self.calculate_damage(critical=True)
            opponent.take_damage(damage)
            self.gain_experience(10)
            return True
        elif roll >= opponent.get_armor_class():
            damage = self.calculate_damage()
            opponent.take_damage(damage)
            self.gain_experience(10)
            return True
        return False

    def calculate_damage(self, critical=False):
        damage = 1 + self.get_modifier(self.strength)  ############# more strength means more damage caused to the opponent 
        if critical:
            damage = max(damage * 2, 1)                   
        return max(damage, 1)       

    def take_damage(self, damage):
        self.hit_points -= damage
        if self.hit_points <= 0:
            self.hit_points = 0  # Character is dead

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
        self.hit_points += 5 + self.get_modifier(self.constitution)
        if self.level % 2 == 0:
            self.armor_class += 1

        
