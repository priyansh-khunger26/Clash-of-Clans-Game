from .person import Person
from buildings.buildings import Building
import random
from buildings.Wall import Wall
import math
from spawning_point import SpawningPoint

class Barbarian(Person):
    def __init__(self, max_health=200, movement_speed=1, attack_power=50, attack_range=1, color = 226, aerial = False):
        super().__init__(max_health, movement_speed, attack_power, attack_range, color, aerial)
        
    def scan_and_attack(self, village):
        if self.target_building is None or not self.target_building.is_alive():
            self.target_building = self._find_target(village)

        if self.target_building:
            # print(f"Barbarian attacks the building at {self.target_building.position} with power {self.attack_power}.")
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
    
    def move_towards_nearest_building(self, village):
        nearest_building = self._find_nearest_building(village)
        if nearest_building:
            target_row, target_col = nearest_building.position

            dx = target_col - self.position[1]
            dy = target_row - self.position[0]
            
            if abs(dx) > abs(dy):
                new_row = self.position[0]
                new_col = self.position[1] + int(math.copysign(1, dx)) * self.movement_speed
            else:
                new_row = self.position[0] + int(math.copysign(1, dy)) * self.movement_speed
                new_col = self.position[1]
            
            if new_row >= 0 and new_row < village.rows and new_col >=0 and new_col < village.cols and (village.grid[new_row][new_col] is None or village.grid[new_row][new_col] is SpawningPoint):
                village.grid[self.position[0]][self.position[1]] = self.prev
                self.prev = village.grid[new_row][new_col]

                self.set_position(new_row, new_col)
                
                village.grid[new_row][new_col] = self

    def _find_nearest_building(self, village):
        min_distance = float('inf')
        nearest_building = None

        for row in range(village.rows):
            for col in range(village.cols):
                cell = village.grid[row][col]
                if isinstance(cell, Building) and not isinstance(cell, Wall):
                    distance = abs(row - self.position[0]) + abs(col - self.position[1])
                    if distance < min_distance:
                        min_distance = distance
                        nearest_building = cell

        return nearest_building
    
        
    def __str__(self):
        return f"\033[48;5;{self.color}m{' ' * 2}\033[0m"