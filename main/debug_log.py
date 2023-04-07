import pygame
import configparser
from tools import debug_refs
from time import time

config = configparser.ConfigParser()
config.read("config.ini")
FPS = config.getint("General", "FPS")

pygame.init()
font = pygame.font.Font(None, 25)


class Debug:
    def __init__(self, info, period: int = 0):
        super(Debug, self).__init__()
        self.info = info
        self.period = period
        self.y = 17
        self.x = 10
        self.font_color = (255, 255, 255)
        self.opacity = 80
        self.bg_color = (0, 0, 0)
        self.font = pygame.font.Font(None, 25)
        self.init_time = time()
        debug_refs.append(self)
        self.time_per_frame = 1/FPS

    def log_info(self, number):
        surface = pygame.display.get_surface()
        debug_surf = self.font.render(str(self.info), True, self.font_color)
        debug_rect = debug_surf.get_rect(topleft=(self.x, self.y * (number + 1)))
        background = pygame.Surface(debug_rect.size)
        background.set_alpha(self.opacity)
        background.fill(self.bg_color)
        surface.blit(background, debug_rect)
        surface.blit(debug_surf, debug_rect)

    def remove_if_expired(self):
        current_time = time()
        if self.period == 0 and self in debug_refs:
            debug_refs.remove(self)
        elif self.init_time < current_time - self.period and self in debug_refs:
            debug_refs.remove(self)
