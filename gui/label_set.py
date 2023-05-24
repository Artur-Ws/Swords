import pygame
import configparser
from pygame.surface import Surface
from pygame.rect import Rect
from label import Label
from typing import List

config = configparser.ConfigParser()
config.read("config.ini")


class LabelSet(Label):
    def __init__(self, x_pos: int, y_pos: int, font: str = "comicsans", font_size: int = 50, item_spacing: int = 50):
        super().__init__(x_pos, y_pos, font, font_size)
        self.item_spacing = item_spacing

    def draw_label_set(self, item_list: List, color: str = config.get("Colors", "label_set_default")) -> None:
        y: int = self.y_pos
        for item in item_list:
            text: Surface = self.__label_font.render(item, True, color, None)
            text_rect: Rect = text.get_rect(center=(self.x_pos, y))
            surface = pygame.display.get_surface()
            surface.blit(text, text_rect)

            y += self.item_spacing
    #pygame.display.flip()
