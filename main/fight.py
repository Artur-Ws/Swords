from character import Character, AttackTypeNames


class Fight:
    def __init__(self, player: Character, opponent: Character):
        self.player = player
        self.opponent = opponent

    def fight_action(self, attack_type: AttackTypeNames) -> None:
        if self.player.alive and self.opponent.alive:
            self.player.attack_action(self.opponent, attack_type.value)
            if self.opponent.alive:
                self.opponent.attack_action(self.player, attack_type.value)

    def rest_action(self, attack_type: AttackTypeNames) -> None:
        if self.player.alive and self.opponent.alive:
            self.player.rest()
            self.opponent.attack_action(self.player, attack_type.value)
