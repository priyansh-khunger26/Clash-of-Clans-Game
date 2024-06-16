from buildings.buildings import Building
from buildings.Wall import Wall
from person.person import Person

class Village:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.grid = [[None for _ in range(cols)] for _ in range(rows)]
        self.king = None
        self.prev = None
        self.queen = None
                    
    # def damage_building(self, row, col, damage):
    #     building = self.grid[row][col]
    #     if building:
    #         destroyed = building.take_damage(damage)
    #         if destroyed:
    #             self._remove_building(row, col, building.size)

    def display_village(self):
        print("called me")
        if self.king:
            health_bar = "\033[42m" + " " * int(self.king.health // 10) + "\033[0m"
            print(f"King's Health: {health_bar} ({self.king.health} HP)")
            print()
        elif self.queen:
            health_bar = "\033[42m" + " " * int(self.queen.health // 10) + "\033[0m"
            print(f"Queen's Health: {health_bar} ({self.queen.health} HP)")
            print()
        
        for row in range(self.rows):
            for col in range(self.cols):
                cell = self.grid[row][col]
                if cell:
                    print(cell, end="")
                else:
                    print("\033[48;5;40m  \033[0m", end="")
            print()
            
    def all_buildings_destroyed(self):
        for row in range(self.rows):
            for col in range(self.cols):
                cell = self.grid[row][col]
                if isinstance(cell, Building) and not isinstance(cell, Wall):
                    return False
        return True
    
    def all_troops_destroyed(self):
        for row in range(self.rows):
            for col in range(self.cols):
                cell = self.grid[row][col]
                if isinstance(cell, Person):
                    return False
        return True