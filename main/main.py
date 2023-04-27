import pygame
import configparser
from Game_State import GameState

config = configparser.ConfigParser()
config.read("config.ini")

FPS = config.getint("General", "FPS")
title = config.get("General", "title")
pygame.display.set_caption(title)

starting_screen = GameState()


def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        starting_screen.state_manager()

    pygame.quit()


if __name__ == "__main__":
    main()
