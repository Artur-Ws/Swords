import pygame
import os
import sys


class Button():
    def __init__(self, image, x_pos, y_pos, text_input):
        self.image = image
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.rect = self.image.get_rect(center=(self.x_pos,self.y_pos))
        self.text_input = text_input
        self.__button_font = pygame.font.SysFont("Lobster", 50)
        self.text = self.__button_font.render(self.text_input, True, [5, 5, 5])
        self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

    def update(self):
        surface = pygame.display.get_surface()
        surface.blit(self.image, self.rect)
        surface.blit(self.text, self.text_rect)

    def check_for_input(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top,
                                                                                          self.rect.bottom):
            print("Button Press!")

    def change_color(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top,
                                                                                          self.rect.bottom):
            self.text = self.__button_font.render(self.text_input, True, "yellow")
        else:
            self.text = self.__button_font.render(self.text_input, True, "white")

