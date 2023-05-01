import pygame
from debug_log import Debug


class Character:
    def __init__(self, x, y, name, strength, defense, health_points):
        self.name = name
        self.strength = strength
        self.defense = defense
        self.health_points = health_points
        self.health_points_max = health_points
        self.alive = True
        self.stamina = 100
        self.lowest_stamina_value = 10
        self.regen_stamina_value = 15
        # self.image = pygame.image.load()
        # self.rect = self.image.get_rect()
        # self.rect.center = (x, y)

    def attack(self, target: 'Character'):
        if self.stamina_check():
            damage = max(0, self.strength - target.defense)
            target.get_damage(damage)
            #think about reference of stamina use value depents on type of action, right now it's hardcoded.
            self.stamina_use(10)
            print(f"{self.name} attacks {target.name} for {damage} damage! Your stamina lvl: {self.stamina}")
        else:
            self.rest()
            Debug(f"You're exhausted. Get some sleep. Current stamina lvl: {self.stamina}", 2)

    def get_damage(self, damage):
        self.health_points -= damage
        if self.health_points < 1:
            self.health_points = 0
            self.alive = False
            print(f"{self.name} has been defeated!")
        else:
            print(f"{self.name} takes {damage} damage! {self.health_points} HP left.")

    def describe(self):
        print(f"Name: {self.name}")
        print(f"Strength: {self.strength}")
        print(f"Defense: {self.defense}")
        print(f"Health Points: {self.health_points}")

    def draw(self):
        surface = pygame.display.get_surface()
        surface.blit(self.image, self.rect)

    def stamina_check(self):
        if self.stamina > self.lowest_stamina_value:
            return True
        else:
            return False

    def stamina_use(self, stamina_value):
        self.stamina -= stamina_value

    def rest(self):
        self.stamina += self.regen_stamina_value
