import pygame
import os
import configparser
from debug_log import Debug
from tools import debug_log
from gui.button import Button
from character import Character
from gui.main_menu_gui import MainMenuGui
from fight import Fight


class GameState:
    def __init__(self):
        self.state = 'main_menu'

    def state_manager(self):
        if self.state == 'main_menu':
            self.main_menu()
        if self.state == 'fight_module':
            self.fight_module()

    def main_menu(self):
        menu = MainMenuGui()
        run = True
        while run:

            for event in pygame.event.get():
                if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    run = False

                if menu.button_play.check_for_input(pygame.mouse.get_pos()):
                    self.state = 'fight_module'
                    self.state_manager()

                if menu.button_options.check_for_input(pygame.mouse.get_pos()):
                    pass

                if menu.button_quit.check_for_input(pygame.mouse.get_pos()):
                    run = False

            menu.draw_menu_background()
            menu.update()
            menu.check_for_input()
            menu.change_color()

            debug_log()
            pygame.display.update()

        pygame.quit()

    def fight_module(self):
        config = configparser.ConfigParser()
        config.read("config.ini")

        screen_width = config.getint("General", "screen_width")
        screen_height = config.getint("General", "screen_height")
        fps = config.getint("General", "FPS")

        screen_size = (screen_width, screen_height)
        win = pygame.display.set_mode(screen_size)
        background = pygame.transform.scale(pygame.image.load(os.path.join('..', 'assets', 'background.jpg')),
                                            screen_size)

        next_stage = GameState

        def draw_window():
            win.blit(background, (0, 0))

        # buttons
        button_surface = pygame.image.load(os.path.join('..', 'assets', 'button.png'))
        button_surface = pygame.transform.scale(button_surface, (300, 100))
        button_menu = Button(button_surface, screen_width / 2, 700, 700, 500, "Menu")

        attack_button = Button(button_surface, screen_width / 2, screen_height / 2, 700, 500, "Attack")

        player_image = Button(button_surface, 500, 500, 500, 500, "Player")
        enemy_image = Button(button_surface, 1400, 500, 1400, 500, "Enemy")

        player = Character(500, 500, 'Player', 25, 5, 110)
        enemy = Character(1400, 500, 'Enemy', 10, 5, 100)

        # importing fight module
        fight = Fight()

        clock = pygame.time.Clock()
        run = True
        while run:
            clock.tick(fps)
            draw_window()
            Debug(f"Player hp: {player.health_points}")
            Debug(f"Enemy hp: {enemy.health_points}")

            for event in pygame.event.get():
                if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    next_stage.main_menu(self)

                if button_menu.check_for_input(pygame.mouse.get_pos()):
                    next_stage.main_menu(self)

                if attack_button.check_for_input(pygame.mouse.get_pos()):
                    fight.fight_action(player, enemy)

                    # if not player.alive or not enemy.alive:
                    #     next_stage.main_menu(self)

            attack_button.change_color(pygame.mouse.get_pos())
            button_menu.change_color(pygame.mouse.get_pos())
            attack_button.update()
            enemy_image.update()
            player_image.update()
            button_menu.update()
            debug_log()
            pygame.display.update()

        pygame.quit()

    if __name__ == "__fight_module__":
        fight_module()


