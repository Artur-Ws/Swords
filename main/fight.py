from character import Character, AttackTypeNames


class Fight:
    def _init_(self):
        self.action = "Idle"
        self.environment_choice = None
        self.place = None

    def fight_action(self, player: Character, target: Character):
        if player.alive and target.alive:
            player.attack(target)
            if target.alive:
                target.attack(player)

    def rest_action(self, player: Character, target: Character):
        if player.alive and target.alive:
            player.rest()
            target.attack(player)

    def target_random_attack_action(self, target: Character, attack_type_name: AttackTypeNames):
        pass

