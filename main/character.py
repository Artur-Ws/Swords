import configparser
import pygame
from enum import Enum
from random import randint
from debug_log import Debug

config = configparser.ConfigParser()
config.read("config.ini")


class Character:
    def __init__(self, x: int, y: int, name: str, strength: int, defense: int, health_points: int, attack: int):
        self.name = name
        self.strength = strength
        self.defense = defense
        self.health_points = health_points
        self.attack = attack
        self.health_points_max = health_points
        self.alive: bool = True
        self.stamina: int = config.getint("CharacterSetting", "init_stamina_value")
        self.stamina_max: int = config.getint("CharacterSetting", "init_max_stamina_value")
        self.lowest_stamina_value: int = config.getint("CharacterSetting", "lowest_stamina_value")
        self.regen_stamina_value: int = config.getint("CharacterSetting", "regen_stamina_value")
        self.strong_attack_stamina_use: int = config.getint("CharacterSetting", "strong_attack_stamina_use")
        self.medium_attack_stamina_use: int = config.getint("CharacterSetting", "strong_attack_stamina_use")
        self.light_attack_stamina_use: int = config.getint("CharacterSetting", "strong_attack_stamina_use")
        self.light_attack_multiplier: float = config.getfloat("FightSettings", "light_attack_multiplier")
        self.medium_attack_multiplier: float = config.getfloat("FightSettings", "medium_attack_multiplier")
        self.strong_attack_multiplier: float = config.getfloat("FightSettings", "strong_attack_multiplier")
        # self.image = pygame.image.load()
        # self.rect = self.image.get_rect()
        # self.rect.center = (x, y)

    def attack_action(self, target: 'Character', attack_type_name: 'AttackTypeNames') -> None:
        if attack_type_name == "strong_attack":
            self.type_attack_action(target, attack_type_name)
        if attack_type_name == "medium_attack":
            self.type_attack_action(target, attack_type_name)
        if attack_type_name == "light_attack":
            self.type_attack_action(target, attack_type_name)

    def type_attack_action(self, target: 'Character', attack_type_name: 'AttackTypeNames') -> None:
        if self.stamina_check():
            if self.is_blocked(target, attack_type_name):
                self.stamina_use(attack_type_name)
                print(f"{target.name} blocked attack ")
                pass
            else:
                damage = self.damage_attack_type(attack_type_name)
                target.get_damage(damage)
                self.stamina_use(attack_type_name)
                print(f"{self.name} attacks {target.name} for {damage} damage! Your stamina lvl: {self.stamina}")
        else:
            self.rest()
            Debug(f"{self.name}'s exhaust. Get some sleep. Current stamina lvl: {self.stamina}", 1)

    def damage_attack_type(self, attack_type_name: 'AttackTypeNames') -> int:
        if attack_type_name == "strong_attack":
            damage_type_attack = self.base_damage() * self.strong_attack_multiplier
        if attack_type_name == "medium_attack":
            damage_type_attack = self.base_damage() * self.medium_attack_multiplier
        if attack_type_name == "light_attack":
            damage_type_attack = self.base_damage() * self.light_attack_multiplier
        damage_type_attack = round(damage_type_attack)
        return damage_type_attack

    def get_damage(self, damage: int) -> None:
        self.health_points -= damage
        if self.health_points < 1:
            self.health_points = 0
            self.alive = False
            print(f"{self.name} has been defeated!")
        else:
            print(f"{self.name} takes {damage} damage! {self.health_points} HP left.")

    def describe(self) -> None:
        print(f"Name: {self.name}")
        print(f"Strength: {self.strength}")
        print(f"Defense: {self.defense}")
        print(f"Health Points: {self.health_points}")

    def draw(self) -> None:
        surface = pygame.display.get_surface()
        surface.blit(self.image, self.rect)

    def stamina_check(self) -> bool:
        if self.stamina > self.lowest_stamina_value:
            return True
        else:
            return False

    def stamina_use(self, attack_type_name: 'AttackTypeNames') -> None:
        if attack_type_name == "strong_attack":
            self.stamina -= self.strong_attack_stamina_use
        if attack_type_name == "medium_attack":
            self.stamina -= self.medium_attack_stamina_use
        if attack_type_name == "light_attack":
            self.stamina -= self.light_attack_stamina_use

    def rest(self) -> None:
        if self.stamina + self.regen_stamina_value <= self.stamina_max:
            self.stamina += self.regen_stamina_value
        else:
            self.stamina = self.stamina_max

    def select_chance_draw(self, first_number_of_draw=1, last_number_of_draw=1000) -> int:
        chance_draw = randint(first_number_of_draw, last_number_of_draw)
        return chance_draw

    def base_damage(self) -> float:
        base_damage = self.strength * (1 + self.select_chance_draw(-10, 10)/100)
        return base_damage

    def defense_attack_difference(self, opponent: 'Character') -> int:
        difference_of_defense_attack = opponent.defense - self.attack
        return difference_of_defense_attack

    def function_of_block_chance(self, opponent: 'Character', attack_type_name: 'AttackTypeNames') -> float:
        base_attack_block_chance = config.getint("FightSettings", "equal_block_attack_attack_chance") + \
                           self.defense_attack_difference(opponent) * \
                           config.getint("FightSettings", "one_point_difference_of_block_attack")
        if attack_type_name == "strong_attack":
            block_chance = base_attack_block_chance + \
                           config.getint("FightSettings", "difference_chance_between_attack_type")
        if attack_type_name == "medium_attack":
            block_chance = base_attack_block_chance
        if attack_type_name == "light_attack":
            block_chance = base_attack_block_chance - \
                           config.getint("FightSettings", "difference_chance_between_attack_type")
        return block_chance

    def is_blocked(self, opponent: 'Character', attack_type_name: 'AttackTypeNames') -> bool:
        if self.select_chance_draw() < self.function_of_block_chance(opponent, attack_type_name):
            Debug(f"{opponent.name} blocked attack!", 1)
            return True
        else:
            return False


class AttackTypeNames(Enum):
    strong_attack = "strong_attack"
    medium_attack = "medium_attack"
    light_attack = "light_attack"
