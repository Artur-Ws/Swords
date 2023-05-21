import pygame
from debug_log import Debug
from tools import debug_log
from character import Character, AttackTypeNames
from gui.main_menu_gui import MainMenuGui
from gui.fight_module_gui import FightModuleGui
from fight import Fight
from gui.village_module import ActivityModuleGui
from gui.adventure_module import AdventureModuleGui


class GameState:
    def __init__(self):
        self.state = 'main_menu'

    def state_manager(self):
        if self.state == 'main_menu':
            self.main_menu()
        if self.state == 'village_module':
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
                    self.state = 'village_module'
                    self.state_manager()

                if menu.button_options.check_for_input(pygame.mouse.get_pos()):
                    pass

                if menu.button_quit.check_for_input(pygame.mouse.get_pos()):
                    run = False

            menu.draw_menu_background()
            menu.update()
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

                if activity_panel.button_weaponsmith.check_for_input(pygame.mouse.get_pos()):
                    pass

                if activity_panel.button_temple.check_for_input(pygame.mouse.get_pos()):
                    pass

                if activity_panel.button_inn.check_for_input(pygame.mouse.get_pos()):
                    pass

            activity_panel.draw_fight_module_background()
            activity_panel.update()
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

                if adventure_panel.button_back.check_for_input(pygame.mouse.get_pos()):
                    self.state = 'village_module'
                    self.state_manager()

                if adventure_panel.button_mountain.check_for_input(pygame.mouse.get_pos()):
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
            adventure_panel.change_color()

            debug_log()
            pygame.display.update()

        pygame.quit()

    def fight_module(self):
        fight_panel = FightModuleGui()
        player = Character(500, 500, 'Player', 25, 5, 300, 25)
        enemy = Character(1400, 500, 'Enemy', 10, 5, 300, 10)
        fight = Fight(player, enemy)
        attack_type = AttackTypeNames
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

                if fight_panel.stamina_available_check(player):
                    if fight_panel.strong_attack_button.check_for_input(pygame.mouse.get_pos()):
                        fight.fight_action(attack_type.strong_attack)

                if fight_panel.stamina_available_check(player):
                    if fight_panel.medium_attack_button.check_for_input(pygame.mouse.get_pos()):
                        fight.fight_action(attack_type.medium_attack)

                if fight_panel.stamina_available_check(player):
                    if fight_panel.light_attack_button.check_for_input(pygame.mouse.get_pos()):
                        fight.fight_action(attack_type.light_attack)

            fight_panel.draw_fight_module_background()
            fight_panel.update()
            fight_panel.change_color(player)
            fight_panel.player_healthbar.draw(player.health_points, player.health_points_max)
            fight_panel.enemy_healthbar.draw(enemy.health_points, enemy.health_points_max)
            fight_panel.player_staminabar.draw(player.stamina, player.stamina_max)
            fight_panel.enemy_staminabar.draw(enemy.stamina,enemy.stamina_max)

            debug_log()
            pygame.display.update()

        pygame.quit()

    if __name__ == "__fight_module__":
        fight_module()
