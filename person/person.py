class Person:
    def __init__(self, max_health, movement_speed, attack_power, attack_range, color, aerial):
        self.max_health = max_health
        self.health = max_health
        self.movement_speed = movement_speed
        self.alive = True
        self.attack_power = attack_power
        self.attack_range = attack_range
        self.target_building = None
        self.active_spells = []
        self.color = color
        self.position = None
        self.aerial = aerial
        self.prev = None
        
    def place_person(self, village, row, col):
        self.set_position(row, col)
        self.prev = village.grid[row][col]
        village.grid[row][col] = self
        
    def move(self, village, new_row, new_col):
        if new_row >= 0 and new_row < village.rows and new_col >= 0 and new_col < village.cols:
            cell = village.grid[new_row][new_col]
            if cell is None:
                row, col = self.get_position()
                
                village.grid[row][col] = self.prev
                
                self.set_position(new_row, new_col)
                self.prev = village.grid[new_row][new_col]
                village.grid[new_row][new_col] = self

    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0.5 * self.max_health and self.health > 0.3 * self.max_health:
            self.color = 120
        elif self.health < 0.3 * self.max_health and self.health > 0:
            self.color = 90
        elif self.health <= 0:
            self.health = 0
            return True

        return False
            
    def remove_person(self, village):
        if self.health <= 0:
            row, col = self.position
            village.grid[row][col] = self.prev
    
    def set_position(self, row, col):
        self.position = (row, col)
        
    def get_position(self):
        return self.position[0], self.position[1]
    
    def apply_spell(self, spell):
        if spell not in self.active_spells:
            spell.apply(self)
            self.active_spells.append(spell)
        if self.health < 0.5 * self.max_health and self.health > 0.3 * self.max_health:
            self.color = 120
        elif self.health < 0.3 * self.max_health and self.health > 0:
            self.color = 90
        elif self.health <= 0:
            self.health = 0
            self.alive = False

    def remove_spell(self, spell):
        if spell in self.active_spells:
            spell.remove(self)
            self.active_spells.remove(spell)