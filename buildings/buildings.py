class Building:
    def __init__(self, color, size, hitpoints, max_hitpoints):
        self.color = color
        self.size = size
        self.hitpoints = hitpoints
        self.max_hitpoints = max_hitpoints
        self.position = None
        
    def _place_building(self, start_row, start_col, village):
        size_y, size_x = self.size
        self.position = (start_row,start_col)
        for row in range(start_row, start_row + size_y):
            for col in range(start_col, start_col + size_x):
                if 0 <= row < village.rows and 0 <= col < village.cols:
                    if village.grid[row][col] is None:
                        village.grid[row][col] = self
    
    def take_damage(self, damage):
        self.hitpoints -= damage
        if self.hitpoints < 0.5 * self.max_hitpoints and self.hitpoints > 0.3 * self.max_hitpoints:
            self.color = 0.5 * self.color
        elif self.hitpoints < 0.3 * self.max_hitpoints and self.hitpoints > 0:
            self.color = 0.3 * self.color   
        elif self.hitpoints <= 0:
            self.hitpoints = 0
            self.color = 40
            return True
        
        return False
    
    def _remove_building(self, village):
        start_row, start_col = self.get_position()
        size_y, size_x = self.size
        for row in range(size_y):
            for col in range(size_x):
                grid_row = start_row + row
                grid_col = start_col + col
                # if 0 <= grid_row < village.rows and 0 <= grid_col < village.cols:
                village.grid[grid_row][grid_col] = None 
    
    def is_alive(self):
        return self.hitpoints > 0
    
    def get_position(self):
        return self.position
    
    def set_position(self, row, col):
        self.position = (row,col)

    def __str__(self):
        return f"\033[48;5;{self.color}m{' ' * 2}\033[0m"  # Two spaces wide