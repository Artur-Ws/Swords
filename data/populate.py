from data_manager import add_objects, link_item_enemy, link_environment_enemy, ItemDB, EnemyDB, EnvironmentDB
'''
########################################## ADDING  NEW  OBJECTS  TO  DATABASE ##########################################

To add new objects to database, simply create this objects from DB-version of their classes (imported above).
Next pass those objects to <add_objects> function. Example below:

enemy1 = EnemyDB("Wolf", 100, 100, 10, 2, 30)
env1 = EnvironmentDB("Forrest")
item1 = ItemDB("Wolf Fur", 0, "Neutral", 0, 0, 0, 0, 15)
item2 = ItemDB("Wolf Fang", 0, "Neutral", 0, 0, 0, 0, 5)

add_objects(enemy1, env1, item1, item2)

################################################### LINKING  OBJECTS ###################################################

To link objects together, those object have to be added to database already. Then just pass names of those objects 
as an argument to one of specific methods: <link_item_enemy> for connecting item and enemy or <link_environment_enemy>
for environment and item connection. Example below:

link_environment_enemy("Forrest", "Wolf")
link_item_enemy("Wolf Fur", "Wolf")
link_item_enemy("Wolf Fang", "Wolf")
'''
