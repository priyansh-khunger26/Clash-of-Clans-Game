from .spell import Spell

class RageSpell(Spell):
    def __init__(self, duration):
        super().__init__(duration)
        self.attack_boost = 2
        self.speed_boost = 2

    def apply(self, troop):
        troop.attack_power *= self.attack_boost
        troop.movement_speed *= self.speed_boost
        self.active = True

    def remove(self, troop):
        troop.attack_power = troop.attack_power // self.attack_boost
        troop.movement_speed = troop.movement_speed // self.speed_boost
        self.active = False
