import pygame


class Character:
    def __init__(self, x, y, name, strength, defense, health_points):
        self.name = name
        self.strength = strength
        self.defense = defense
        self.health_points = health_points
        self.health_points_max = health_points
        self.alive = True
        # self.image = pygame.image.load()
        # self.rect = self.image.get_rect()
        # self.rect.center = (x, y)

    def attack(self, target: 'Character'):
        damage = max(0, self.strength - target.defense)

        target.get_damage(damage)
        print(f"{self.name} attacks {target.name} for {damage} damage!")

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
