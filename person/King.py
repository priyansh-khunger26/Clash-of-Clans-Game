from .person import Person
from buildings.buildings import Building
import random

class King(Person):
    def __init__(self, max_health=30000, movement_speed=1, attack_power=1000, attack_range=1, color = 160, aerial = False):
        super().__init__(max_health, movement_speed, attack_power, attack_range, color, aerial)
    
    def scan_and_attack(self, village):
        if self.target_building is None:
            self.target_building = self._find_target(village)

        if self.target_building:
            # print(f"King attacks the building at {self.target_building.position} with power {self.attack_power}.")
            destroyed = self.target_building.take_damage(self.attack_power)
            if destroyed:
                self.target_building._remove_building(village)
                self.target_building = None
            
    def _find_target(self, village):
        targets = []
        for row in range(max(0, self.position[0] - self.attack_range), min(village.rows, self.position[0] + self.attack_range + 1)):
            for col in range(max(0, self.position[1] - self.attack_range), min(village.cols, self.position[1] + self.attack_range + 1)):
                if row == self.position[0] and col == self.position[1]:
                    continue
                cell = village.grid[row][col]
                if isinstance(cell, Building) and cell.is_alive():
                    targets.append(cell)
        if targets:
            return random.choice(targets)
        return None
    
            
    def __str__(self):
        return f"\033[48;5;{self.color}m{' ' * 2}\033[0m"