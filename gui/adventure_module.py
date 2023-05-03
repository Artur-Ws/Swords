import pygame
import os
from gui.button import Button
import configparser
config = configparser.ConfigParser()
config.read("config.ini")


class AdventureModuleGui:
    def __init__(self):
        self.screen_width = config.getint("General", "screen_width")
        self.screen_height = config.getint("General", "screen_height")
        self.screen_size = (self.screen_width, self.screen_height)
        self.win = pygame.display.set_mode(self.screen_size)
        self.background = pygame.transform.scale(pygame.image.load(os.path.join('..', 'assets', 'adventure_background.png')),
                                                 self.screen_size)

        self.button_surface = pygame.image.load(os.path.join('..', 'assets', 'button.png'))
        self.button_surface = pygame.transform.scale(self.button_surface, (300, 100))

        self.button_menu = Button(self.button_surface, self.screen_width / 2, 950, 700, 950, "menu")
        self.button_beach = Button(self.button_surface, self.screen_width / 2, 150, 700, 150, "beach")
        self.button_ruins = Button(self.button_surface, 1700, 350, 1700, 350, "ruins")
        self.button_desert = Button(self.button_surface, 200, 300, 200, 300, "desert")
        self.button_cave = Button(self.button_surface, 1750, 700, 1750, 700, "cave")
        self.button_forest = Button(self.button_surface, 200, 750, 200, 750, "forest")

    def draw_fight_module_background(self):
        self.win.blit(self.background, (0, 0))

    def update(self):
        self.button_menu.update()
        self.button_beach.update()
        self.button_ruins.update()
        self.button_desert.update()
        self.button_cave.update()
        self.button_forest.update()

    def check_for_input(self):
        self.button_menu.check_for_input(pygame.mouse.get_pos())
        self.button_beach.check_for_input(pygame.mouse.get_pos())
        self.button_ruins.check_for_input(pygame.mouse.get_pos())
        self.button_desert.check_for_input(pygame.mouse.get_pos())
        self.button_cave.check_for_input(pygame.mouse.get_pos())
        self.button_forest.check_for_input(pygame.mouse.get_pos())

    def change_color(self):
        self.button_menu.change_color(pygame.mouse.get_pos())
        self.button_beach.change_color(pygame.mouse.get_pos())
        self.button_ruins.change_color(pygame.mouse.get_pos())
        self.button_desert.change_color(pygame.mouse.get_pos())
        self.button_cave.change_color(pygame.mouse.get_pos())
        self.button_forest.change_color(pygame.mouse.get_pos())
