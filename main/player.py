import pygame
from character import Character

class Player(Character):
    def __init__(self, x, y, name, strength, defense, health_points):
        super().__init__(x, y, name, strength, defense, health_points)
        self.backpack = []
        self.backpack_size = 4
        self.level = 1
        self.experience = 0
        self.experience_needed
        self.attribiute_points
        self.money = 0


    def consume

    def add_to_backpack(self, item):
        if len(self.backpack) < self.backpack_size:
            self.backpack.append(item)
        else:
            print("Backpack is full")


    def remove_from_backpack(self, item):
        is_item = False
        for i in self.backpack:
            if i == item:
                self.backpack.remove(item)
                is_item = True
        print(f"{item} removed from backpack")
        if not is_item:
            print(f"{item} not found in backpack")


    def expand_backpack(self):
        self.backpack_size += 1

    def gain_epxerience

