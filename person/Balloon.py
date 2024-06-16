from person.person import Person
import math
from buildings.buildings import Building
from buildings.cannon import Cannon
from buildings.Wall import Wall
from buildings.Wizard_tower import Wizard

class Balloon(Person):
    def __init__(self, max_health=200, movement_speed=1, attack_power=1000, attack_range=1, color=58, aerial=True):
        super().__init__(max_health, movement_speed, attack_power, attack_range, color, aerial)
        
    def move(self, building, village):
        
        if self.health <=0:
            return False
        
        row, col = building.position
        curr_row, curr_col = self.position
        
        if curr_col == col and curr_row == row:
            return True
        
        dx = col - curr_col
        dy = row - curr_row
            
        if abs(dx) > abs(dy):
            new_row = curr_row
            new_col = curr_col + int(math.copysign(1, dx)) * self.movement_speed
        else:
            new_row = curr_row + int(math.copysign(1, dy)) * self.movement_speed
            new_col = curr_col
            
        if new_row >= 0 and new_row < village.rows and new_col >= 0 and new_col < village.cols and isinstance(village.grid[new_row][new_col], Balloon):
            new_row, new_col = self.find_alternate_path(curr_row, curr_col, new_row, new_col, village)
            return "ok"
        
        village.grid[curr_row][curr_col] = self.prev
        self.set_position(new_row, new_col)
        if new_row == row and new_col == col:
            self.prev = None
        else:
            self.prev = village.grid[new_row][new_col]
            village.grid[new_row][new_col] = self
        return False
    
    def find_alternate_path(self, curr_row, curr_col, new_row, new_col, village):
        # Check surrounding cells for an alternate path
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for d in directions:
            alt_row, alt_col = new_row + d[0], new_col + d[1]
            if 0 <= alt_row < village.rows and 0 <= alt_col < village.cols:
                if not isinstance(village.grid[alt_row][alt_col], Balloon):
                    return alt_row, alt_col
        return curr_row, curr_col 
        
    def _find_nearest_building(self, village):
        min_distance = float('inf')
        nearest_building = None
        
        if self.health <=0:
            return None

        for row in range(village.rows):
            for col in range(village.cols):
                cell = village.grid[row][col]
                if isinstance(cell, Cannon) or isinstance(cell, Wizard):    # wizard bhi dalna baad mei
                    distance = abs(row - self.position[0]) + abs(col - self.position[1])
                    if distance < min_distance:
                        min_distance = distance
                        nearest_building = cell
                        
        if nearest_building is None:
            for row in range(village.rows):
                for col in range(village.cols):
                    cell = village.grid[row][col]
                    if isinstance(cell, Building) and not isinstance(cell, Wall):
                        distance = abs(row - self.position[0]) + abs(col - self.position[1])
                        if distance < min_distance:
                            min_distance = distance
                            nearest_building = cell        
        
        return nearest_building
    
    def attack(self, village):
        row, col = self.position
        cell = village.grid[row][col]
        if isinstance(cell, Building):
            destroy = cell.take_damage(self.attack_power)
            if destroy:
                cell._remove_building(village)
                self.prev = None
                village.grid[row][col] = None
                # self.set_position(row, col)
                return True
        return False
    
    def __str__(self):
        return f"\033[48;5;{self.color}m{' ' * 2}\033[0m"
