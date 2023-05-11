import pygame

from character import Character


class Player(Character):
    def __init__(self, x, y, name, strength, defense, health_points):
        super().__init__(x, y, name, strength, defense, health_points)
        self.backpack = []
        self.backpack_size = 12
        self.level = 1
        self.experience = 0
        self.experience_needed = 100
        self.attribiute_points = 10
        self.money = 0

    def add_to_backpack(self, item):
        if len(self.backpack) < self.backpack_size:
            self.backpack.append(item)
        else:
            print("Backpack is full")

    def remove_from_backpack(self, item):
        if item in self.backpack:
            self.backpack.remove(item)

    def gain_experience(self, sum_of_enemys_stats):
        self.experience += sum_of_enemys_stats
        while self.experience >= self.experience_needed:
            self.experience -= self.experience_needed
            self.level_up()

    def level_up(self):
        self.level += 1
        self.experience_needed = int(self.experience_needed * 1.2)
        self.strength += 2
        self.defense += 2
        self.health_points_max += 10
        self.health_points = self.health_points_max
