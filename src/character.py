import random
class Character:
    def __init__(self, name, alignment):
        self.name = name
        self.alignment = alignment
        self.armor_class = 10
        self.hit_points = 5

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
        roll = random.randint(1, 20)
        print(roll)
        if roll == 20 or roll >= opponent.get_armor_class():
            return True  # Successful attack
        return False  # Unsuccessful attack

