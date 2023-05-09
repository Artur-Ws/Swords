import pygame


class Label():
    def __init__(self, x_pos, y_pos, text_input, font="comicsans", font_size=50, colour ="yellow"):

        self.x_pos = x_pos
        self.y_pos = y_pos
        self.font = font
        self.font_size = font_size
        self.text_input = text_input
        self.__button_font = pygame.font.SysFont(self.font, self.font_size)
        self.text = self.__button_font.render(self.text_input, True, colour, None)
        self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

    def draw_label(self):
        surface = pygame.display.get_surface()
        surface.blit(self.text, self.text_rect)