import pygame


class Label:
    def __init__(self, x_pos, y_pos, font="comicsans", font_size=50):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.font = font
        self.font_size = font_size
        self.__button_font = pygame.font.SysFont(self.font, self.font_size)

    def draw_label(self, text_input, color ="yellow"):
        text = self.__button_font.render(text_input, True, color, None)
        text_rect = text.get_rect(center=(self.x_pos, self.y_pos))
        surface = pygame.display.get_surface()
        surface.blit(text, text_rect)