import pygame
import os
from gui.button import Button

button_surface = pygame.image.load(os.path.join('..', 'assets', 'button.png'))
button_surface = pygame.transform.scale(button_surface, (300, 100))

button_play = Button(button_surface, 960, 300, "play")
button_option = Button(button_surface, 960, 450, "options")
button_quit = Button(button_surface, 960, 600, "quit")


def button_update():
    button_play.update()
    button_quit.update()
    button_option.update()


def button_check_for_input():
    button_play.check_for_input(pygame.mouse.get_pos())
    button_quit.check_for_input(pygame.mouse.get_pos())
    button_option.check_for_input(pygame.mouse.get_pos())


def button_change_color():
    button_play.change_color(pygame.mouse.get_pos())
    button_quit.change_color(pygame.mouse.get_pos())
    button_option.change_color(pygame.mouse.get_pos())
