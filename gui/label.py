import pygame
from pygame.surface import Surface
from pygame.rect import Rect
from pygame.font import Font

class Label:
    def __init__(self, x_pos: int, y_pos: int, font: str = "comicsans", font_size: int = 50):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.font = font
        self.font_size = font_size
        self.__label_font: Font = pygame.font.SysFont(self.font, self.font_size)

    def draw_label(self, text_input: str, color: str ="yellow") -> None:
        text: Surface = self.__label_font.render(text_input, True, color, None)
        text_rect: Rect = text.get_rect(center=(self.x_pos, self.y_pos))
        surface = pygame.display.get_surface()
        surface.blit(text, text_rect)