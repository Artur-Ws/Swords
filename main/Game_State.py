import pygame
from debug_log import Debug
from tools import debug_log
from character import Character
from gui.main_menu_gui import MainMenuGui
from gui.fight_module_gui import FightModuleGui
from fight import Fight
from gui.activity_module import ActivityModuleGui
from gui.adventure_module import AdventureModuleGui


class GameState:
    def __init__(self):
        self.state = 'main_menu'

    def state_manager(self):
        if self.state == 'main_menu':
            self.main_menu()
        if self.state == 'activity_module':
            self.activity_module()
        if self.state == 'adventure_module':
            self.adventure_module()
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
                    self.state = 'activity_module'
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
    def activity_module(self):
        activity_panel = ActivityModuleGui()
        run = True
        while run:

            for event in pygame.event.get():
                if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    run = False

                if activity_panel.button_adventure.check_for_input(pygame.mouse.get_pos()):
                    pass
                    self.state = 'adventure_module'
                    self.state_manager()

                if activity_panel.button_menu.check_for_input(pygame.mouse.get_pos()):
                    self.state = 'main_menu'
                    self.state_manager()

                if activity_panel.button_smithy.check_for_input(pygame.mouse.get_pos()):
                    pass

                if activity_panel.button_temple.check_for_input(pygame.mouse.get_pos()):
                    pass

                if activity_panel.button_inn.check_for_input(pygame.mouse.get_pos()):
                    pass

            activity_panel.draw_fight_module_background()
            activity_panel.update()
            activity_panel.check_for_input()
            activity_panel.change_color()

            debug_log()
            pygame.display.update()

        pygame.quit()

    def adventure_module(self):
        adventure_panel = AdventureModuleGui()
        run = True
        while run:

            for event in pygame.event.get():
                if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    run = False

                if adventure_panel.button_menu.check_for_input(pygame.mouse.get_pos()):
                    self.state = 'main_menu'
                    self.state_manager()

                if adventure_panel.button_beach.check_for_input(pygame.mouse.get_pos()):
                    self.state = 'fight_module'
                    self.state_manager()

                if adventure_panel.button_ruins.check_for_input(pygame.mouse.get_pos()):
                    self.state = 'fight_module'
                    self.state_manager()

                if adventure_panel.button_desert.check_for_input(pygame.mouse.get_pos()):
                    self.state = 'fight_module'
                    self.state_manager()

                if adventure_panel.button_cave.check_for_input(pygame.mouse.get_pos()):
                    self.state = 'fight_module'
                    self.state_manager()

                if adventure_panel.button_forest.check_for_input(pygame.mouse.get_pos()):
                    self.state = 'fight_module'
                    self.state_manager()

            adventure_panel.draw_fight_module_background()
            adventure_panel.update()
            adventure_panel.check_for_input()
            adventure_panel.change_color()

            debug_log()
            pygame.display.update()

        pygame.quit()
    def fight_module(self):
        fight_panel = FightModuleGui()
        fight = Fight()
        player = Character(500, 500, 'Player', 25, 5, 1110)
        enemy = Character(1400, 500, 'Enemy', 10, 5, 1100)
        run = True

        while run:
            Debug(f"Player hp: {player.health_points}")
            Debug(f"Player stamina: {player.stamina}")
            Debug(f"Enemy hp: {enemy.health_points}")
            Debug(f"Enemy stamina: {enemy.stamina}")
            Debug(pygame.mouse.get_pos())

            for event in pygame.event.get():
                if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    run = False

                if fight_panel.button_menu.check_for_input(pygame.mouse.get_pos()):
                    self.state = 'main_menu'
                    self.state_manager()

                if fight_panel.stamina_available_check(player.stamina, player.lowest_stamina_value):
                        if fight_panel.attack_button.check_for_input(pygame.mouse.get_pos()):
                            fight.fight_action(player, enemy)

                if fight_panel.rest_button.check_for_input(pygame.mouse.get_pos()):
                    fight.rest_action(player, enemy)

            fight_panel.draw_fight_module_background()
            fight_panel.update()
            fight_panel.check_for_input(player.stamina, player.lowest_stamina_value)
            fight_panel.change_color(player.stamina, player.lowest_stamina_value)

            fight_panel.player_healthbar.draw(player.health_points, player.health_points_max)
            fight_panel.enemy_healthbar.draw(enemy.health_points, enemy.health_points_max)
            fight_panel.player_staminabar.draw(player.stamina, player.stamina_max)
            fight_panel.enemy_staminabar.draw(enemy.stamina,enemy.stamina_max)

            debug_log()
            pygame.display.update()

        pygame.quit()

    if __name__ == "__fight_module__":
        fight_module()
