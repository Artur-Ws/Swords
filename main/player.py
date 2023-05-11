import pygame
from character import Character


class Player(Character):
    def __init__(self, x, y, name, strength, defense, health_points):
        super().__init__(x, y, name, strength, defense, health_points)
        self.backpack = []
        self.backpack_size = 4
        self.level = 1
        self.experience = 0
        self.experience_needed = 100
        self.attribiute_points = 10
        self.money = 12345

    def add_to_backpack(self, item):
        if len(self.backpack) < self.backpack_size:
            self.backpack.append(item)
        else:
            print("Backpack is full")

    def remove_from_backpack(self, item):
        if item in self.backpack:
            self.backpack.remove(item)
            print(f"{item} removed from backpack")
        else:
            print(f"{item} not found in backpack")

    def expand_backpack(self):
        self.backpack_size += 1
        print(f"Backpack size has increased to {self.backpack_size}")

    def gain_experience(self, gained_experience):
        self.experience += gained_experience
        if self.experience >= self.experience_needed:
            self.level_up()

    def level_up(self):
        self.level += 1
        self.experience_needed = int(self.experience_needed * 1.2)
        print(f"Your actual level: {self.level}")

