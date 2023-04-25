import pygame
import os
import configparser
from debug_log import Debug
from tools import debug_log
from Game_State import GameState

config = configparser.ConfigParser()
config.read("config.ini")

screen_width = config.getint("General", "screen_width")
screen_height = config.getint("General", "screen_height")
FPS = config.getint("General", "FPS")
title = config.get("General", "title")

SCREEN_SIZE = (screen_width, screen_height)
WIN = pygame.display.set_mode(SCREEN_SIZE)
BACKGROUND = pygame.transform.scale(pygame.image.load(os.path.join('..', 'assets', 'background.jpg')), SCREEN_SIZE)
pygame.display.set_caption(title)

starting_screen = GameState()


def draw_window():
    WIN.blit(BACKGROUND, (0, 0))


def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        starting_screen.state_manager()

        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                run = False

        debug_log()
        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()
