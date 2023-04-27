import pygame
from debug_log import Debug
from tools import debug_log
from character import Character
from gui.main_menu_gui import MainMenuGui
from gui.fight_module_gui import FightModuleGui
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
        fight_panel = FightModuleGui()
        fight = Fight()
        run = True

        player = Character(500, 500, 'Player', 25, 5, 110)
        enemy = Character(1400, 500, 'Enemy', 10, 5, 100)

        while run:
            Debug(f"Player hp: {player.health_points}")
            Debug(f"Enemy hp: {enemy.health_points}")

            for event in pygame.event.get():
                if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    run = False

                if fight_panel.button_menu.check_for_input(pygame.mouse.get_pos()):
                    self.state = 'main_menu'
                    self.state_manager()

                if fight_panel.attack_button.check_for_input(pygame.mouse.get_pos()):
                    fight.fight_action(player, enemy)

            fight_panel.draw_fight_module_background()
            fight_panel.update()
            fight_panel.check_for_input()
            fight_panel.change_color()

            debug_log()
            pygame.display.update()

        pygame.quit()

    if __name__ == "__fight_module__":
        fight_module()
