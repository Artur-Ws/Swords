import random


class LightAttack(Attack):
    def __init__(self):
        super().__init__(name="Sword Attack", damage=(random.randint(1,5)), description="Weak attack, little damage")


class MediumAttack(Attack):
    def __init__(self):
        super().__init__(name="MediumAttack", damage=(random.randint(6,10)), description="Standard attack")


class HeavyAttack(Attack):
    def __init__(self):
        super().__init__(name="HeavyAttack", damage=(random.randint(15,20)), description="Heavy and deadly attack")
