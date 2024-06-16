from .buildings import Building
from person.person import Person
import random

class Cannon(Building):
    def __init__(self):
        super().__init__(color=59, size=(2, 2), hitpoints=3000, max_hitpoints=3000)  # Red color, size 2x2, 500 HP
        self.attack_power = 100
        self.range = 5
        self.target_person = None
        self.dead = False
        
    def scan_and_attack(self, village):
        if self.target_person is None:
            self.target_person = self._find_target(village)

        if self.target_person and (not self.target_person.aerial):
            destroyed = self.target_person.take_damage(self.attack_power)
            if destroyed:
                self.target_person.remove_person(village)
        
        self.target_person = None
        
    def _find_target(self, village):
        targets = []
        start_row = max(0, self.position[0] - self.range)
        end_row = min(self.position[0] + self.range + 1, village.rows)
        start_col = max(0, self.position[1] - self.range)
        end_col = min(self.position[1] + self.range + 1, village.cols)

        for row in range(start_row, end_row):
            for col in range(start_col, end_col):
                if (row, col) == self.position:
                    continue
                
                cell = village.grid[row][col]
                if (isinstance(cell, Person)):  # Assuming King is a subclass of Person
                    targets.append(cell)
        
        if targets:
            return random.choice(targets)
        return None

    def __str__(self):
        return f"\033[48;5;{self.color}m{' ' * 2}\033[0m"  # Two spaces wide