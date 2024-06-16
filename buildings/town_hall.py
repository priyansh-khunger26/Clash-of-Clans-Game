from .buildings import Building

class TownHall(Building):
    def __init__(self):
        super().__init__(color=202, size=(4, 3), hitpoints=20000, max_hitpoints=20000)  # Orange color, size 4x3, 1000 HP

    def __str__(self):
        return f"\033[48;5;{self.color}m{' ' * 2}\033[0m"  # Two spaces wide