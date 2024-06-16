from .person import Person
from buildings.buildings import Building
from village import Village

class Queen(Person):
    def __init__(self, max_health=10000, movement_speed=1, attack_power=100, attack_range=5, color = 165, aerial = False):
        super().__init__(max_health, movement_speed, attack_power, attack_range, color, aerial)
        self.direction = "up"

    def attack(self, village):
        curr_row, curr_col = self.position
        
        if self.direction == "up":
            new_row = curr_row - 8
            new_col = curr_col
        elif self.direction == "down":
            new_row = curr_row + 8
            new_col = curr_col
        elif self.direction == "left":
             new_col = curr_col - 8
             new_row = curr_row
        elif self.direction == "right":
            new_col = curr_col + 8
            new_row = curr_row
            
        range_x = new_col - 2
        range_y = new_row - 2
        
        for i in range(range_x, range_x + 5):
            for j in range(range_y, range_y + 5):
                if i >=0 and i < village.cols and j >= 0 and j < village.rows:
                    cell = village.grid[j][i]
                    if isinstance(cell, Building):
                        destroyed = cell.take_damage(self.attack_power)
                        if destroyed:
                            cell._remove_building(village)
    
            
    def __str__(self):
        return f"\033[48;5;{self.color}m{' ' * 2}\033[0m"