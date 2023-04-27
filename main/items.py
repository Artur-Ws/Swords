class Item:
    def __init__(self, name, level, category, armor, damage, health, mana, value):
        self.name = name
        self.level = level
        self.category = category
        self.armor = armor
        self.damage = damage
        self.health = health
        self.mana = mana
        self.value = value

    def __repr__(self):
        return f"Item: {self.name}, category: {self.category}, value: {self.value}"
