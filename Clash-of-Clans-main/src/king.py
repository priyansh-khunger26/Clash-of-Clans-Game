from src.constants import *
from colorama import init, Fore, Back, Style

init()

# King class
class King:
    def __init__(this):
        this.__total_health = 100 # total health of king
        this.__health = 100
        this.__row = game_ht[1] - 1 # starting point
        this.__col = game_wd[1] - 2
        this.__isdead = 0
        this.__speed = 1
        this.__damage = 10
        this.__king = "K" # symbol for king

    # encapsulation
    def ret_total_health(this):
        return this.__total_health

    def upd_total_health(this, x):
        this.__total_health = x

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

    def ret_king(this):
        return this.__king
    
    def on_attack(this, damage):
        this.upd_health(this.ret_health() - damage)
        if this.ret_health() <= 0:
            this.upd_isdead(1)

    def reset(this):
        this.upd_total_health(100)
        this.upd_health(100)
        this.upd_row(game_ht[1] - 1)
        this.upd_col(game_wd[1] - 1)
        this.upd_isdead(0)
        this.upd_speed(1)
        this.upd_damage(10)

    '''
    "Abstraction" property implemented.
    attacking when space is input by user
    Leviathan axe implemented : 5x5 attack area
    all buildings in this area are effected
    '''
    def attack(this, screen, buildings):
        r = this.ret_row()
        c = this.ret_col()
        attack_area = set()
        
        # setting attack_area
        for i in range(5):
            for j in range(5):
                attack_area.add((r + i, c + j))
                attack_area.add((r + i, c - j))
                attack_area.add((r - i, c + j))
                attack_area.add((r - i, c - j))

        flag = 0
        for i in range(5):
            for j in range(5):
                if (
                    screen[r + i][c + j] != 0
                    or screen[r + i][c - j] != 0
                    or screen[r - i][c + j] != 0
                    or screen[r - i][c - j] != 0
                ):
                    flag = 1
                    break

        if flag == 0:
            return

        # sword sound every time king attacks
        os.system("aplay -q ./src/sounds/sword.wav &")

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

    def clear(this, screen):
        screen[this.ret_row()][this.ret_col()] = " "

    def show(this, screen):
        r = this.ret_row()
        c = this.ret_col()
        screen[r][c] = this.ret_king()

    '''
    Abstraction implemented again.
    w: king moves up
    a: king moves left
    s: king moves right
    d: king moves down
    '''
    def move_up(this, screen):
        this.clear(screen)
        r = this.ret_row()
        c = this.ret_col()
        if r != 0:
            if screen[r - this.ret_speed()][c] == " ":
                this.upd_row(r - this.ret_speed())

    def move_down(this, screen):
        this.clear(screen)
        r = this.ret_row()
        c = this.ret_col()
        if r != game_ht[1] - 1:
            if screen[r + this.ret_speed()][c] == " ":
                this.upd_row(r + this.ret_speed())

    def move_left(this, screen):
        this.clear(screen)
        r = this.ret_row()
        c = this.ret_col()
        if c != game_wd[0]:
            if screen[r][c - this.ret_speed()] == " ":
                this.upd_col(c - this.ret_speed())

    def move_right(this, screen):
        this.clear(screen)
        r = this.ret_row()
        c = this.ret_col()
        if c != game_wd[1]:
            if screen[r][c + this.ret_speed()] == " ":
                this.upd_col(c + this.ret_speed())

