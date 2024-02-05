from src.constants import *
from colorama import init, Fore, Back, Style
import math

init()

# barbarians class
class Barbarians:
    def __init__(this):
        this.__total_health = 20 # health of the barbarian
        this.__health = 20
        this.__isdead = 0
        this.__speed = 1 # speed = 1 = rows/columns every frametransition
        this.__damage = 5 # damage dealt
        this.__row = game_ht[1] - 2
        this.__col = 0
        this.__is_started = 0
        this.__active = 0
        this.__barbarian = "B" # representing the barbarian

    # encapsulation
    def ret_total_health(this):
        return this.__total_health

    def upd_total_health(this, x):
        this.__health = x

    def ret_health(this):
        return this.__health

    def upd_health(this, x):
        this.__health = x

    def ret_row(this):
        return this.__row

    def upd_row(this, x):
        this.__row = x

    def ret_col(this):
        return this.__col

    def upd_col(this, x):
        this.__col = x

    def ret_is_started(this):
        return this.__is_started

    def upd_is_started(this, x):
        this.__is_started = x

    def ret_isdead(this):
        return this.__isdead

    def upd_isdead(this, x):
        this.__isdead = x

    def ret_speed(this):
        return this.__speed

    def upd_speed(this, x):
        this.__speed = x

    def ret_damage(this):
        return this.__damage

    def upd_damage(this, x):
        this.__damage = x
        
    def ret_active(this):
        return this.__active
    
    def upd_active(this,x):
        this.__active = x

    def ret_barbarian(this):
        return this.__barbarian

    def upd_barbarian(this,x):
        this.__barbarian = x

    def on_attack(this, damage):
        this.upd_health(this.ret_health() - damage)
        if this.ret_health() <= 0:
            this.upd_isdead(1)
            this.upd_active(0)

    def reset(this):
        this.upd_total_health(20)
        this.upd_health(20)
        this.upd_row(game_ht[1] - 1)
        this.upd_col(0)
        this.upd_isdead(0)
        this.upd_speed(1)
        this.upd_damage(10)
        this.upd_barbarian("B")

    def clear(this, screen):
        screen[this.ret_row()][this.ret_col()] = " "

    # displaying barbarian on the screen
    def show(this, screen):
        r = this.ret_row()
        c = this.ret_col()
        this.upd_active(1)
        if this.ret_isdead():
            screen[r][c] = " "
            this.upd_active(0)
            return
        screen[r][c] = this.ret_barbarian()

    # calculate distance between 2 points
    def euclid_distance(this, r1, c1, r2, c2):
        dist = math.dist([r1, c1], [r2, c2])
        return dist

    # see the difference of rows and columns
    def dist(this, r1, c1, r2, c2):
        a = r2 - r1
        b = c2 - c1
        return a, b

    # barbarian attack
    def attack(this, r, c, screen, buildings):
        attack_area = [] # the area in which barbarian can attack
        attack_area.append((r,c+1))
        attack_area.append((r,c-1))
        attack_area.append((r+1,c))
        attack_area.append((r-1,c))
        attack_area.append((r+1,c+1))
        attack_area.append((r-1,c-1))
        attack_area.append((r+1,c-1))
        attack_area.append((r-1,c+1))

        # checking which building lies in attack_area and attacking accordingly
        for building in buildings:
            t = building.ret_type()
            r1 = building.ret_row()
            c1 = building.ret_col()
            flag = 0
            if t != 3:
                for i in range(building.ret_row_size()):
                    for j in range(building.ret_col_size()):
                        test = (r1 + i, c1 + j)
                        if test in attack_area:
                            # os.system("aplay -q ./sounds/sword.wav &")
                            building.on_attack(this.ret_damage())
                            flag = 1
                            break
                    if flag:
                        break
            else:
                for i in range(building.ret_row_size()):
                    for j in range(building.ret_col_size()):
                        if (
                            i == 0
                            or i == building.ret_row_size() - 1
                            or j == 0
                            or j == building.ret_col_size() - 1
                        ):
        
                            test = (r1 + i, c1 + j)
                            if test in attack_area:
            
                                building.on_attack(this.ret_damage())
                                flag = 1
                                break
                    if flag:
                        break
     
    # moving towards the closes building. Diagonal movements allowed.                    
    def move(this, r, c, a, b, screen, buildings):
        this.clear(screen)
        if a < 0:
            if screen[r - this.ret_speed()][c] == " ":
                this.upd_row(r - this.ret_speed())
        if a > 0:
            if screen[r + this.ret_speed()][c] == " ":
                this.upd_row(r + this.ret_speed())
        if b > 0:
            if screen[r][c + this.ret_speed()] == " ":
                this.upd_col(c + this.ret_speed())
        if b < 0:
            if screen[r][c - this.ret_speed()] == " ":
                this.upd_col(c - this.ret_speed())

    '''
    predicting path of barbarian
    finding closest building
    if it is not in attack_area, we move towards it
    else we attack
    '''
    def predict_path(this, screen, buildings):
        if this.ret_isdead() == 0:
            r = this.ret_row()
            c = this.ret_col()
            h = this.ret_health()
            h_total = this.ret_total_health()
            if(h/h_total <= 0.5):
                this.upd_barbarian("D")
            else:
                this.upd_barbarian("B")

            distance = 10000
            x = 0
            y = 0

            for i in range(game_ht[0] + 5, game_ht[1] - 1):
                for j in range(game_wd[0]+2,game_wd[1]-2):
                    if (
                        screen[i][j] != " "
                        and screen[i][j] != "K"
                        and screen[i][j] != "B"
                        and screen[i][j] != "D"
                        and screen[i][j] != "A"
                        and screen[i][j] != "G"
                    ):
                        d = this.euclid_distance(r, c, i, j)

                        if(d < distance):
                            distance = d
                            x = i
                            y = j

            a, b = this.dist(r, c, x, y)
            if abs(a) <= this.ret_speed() and abs(b) <= this.ret_speed():
                this.attack(r, c, screen, buildings)
            else:
                this.move(r, c, a, b, screen, buildings)

