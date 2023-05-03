import pygame
import os
from gui.button import Button
import configparser
config = configparser.ConfigParser()
config.read("config.ini")


class ActivityModuleGui:
    def __init__(self):
        self.screen_width = config.getint("General", "screen_width")
        self.screen_height = config.getint("General", "screen_height")
        self.screen_size = (self.screen_width, self.screen_height)
        self.win = pygame.display.set_mode(self.screen_size)
        self.background = pygame.transform.scale(pygame.image.load(os.path.join('..', 'assets', 'activity_background.png')),
                                                 self.screen_size)

        self.button_surface = pygame.image.load(os.path.join('..', 'assets', 'button.png'))
        self.button_surface = pygame.transform.scale(self.button_surface, (300, 100))

        self.button_menu = Button(self.button_surface, self.screen_width / 2, 900, 700, 900, "menu")
        self.button_adventure = Button(self.button_surface, self.screen_width / 2, 200, 700, 200, "adventure")
        self.button_smithy = Button(self.button_surface, 400, 700, 400, 500, "smithy")
        self.button_temple = Button(self.button_surface, 1300, 600, 1300, 600, "temple")
        self.button_inn = Button(self.button_surface, 1450, 800, 1450, 800, "inn")

    def draw_fight_module_background(self):
        self.win.blit(self.background, (0, 0))

    def update(self):
        self.button_menu.update()
        self.button_adventure.update()
        self.button_smithy.update()
        self.button_temple.update()
        self.button_inn.update()

    def check_for_input(self):
        self.button_menu.check_for_input(pygame.mouse.get_pos())
        self.button_adventure.check_for_input(pygame.mouse.get_pos())
        self.button_smithy.check_for_input(pygame.mouse.get_pos())
        self.button_temple.check_for_input(pygame.mouse.get_pos())
        self.button_inn.check_for_input(pygame.mouse.get_pos())

    def change_color(self):
        self.button_menu.change_color(pygame.mouse.get_pos())
        self.button_adventure.change_color(pygame.mouse.get_pos())
        self.button_smithy.change_color(pygame.mouse.get_pos())
        self.button_temple.change_color(pygame.mouse.get_pos())
        self.button_inn.change_color(pygame.mouse.get_pos())
