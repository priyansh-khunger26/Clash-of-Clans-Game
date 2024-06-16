class SpawningPoint:
    def __init__(self, location):
        self.location = location
        
    def add_spawning_point(self, village):
        row,col = self.location
        if 0 <= row < village.rows and 0 <= col < village.cols:
            village.grid[row][col] = self
        else:
            print("cannot place the spawning point")

    def __str__(self):
        return "\033[48;5;245mSP\033[0m"  # Gray background with "SP" indicating spawning point
