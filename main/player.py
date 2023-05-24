import pygame

from character import Character

import configparser
config = configparser.ConfigParser()
config.read("config.ini")


class Player(Character):
    def __init__(self, x: int, y: int, name: str, strength: int, defense: int, health_points: int, attack: int):
        super().__init__(x, y, name, strength, defense, health_points, attack)
        self.level: int = config.getint("Player Settings", "starting_level")
        self.experience: int = config.getint("Player Settings", "starting_experience")
        self.experience_needed: int = config.getint("Player Settings", "starting_exp_needed_for_next_level")
        self.attribiute_points: int = config.getint("Player Settings", "starting_attribute_points")
        self.money: int = config.getint("Player Settings", "starting_money")
        self.backpack: list = []
        self.backpack_size: int = config.getint("Player Settings", "backpack_size")

    def add_to_backpack(self, item) -> None:
        if len(self.backpack) < self.backpack_size:
            self.backpack.append(item)
        else:
            print("Backpack is full")

    def remove_from_backpack(self, item) -> None:
        if item in self.backpack:
            self.backpack.remove(item)

    def gain_experience(self, sum_of_enemys_stats: int) -> None:
        self.experience += sum_of_enemys_stats
        while self.experience >= self.experience_needed:
            self.experience -= self.experience_needed
            self.level_up()

    def level_up(self) -> None:
        self.level += 1
        self.experience_needed *= config.getint("Player Settings", "exp_needed_multiplier")
        self.health_points_max += config.getint("Player Settings", "max_hp_added")
        self.health_points = self.health_points_max
