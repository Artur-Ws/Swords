import pygame

pygame.init()
font = pygame.font.Font(None, 25)


def debug(info, y: int = 10, x: int = 10):
    """
    Displays information on screen for debug purposes. To use for dynamic events (i.e. Show actual mouse position),
    place it in main loop to be updated each frame. For static use (one-time event i.e. Display text after button
    was pressed), set variable with empty string and put this function in main loop with that variable as info argument,
    then change this variable after one-time action was performed (i.e.button has been pressed)

    :param info: Information to be displayed on screen.
    :param y: Y position of displayed text.
    :param x: X position of displayed text.
    :return: None
    """
    surface = pygame.display.get_surface()
    debug_surf = font.render(str(info), True, (255, 255, 255))
    debug_rect = debug_surf.get_rect(topleft=(x, y))
    background = pygame.Surface(debug_rect.size)
    background.set_alpha(80)
    background.fill((0, 0, 0))
    surface.blit(background, debug_rect)
    surface.blit(debug_surf, debug_rect)
