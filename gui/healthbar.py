import pygame


class Bar():

    def __init__(self, x, y, hp, max_hp):
        self.x = x
        self.y = y
        self.hp = hp
        self.max_hp = max_hp

    def draw(self, hp, screen, colour_of_background_bar, colour_of_front_bar):
        self.hp = hp
        ratio = self.hp / self.max_hp
        pygame.draw.rect(screen, colour_of_background_bar, (self.x, self.y, 150, 20))
        pygame.draw.rect(screen, colour_of_front_bar, (self.x, self.y, 150 * ratio, 20))
