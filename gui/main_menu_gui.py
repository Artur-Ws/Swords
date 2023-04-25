import pygame
import os
from gui.button import Button
import configparser
config = configparser.ConfigParser()
config.read("config.ini")


class MainMenuGui:
    def __init__(self):
        self.screen_width = config.getint("General", "screen_width")
        self.screen_height = config.getint("General", "screen_height")
        self.screen_size = (self.screen_width, self.screen_height)
        self.win = pygame.display.set_mode(self.screen_size)
        self.background = pygame.transform.scale(pygame.image.load(os.path.join('..', 'assets', 'background.jpg')),
                                                 self.screen_size)

        self.button_surface = pygame.image.load(os.path.join('..', 'assets', 'button.png'))
        self.button_surface = pygame.transform.scale(self.button_surface, (300, 100))

        self.button_play = Button(self.button_surface, 960, 300, 960, 300, "play")
        self.button_options = Button(self.button_surface, 960, 450, 960, 450, "options")
        self.button_quit = Button(self.button_surface, 960, 600, 960, 600, "quit")

    def draw_menu_background(self):
        self.win.blit(self.background, (0, 0))

    def update(self):
        self.button_play.update()
        self.button_options.update()
        self.button_quit.update()

    def check_for_input(self):
        self.button_play.check_for_input(pygame.mouse.get_pos())
        self.button_options.check_for_input(pygame.mouse.get_pos())
        self.button_quit.check_for_input(pygame.mouse.get_pos())

    def change_color(self):
        self.button_play.change_color(pygame.mouse.get_pos())
        self.button_options.change_color(pygame.mouse.get_pos())
        self.button_quit.change_color(pygame.mouse.get_pos())
