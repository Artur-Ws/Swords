import pygame

from character import Character


class Player(Character):
    def __init__(self, x, y, name: str, strength: int, defense: int, health_points: int):
        super().__init__(x, y, name, strength, defense, health_points)
        self.backpack: list = []
        self.backpack_size: int = 12
        self.level: int = 1
        self.experience: int = 0
        self.experience_needed: int = 100
        self.attribiute_points: int = 10
        self.money: int = 0

    def add_to_backpack(self, item):
        if len(self.backpack) < self.backpack_size:
            self.backpack.append(item)
        else:
            print("Backpack is full")

    def remove_from_backpack(self, item):
        if item in self.backpack:
            self.backpack.remove(item)

    def gain_experience(self, sum_of_enemys_stats: int) -> None:
        self.experience += sum_of_enemys_stats
        while self.experience >= self.experience_needed:
            self.experience -= self.experience_needed
            self.level_up()

    def level_up(self):
        self.level += 1
        self.experience_needed = int(self.experience_needed * 1.2)
        self.health_points_max += 10
        self.health_points = self.health_points_max
