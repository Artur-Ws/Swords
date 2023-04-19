import pygame

pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

background_color = (255, 255, 255)

health_bar_color = (255, 0, 0)

health_bar_width = 200
health_bar_height = 20
health_bar_x = screen_width / 2 - health_bar_width / 2
health_bar_y = screen_height - 50

health = 100

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.fill(background_color)

    pygame.draw.rect(screen, health_bar_color, (health_bar_x, health_bar_y, health * health_bar_width / 100, health_bar_height))

    pygame.display.flip()
