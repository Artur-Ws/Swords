import pygame
import os
from gui.button import Button
from gui.label import Label
import configparser
from player import Player

player = Player(500, 500, 'Player', 25, 5, 110)

config = configparser.ConfigParser()
config.read("config.ini")


class WeaponsmithGui:
    def __init__(self):
        self.screen_width = config.getint("General", "screen_width")
        self.screen_height = config.getint("General", "screen_height")
        self.screen_size = (self.screen_width, self.screen_height)
        self.win = pygame.display.set_mode(self.screen_size)
        self.background = pygame.transform.scale(pygame.image.load(os.path.join('..', 'assets',
                                                                                'weaponsmith_background.png')),
                                                 self.screen_size)

        self.button_surface = pygame.image.load(os.path.join('..', 'assets', 'button.png'))
        self.button_surface = pygame.transform.scale(self.button_surface, (300, 100))

        self.button_exit = Button(self.button_surface, 1600, 900, 1600, 900, "exit")
        self.button_something = Button(self.button_surface, self.screen_width / 2, 200, 700, 200, "something")
        self.label_gold = Label( self.screen_width / 2, 500,  f"GOLD: {player.money}")

    def draw_fight_module_background(self):
        self.win.blit(self.background, (0, 0))

    def update(self):
        self.button_exit.update()
        self.button_something.update()
        self.label_gold.draw_label()

    def check_for_input(self):
        self.button_exit.check_for_input(pygame.mouse.get_pos())
        self.button_something.check_for_input(pygame.mouse.get_pos())

    def change_color(self):
        self.button_exit.change_color(pygame.mouse.get_pos())
        self.button_something.change_color(pygame.mouse.get_pos())

