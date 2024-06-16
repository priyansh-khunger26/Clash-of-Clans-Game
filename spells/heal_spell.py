from .spell import Spell

class HealSpell(Spell):
    def __init__(self, duration):
        super().__init__(duration)
        self.heal_amount = 1.5

    def apply(self, troop):
        prev_health = troop.health
        troop.health = min(troop.max_health, troop.health * self.heal_amount)
        self.active = True

    def remove(self, troop):
        # Healing spell doesn't need to remove effects
        self.active = False
    