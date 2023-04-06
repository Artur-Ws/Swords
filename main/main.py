import pygame
import os
from debug_log import debug

SCREEN_SIZE = (1920, 1030)
WIN = pygame.display.set_mode(SCREEN_SIZE)
FPS = 60
MAIN_COLOR = (105, 93, 79)
BACKGROUND = pygame.transform.scale(pygame.image.load(os.path.join('..', 'assets', 'background.jpg')), SCREEN_SIZE)
pygame.display.set_caption("Axes and Creampies")


def draw_window():
    WIN.blit(BACKGROUND, (0, 0))


def main():
    clock = pygame.time.Clock()
    run = True
    static_log = ""
    while run:
        clock.tick(FPS)
        draw_window()

        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                run = False

        debug(static_log)
        pygame.display.update()
    pygame.quit()


if __name__ == "__main__":
    main()
