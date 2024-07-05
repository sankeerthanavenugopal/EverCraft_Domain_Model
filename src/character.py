# src/character.py
class Character:
    def __init__(self, name, alignment):
        self.name = name
        self.alignment = alignment

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_alignment(self):
        return self.alignment

    def set_alignment(self, alignment):
        self.alignment = alignment
