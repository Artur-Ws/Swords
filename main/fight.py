from character import Character


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
