import pygame
from pygame.surface import Surface
from pygame.rect import Rect
from pygame.font import Font
from typing import Tuple


class Button:
    def __init__(self, image, x_pos: int, y_pos: int, hitbox_x_pos: int, hitbox_y_pos: int, text_input: str,
                 font: str = "comicsans", font_size: int = 50):
        self.image: Surface = image
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.hitbox_x_pos = hitbox_x_pos
        self.hitbox_y_pos = hitbox_y_pos
        self.font = font
        self.font_size: int = font_size
        self.rect: Rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
        self.text_input = text_input
        self.__button_font: Font = pygame.font.SysFont(self.font, self.font_size)
        self.text: Surface = self.__button_font.render(self.text_input, True, [5, 5, 5])
        self.text_rect: Rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

    def update(self) -> None:
        surface = pygame.display.get_surface()
        surface.blit(self.image, self.rect)
        surface.blit(self.text, self.text_rect)

    def check_for_input(self, position: Tuple[int, int]) -> bool:
        left_click = pygame.mouse.get_pressed()[0]
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top,
                                                                                          self.rect.bottom) and \
                left_click:
            return True

    def change_color(self, position: Tuple[int, int], color_default: str ="white", color_hovered: str ="green") -> None:
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top,
                                                                                          self.rect.bottom):
            self.text = self.__button_font.render(self.text_input, True, color_hovered)
        else:
            self.text = self.__button_font.render(self.text_input, True, color_default)
