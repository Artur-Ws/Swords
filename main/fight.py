from character import Character, AttackTypeNames


attack_type = AttackTypeNames


class Fight:
    def __init__(self, player: Character, opponent: Character):
        self.player = player
        self.opponent = opponent

    def fight_action(self):
        if self.player.alive and self.opponent.alive:
            self.player.attack_action(self.opponent, attack_type.medium_attack.value)
            if self.opponent.alive:
                self.opponent.attack_action(self.player, attack_type.medium_attack.value)

    def rest_action(self):
        if self.player.alive and self.opponent.alive:
            self.player.rest()
            self.opponent.attack_action(self.player, attack_type.medium_attack.value)

    # def if_all_alive_action(self, type_attack_method) -> None:
    #     if self.player.alive and self.opponent.alive:
    #         type_attack_method()
    #         if self.opponent.alive:
    #             self.draw_enemy_action(self.player, self.opponent)
    #
    # def draw_enemy_action(selfself.) -> None:
    #     attack_type_number = randint(1, 3)
    #     if attack_type_number == 1:
    #         self.opponent.light_attack(self.player)
    #     elif attack_type_number == 2:
    #         self.opponent.medium_attack(self.player)
    #     else:
    #         self.opponent.heavy_attack(self.player)
