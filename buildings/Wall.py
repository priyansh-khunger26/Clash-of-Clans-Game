from .buildings import Building

class Wall(Building):
    def __init__(self):
        super().__init__(color=128, size=(1, 1), hitpoints=1000, max_hitpoints=1000)  # Gray color, size 1x1, 300 HP

    def __str__(self):
        return f"\033[48;5;{self.color}m{' ' * 2}\033[0m"  # Two spaces wide