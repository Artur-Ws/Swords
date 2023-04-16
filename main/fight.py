import pygame
import character
import enemy


class fight:
    def _init_(self):
        self.action = "Idle"
        self.environment_choice = None
        self.environment_list = ["Forest", "Meadow"]
        # self.enemies_from_environemt = {"forest" : {
        #                                     {"enemies" : {"rabbit":(),
        #                                                 "bandit":(), 
        #                                                 "owl":()}}, 
        #                                     {"strangers" : {"blind_man":(), 
        #                                                   "old_man":()}}}, 
        #                                 "meadow" : {
        #                                     {"enemies" : {"rat":(), 
        #                                                 "mouse":()}},
        #                                     {"strangers" : {"pirest":(), 
        #                                                   "fool":()}}}
        #                                  }
   
    def choose_environment(self):
           environment = input("Select place where are you want to go (forest, meadow)")
           return environment                  

    def action(self):
          action = input("Select action: Attack or Idle")
          return action

    def fight_loop(self, target, damage):
           while character.Character.alive == True and enemy.Enemy.alive == True:
                if self.action() == "Attack":
                    character.Character.attack(target)
                    if enemy.Enemy.alive == True:
                            character.Character.get_damage(damage)
                else:
                      character.Character.get_damage(damage)
                    
                         
                         
                         
        

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

