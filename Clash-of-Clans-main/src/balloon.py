from src.constants import *
from src.barbarians import *
from colorama import init, Fore, Back, Style
import math

init()

# archer class
class Balloon:
    def __init__(this):
        this.__total_health = Barbarians().ret_health() # same as barbarian
        this.__health = Barbarians().ret_health()
        this.__isdead = 0
        this.__speed = Barbarians().ret_speed() * 2 # twice of barbarian
        this.__damage = Barbarians().ret_health() * 2 # twice of barbarbarian
        this.__row = game_ht[1] - 2
        this.__col = 0
        this.__is_started = 0
        this.__active = 0
        this.__balloon = "G" # representing the balloon

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

    def ret_balloon(this):
        return this.__balloon

    def upd_balloon(this,x):
        this.__balloon = x

    def on_attack(this, damage):
        this.upd_health(this.ret_health() - damage)
        if this.ret_health() <= 0:
            this.upd_isdead(1)
            this.upd_active(0)

    def reset(this):
        this.upd_total_health(Barbarians().ret_health())
        this.upd_health(Barbarians().ret_health())
        this.upd_row(game_ht[1] - 1)
        this.upd_col(0)
        this.upd_isdead(0)
        this.upd_speed(Barbarians().ret_speed() * 2)
        this.upd_damage(Barbarians().ret_health() * 2)
        this.upd_balloon("G")

    def clear(this, screen):
        screen[this.ret_row()][this.ret_col()] = " "

    # displaying archer on the screen
    def show(this, screen):
        r = this.ret_row()
        c = this.ret_col()
        this.upd_active(1)
        if this.ret_isdead():
            screen[r][c] = " "
            this.upd_active(0)
            return
        if screen[r][c] == " ":
            screen[r][c] = this.ret_balloon()

    # calculate distance between 2 points
    def euclid_distance(this, r1, c1, r2, c2):
        dist = math.dist([r1, c1], [r2, c2])
        return dist

    # see the difference of rows and columns
    def dist(this, r1, c1, r2, c2):
        a = r2 - r1
        b = c2 - c1
        return a, b

    # balloon attack
    def attack(this, r, c, screen, buildings):
        attack_area = set()
        for i in range(this.ret_speed()):
            for j in range(this.ret_speed()):
                attack_area.add((r + i, c + j))
                attack_area.add((r + i, c - j))
                attack_area.add((r - i, c + j))
                attack_area.add((r - i, c - j))

        flag = 0
        for i in range(this.ret_speed()):
            for j in range(this.ret_speed()):
                if (
                        screen[r + i][c + j] != 0
                        or screen[r + i][c - j] != 0
                        or screen[r - i][c + j] != 0
                        or screen[r - i][c - j] != 0
                    ):
                        flag = 1

        if flag == 0:
            return

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
            if screen[r - this.ret_speed()][c] != "G":
                this.upd_row(r - this.ret_speed())
        if a > 0:
            if screen[r + this.ret_speed()][c] != "G":
                this.upd_row(r + this.ret_speed())
        if b > 0:
            if screen[r][c + this.ret_speed()] != "G":
                this.upd_col(c + this.ret_speed())
        if b < 0:
            if screen[r][c - this.ret_speed()] != "G":
                this.upd_col(c - this.ret_speed())

    '''
    predicting path of ballon
    finding closest building
    if it is not in attack_area, we move towards it
    else we attack
    '''
    def predict_path(this, screen, buildings):
        if this.ret_isdead() == 0:
            r = this.ret_row()
            c = this.ret_col()

            distance = 10000
            x = 0
            y = 0
            
            flag = 0
            for building in buildings:
                t = building.ret_type()
                i = building.ret_row()
                j = building.ret_col()
                
                if t == 4 or t == 6:
                    if building.ret_isdestroyed() == 0:
                        flag = 1
                        d = this.euclid_distance(r, c, i, j)
                        if(d < distance):
                            distance = d
                            x = i
                            y = j
                            
            if flag == 0:
                for building in buildings:
                    t = building.ret_type()
                    i = building.ret_row()
                    j = building.ret_col()
                    
                    if t != 4 and t != 6:
                        if building.ret_isdestroyed() == 0:
                            d = this.euclid_distance(r, c, i, j)
                            if(d < distance):
                                distance = d
                                x = i
                                y = j
                                
            a, b = this.dist(r, c, x, y)
                               
            if abs(a) <= Barbarians().ret_speed() and abs(b) <= Barbarians().ret_speed():
                this.attack(r, c, screen, buildings)
            else:
                this.move(r, c, a, b, screen, buildings)

