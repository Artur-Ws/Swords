import pygame
import os
r = 105
SCREEN_SIZE = (1920, 1080)
WIN = pygame.display.set_mode(SCREEN_SIZE)
FPS = 60
MAIN_COLOR = (105, 93, 79)
BACKGROUND = pygame.transform.scale(pygame.image.load(os.path.join('..', 'assets', 'background.jpg')), SCREEN_SIZE)
pygame.display.set_caption("Axes and Creampies")


def draw_window():
    WIN.blit(BACKGROUND, (0, 0))
    pygame.display.update()


def main():
    clock = pygame.time.Clock()
    run = True
    draw_window()
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pass

    pygame.quit()


if __name__ == "__main__":
    main()
print(type(BACKGROUND))