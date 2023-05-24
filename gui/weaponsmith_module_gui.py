import pygame
import os
from gui.button import Button
from gui.label import Label
from gui.label_set import LabelSet
import configparser

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

        self.label_weapon = Label(500, 100, font_size=40)
        self.label_weapon_price = Label(350, 200, font_size=30)
        self.label_weapon_damage = Label(600, 200, font_size=30)
        self.label_set_weapons_lev0 = LabelSet(100, 300, font_size=30)

        self.label_armour = Label(1550, 100, font_size=40)
        self.label_armour_price = Label(1400, 200, font_size=30)
        self.label_armour_defence = Label(1700, 200, font_size=30)

        self.label_gold = Label(1000, 900)
        self.label_backpack = Label(200, 700, font_size=30)
        self.label_set_backpack_items = LabelSet(200, 750)

    def draw_weaponsmith_module_background(self):
        self.win.blit(self.background, (0, 0))

    def update(self):
        self.button_exit.update()
        self.label_armour.draw_label("ARMOUR", color="#0AA80D")
        self.label_armour_price.draw_label("price:")
        self.label_armour_defence.draw_label("defence:")
        self.label_weapon.draw_label("WEAPON", color="#0AA80D")
        self.label_weapon_price.draw_label("price:")
        self.label_weapon_damage.draw_label("damage:")
        self.label_backpack.draw_label("Backpack: ", color="#0AA80D")

    def check_for_input(self):
        self.button_exit.check_for_input(pygame.mouse.get_pos())

    def change_color(self):
        self.button_exit.change_color(pygame.mouse.get_pos())
