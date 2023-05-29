import os
import configparser
import pygame
from gui.button import Button
from gui.bar import Bar

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
        self.rest_button = Button(self.button_surface, self.screen_width / 2, self.screen_height/5, 700, 500, "Rest")
        self.strong_attack_button = Button(self.button_surface, self.screen_width / 2, self.screen_height/3.33, 700, 500,
                                           "Strong attack", "comicsans", 40)
        self.medium_attack_button = Button(self.button_surface, self.screen_width / 2, self.screen_height/2.5, 700, 500,
                                           "Medium attack", "comicsans", 40)
        self.light_attack_button = Button(self.button_surface, self.screen_width / 2, self.screen_height/2, 700, 500,
                                           "Light attack", "comicsans", 40)
        self.button_menu = Button(self.button_surface, self.screen_width / 2, 700, 700, 500, "Menu")
        self.player_image = Button(self.button_surface, 500, 500, 500, 500, "Player")
        self.enemy_image = Button(self.button_surface, 1400, 500, 1400, 500, "Enemy")
        self.player_healthbar = Bar(350, 650, pygame.Color(config.get("Colors", "red_healthbar")),
                                    pygame.Color(config.get("Colors", "green_healthbar")))
        self.player_staminabar = Bar(350, 700, pygame.Color(config.get("Colors", "white_staminabar")),
                                     pygame.Color(config.get("Colors", "orange_staminabar")))
        self.enemy_healthbar = Bar(1250, 650, pygame.Color(config.get("Colors", "red_healthbar")),
                                   pygame.Color(config.get("Colors", "green_healthbar")))
        self.enemy_staminabar = Bar(1250, 700, pygame.Color(config.get("Colors", "white_staminabar")),
                                   pygame.Color(config.get("Colors", "orange_staminabar")))
        self.attack_button_list = [self.strong_attack_button, self.medium_attack_button, self.light_attack_button]
        self.all_button_list = [self.button_menu, self.rest_button, self.strong_attack_button,
                                self.medium_attack_button, self.light_attack_button]

    def draw_fight_module_background(self):
        self.win.blit(self.background, (0, 0))

    def update(self):
        [button.update() for button in self.all_button_list]
        self.player_image.update()
        self.enemy_image.update()

    def check_for_input(self, player: "Character"):
        mouse_pos = pygame.mouse.get_pos()
        if self.stamina_available_check(player):
            [button.check_for_input(mouse_pos) for button in self.all_button_list]
        else:
            self.button_menu.check_for_input(mouse_pos)
            self.rest_button.check_for_input(mouse_pos)

    def change_color(self, player: "Character"):
        mouse_pos = pygame.mouse.get_pos()
        if self.stamina_available_check(player) and \
                not self.stamina_max_lvl_check(player):
            [button.change_color(mouse_pos) for button in self.all_button_list]
        elif self.stamina_available_check(player) and \
                self.stamina_max_lvl_check(player):
            [attack_button.change_color(mouse_pos) for attack_button in self.attack_button_list]
            self.button_menu.change_color(pygame.mouse.get_pos())
            self.rest_button.change_color(pygame.mouse.get_pos(), "black", "black")
        else:
            [attack_button.change_color(mouse_pos, "black", "black") for attack_button in self.attack_button_list]
            self.button_menu.change_color(pygame.mouse.get_pos())
            self.rest_button.change_color(pygame.mouse.get_pos())

    def stamina_available_check(self, player: "Character"):
        if player.stamina > player.lowest_stamina_value:
            return True
        else:
            return False

    def stamina_max_lvl_check(self, player: "Character"):
        if player.stamina == player.stamina_max:
            return True
        else:
            return False
