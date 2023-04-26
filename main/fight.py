from character import Character
from random import randint


class Fight:
    def _init_(self):
        self.action = "Idle"
        self.environment_choice = None
        self.place = None

    def fight_action(self, player: Character, target: Character):
        if player.alive == True and target.alive == True:
            player.attack(target)
            if target.alive == True:
                target.attack(player)

    # def choose_environment(self):
    #     for self.place in self.enemies_from_environemt:
    #         self.environment_list.append(self.place)
    #     print(f"Select place where are you want to go {self.environment_list}")
    #     self.environment_choice = input()
    #     return self.environment_choice
    #
    #
    # def action(self):
    #     while True:
    #         action = input("Select action: Idle - 1 or Attack - 2: ")
    #         if action == "1" or action == "2":
    #             return action
    #         else:
    #             print("Wrong action, try again")


