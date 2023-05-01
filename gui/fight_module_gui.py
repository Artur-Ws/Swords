import pygame
import os
from gui.button import Button
from gui.bar import Bar
import configparser
#from main.character import Character
config = configparser.ConfigParser()
config.read("config.ini")


class FightModuleGui:
    def __init__(self):
        self.screen_width = config.getint("General", "screen_width")
        self.screen_height = config.getint("General", "screen_height")
        self.screen_size = (self.screen_width, self.screen_height)
        self.win = pygame.display.set_mode(self.screen_size)
        self.background = pygame.transform.scale(pygame.image.load(os.path.join('..', 'assets', 'background.jpg')),
                                                 self.screen_size)

        self.button_surface = pygame.image.load(os.path.join('..', 'assets', 'button.png'))
        self.button_surface = pygame.transform.scale(self.button_surface, (300, 100))

        self.button_menu = Button(self.button_surface, self.screen_width / 2, 700, 700, 500, "Menu")
        self.attack_button = Button(self.button_surface, self.screen_width / 2, self.screen_height / 2, 700, 500, "Attack")
        self.rest_button = Button(self.button_surface,self.screen_width / 2, self.screen_height / 2.5, 700, 500, "Rest" )
        self.player_image = Button(self.button_surface, 500, 500, 500, 500, "Player")
        self.enemy_image = Button(self.button_surface, 1400, 500, 1400, 500, "Enemy")
        self.player_healthbar = Bar(350, 650, pygame.Color(config.get("Colors", "red")),
                                    pygame.Color(config.get("Colors", "green")))
        self.enemy_healthbar = Bar(1250, 650, pygame.Color(config.get("Colors", "red")),
                                   pygame.Color(config.get("Colors", "green")))

    def draw_fight_module_background(self):
        self.win.blit(self.background, (0, 0))

    def update(self):
        self.button_menu.update()
        self.attack_button.update()
        self.player_image.update()
        self.enemy_image.update()
        self.rest_button.update()

    def check_for_input(self, stamina, lowest_stamina_value):
        if self.stamina_available_check(stamina, lowest_stamina_value):
            self.button_menu.check_for_input(pygame.mouse.get_pos())
            self.attack_button.check_for_input(pygame.mouse.get_pos())
            self.rest_button.check_for_input(pygame.mouse.get_pos())
        else:
            self.button_menu.check_for_input(pygame.mouse.get_pos())
            self.rest_button.check_for_input(pygame.mouse.get_pos())

    def change_color(self, stamina, lowest_stamina_value):
        if self.stamina_available_check(stamina, lowest_stamina_value):
            self.button_menu.change_color(pygame.mouse.get_pos())
            self.attack_button.change_color(pygame.mouse.get_pos())
            self.rest_button.change_color(pygame.mouse.get_pos())
        else:
            self.button_menu.change_color(pygame.mouse.get_pos())
            self.attack_button.change_color(pygame.mouse.get_pos(), "black", "black")
            self.rest_button.change_color(pygame.mouse.get_pos())

    def stamina_available_check(self, stamina, lowest_stamina_value):
        if stamina > lowest_stamina_value:
            return True
        else:
            return False
