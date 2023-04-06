import pygame

pygame.init()
font = pygame.font.Font(None, 25)


def debug(info, y=10, x=10):
    surface = pygame.display.get_surface()
    debug_surf = font.render(str(info), True, (255, 255, 255))
    debug_rect = debug_surf.get_rect(topleft=(x, y))
    background = pygame.Surface(debug_rect.size)
    background.set_alpha(80)
    background.fill((0, 0, 0))
    surface.blit(background, debug_rect)
    surface.blit(debug_surf, debug_rect)
