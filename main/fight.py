import pygame
from character import Character
import enemy


class fight:
    def _init_(self):
        self.action = "Idle"
        self.environment_choice = None
        self.environment_list = ["Forrest", "Meadow"]
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
           environment = input("Select place where are you want to go (forest, meadow)")
           return environment                  


    def action(self):
          action = input("Select action: Attack or Idle")
          return action


    def fight_loop(self,player: Character, target: Character, damage):
           while player.alive == True and target.alive == True:
                if self.action() == "Attack":
                    player.attack(target)
                    if enemy.Enemy.alive == True:
                            player.get_damage(damage)
                else:
                      player.get_damage(damage)
                    
                         
                         
                         
        

# enemies_from_environemt = {"Forest" : {
#                                         {"enemies" : {"rabbit":(),
#                                                     "bandit":(), 
#                                                     "owl":()}}, 
#                                         {"strangers" : {"blind_man":(), 
#                                                       "old_man":()}}}, 
#                             "Meadow" : {
#                                         {"enemies" : {"rat":(), "mouse":()}},
#                                         {"strangers" : {"pirest":(), "fool":()}}}
# }

# for environment in enemies_from_environemt:
#             print(f'{environment}')

