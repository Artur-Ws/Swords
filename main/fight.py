from character import Character, AttackTypeNames


attack_type = AttackTypeNames


class Fight:
    def _init_(self):
        self.action = "Idle"
        self.environment_choice = None
        self.place = None

    def fight_action(self, player: Character, target: Character):
        if player.alive and target.alive:
            player.attack_action(target, attack_type.medium_attack.value)
            if target.alive:
                target.attack_action(player, attack_type.medium_attack.value)

    def rest_action(self, player: Character, target: Character):
        if player.alive and target.alive:
            player.rest()
            target.attack_action(player, attack_type.medium_attack.value)
