import pygame


class Bar:
    def __init__(self, x, y, max_points, colour_of_background_bar, colour_of_front_bar):
        self.x = x
        self.y = y
        self.max_points = max_points
        self.colour_of_background_bar = colour_of_background_bar
        self.colour_of_front_bar = colour_of_front_bar
        self.screen = pygame.display.get_surface()
    def draw(self, points):
        ratio = points / self.max_points
        pygame.draw.rect(self.screen, colour_of_background_bar, (self.x, self.y, 150, 20))
        pygame.draw.rect(self.screen, colour_of_front_bar, (self.x, self.y, 150 * ratio, 20))
