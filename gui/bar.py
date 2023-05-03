import pygame


class Bar:
    def __init__(self, x, y, colour_of_background_bar, colour_of_front_bar):
        self.x = x
        self.y = y
        self.colour_of_background_bar = colour_of_background_bar
        self.colour_of_front_bar = colour_of_front_bar
        self.screen = pygame.display.get_surface()
    def draw(self, points, max_points):
        ratio = points / max_points
        pygame.draw.rect(self.screen, self.colour_of_background_bar, (self.x, self.y, 150, 20))
        pygame.draw.rect(self.screen, self.colour_of_front_bar, (self.x, self.y, 150 * ratio, 20))