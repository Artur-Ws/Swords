import pygame
from character import Character
from random import randint


class Fight:
    def _init_(self):
        self.action = "Idle"
        self.environment_choice = None
        self.environment_list = []
        self.place = None
        self.enemies_from_environemt = {"Forrest": { "Wolf": 
                                                    {   "name": "Wolf",
                                                        "strength": 10,
                                                        "defense": 2,
                                                        "health_points": 40,
                                                        "loot": { 
                                                            "pelt": { 
                                                                "drop_chance": 30,
                                                                "value": 10 }, 
                                                            "fang": { 
                                                                "drop_chance": 40,
                                                                "value": 5 } }}, 
                                                    "Fox": 
                                                    {   "name": "Fox",
                                                        "strength": 5,
                                                        "defense": 1,
                                                        "health_points": 30,
                                                        "loot": { 
                                                            "pelt": { 
                                                                "drop_chance": 30,
                                                                "value": 10 }}}}}
   

    def choose_environment(self):
        for self.place in self.enemies_from_environemt:
            self.environment_list.append(self.place)
        print(f"Select place where are you want to go {self.environment_list}")
        self.environment_choice = input()
        return self.environment_choice

    def action(self):
        while True:
            action = input("Select action: Idle - 1 or Attack - 2: ")
            if action == "1" or action == "2":
                return action
            else:
                print("Wrong action, try again")

    def fight_loop(self,player: Character, target: Character):
           while player.alive == True and target.alive == True:
                if self.action() == "Attack":
                    player.attack(target)
                    if target.alive == True:
                        target.attack(player)
                else:
                     target.attack(player)
                    
# player = Character(1,50,'Player', 10, 2, 100)
# enemy = Character(100, 50, "Enemy", 5, 1, 50 )
          
# f = Fight()
# f.action()
