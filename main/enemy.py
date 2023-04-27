from main.character import Character


class Enemy(Character):
    def __init__(self, name, x, y, strength, defense, health_points):
        super().__init__(x, y, name, strength, defense, health_points)
        self.name = name
        self.x = x
        self.y = y
        self.strength = strength
        self.defense = defense
        self.health_points = health_points

    def __repr__(self):
        return f"<{self.name}. Stats: STR-{self.strength}, DEF-{self.defense}, HP-{self.health_points}>"


# Enemy("Wolf", 100, 100, 10, 2, 30, "Pelt, Fang").add_entry()
