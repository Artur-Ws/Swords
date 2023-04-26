import pygame


class Bar():
    def __init__(self, x, y, points, max_points):
        self.x = x
        self.y = y
        self.points = points
        self.max_points = max_points

    def draw(self, points, screen, colour_of_background_bar, colour_of_front_bar):
        self.points = points
        ratio = self.points / self.max_points
        pygame.draw.rect(screen, colour_of_background_bar, (self.x, self.y, 150, 20))
        pygame.draw.rect(screen, colour_of_front_bar, (self.x, self.y, 150 * ratio, 20))
