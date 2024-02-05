from distutils.command.build import build
import os
from src.constants import *
from colorama import init, Fore, Back, Style
import random

init()

"""
Building, its colour on the terminal, and the number used to represent
Town Hall: Yellow : 1
Huts: Blue : 2
Walls: Magenta : 3
Cannon: red: 4 (5 and Blue while attacking)
"""

# Buildings class: stores all the buildings that are generated
class Buildings:
    def __init__(this):
        this.buildings = []
        this.a = []
        for i in range(game_ht[1]):
            this.a.append([])
            for j in range(game_wd[1]):
                this.a[i].append(0)

    # generating all the buildings
    def generator(this, cannons, towers, x):
        this.hall_generator()
        this.hut_generator()
        this.cannon_generator(cannons, x)
        this.tower_generator(towers, x)

    # surrounds all the buildings by default
    def wall_generator(this, x):
        w = Wall()
        w.upd_col(this.col - 1)
        w.upd_row(this.row - 1)
        # w.upd_isdestroyed(1)
        if x == 1:
            w.upd_col_size(5)
            w.upd_row_size(6)
        else:
            w.upd_col_size(4)
            w.upd_row_size(4)
        this.buildings.append(w)

    # 4x3 size in the middle of the terminal
    def hall_generator(this):
        this.row = game_ht[1] // 2 - 2
        this.col = int(game_wd[1] / 1.7)
        t = TownHall()
        t.upd_col(this.col)
        t.upd_row(this.row)
        # t.upd_isdestroyed(1)
        this.buildings.append(t)
        this.wall_generator(1)
        r = this.row - 1
        c = this.col - 1
        for i in range(6):
            for j in range(5):
                if i == 0 or i == 5 or j == 0 or j == 4:
                    this.a[r + i][c + j] = Wall().ret_type()
                else:
                    this.a[r + i][c + j] = t.ret_type()

    def building_check(this, r, c, x):
        if x == Hut().ret_type():
            for i in range(4):
                for j in range(4):
                    if this.a[r + i][c + j] != 0:
                        return 0
            return 1
        elif x == Cannon().ret_type() or x == WizardTower().ret_type():
            if this.a[r][c] != 0:
                return 0
            else:
                return 1

    # 2x2 size generated randomly
    def hut_generator(this):
        huts = 5
        while huts > 0:
            this.row = random.randint(2, game_ht[1] // 1.2)
            this.col = random.randint(game_wd[0] + 5, game_wd[1] - 10)
            if this.building_check(this.row - 1, this.col - 1, Hut().ret_type()):
                huts -= 1
                h = Hut()
                h.upd_col(this.col)
                h.upd_row(this.row)
                this.buildings.append(h)
                this.wall_generator(2)
                r = this.row - 1
                c = this.col - 1
                for i in range(4):
                    for j in range(4):
                        if i == 0 or i == 3 or j == 0 or j == 3:
                            this.a[r + i][c + j] = Wall().ret_type()
                        else:
                            this.a[r + i][c + j] = h.ret_type()
        return

    # 1x1 size generated randomly
    def cannon_generator(this, number, x):
        cannons = number
        while cannons > 0:
            # x.append('here_cannon')
            this.row = random.randint(2, game_ht[1] // 1.2)
            this.col = random.randint(game_wd[0] + 5, game_wd[1] - 10)
            if this.building_check(this.row, this.col, Cannon().ret_type()):
                c = Cannon()
                c.upd_col(this.col)
                c.upd_row(this.row)
                this.buildings.append(c)
                cannons -= 1
                this.a[this.row][this.col] = c.ret_type()
        return

    def tower_generator(this, number, x):
        towers = number
        # x.append(towers)
        while towers > 0:
            this.row = random.randint(2, game_ht[1] // 1.2)
            this.col = random.randint(game_wd[0] + 5, game_wd[1] - 10)
            if this.building_check(this.row, this.col, WizardTower().ret_type()):
                w = WizardTower()
                w.upd_col(this.col)
                w.upd_row(this.row)
                this.buildings.append(w)
                towers -= 1
                this.a[this.row][this.col] = w.ret_type()
        return

    # cannon attack function when someone is in its vicinity (5 tile radius) : turns blue when its attacking
    def cannon_attack(
        this,
        screen,
        king,
        barbarian1,
        barbarian2,
        barbarian3,
        archer1,
        archer2,
        archer3,
    ):
        r_king = king.ret_row()
        c_king = king.ret_col()
        r_b1 = barbarian1.ret_row()
        c_b1 = barbarian1.ret_col()
        r_b2 = barbarian2.ret_row()
        c_b2 = barbarian2.ret_col()
        r_b3 = barbarian3.ret_row()
        c_b3 = barbarian3.ret_col()
        r_b4 = archer1.ret_row()
        c_b4 = archer1.ret_col()
        r_b5 = archer2.ret_row()
        c_b5 = archer2.ret_col()
        r_b6 = archer3.ret_row()
        c_b6 = archer3.ret_col()
        test1 = (r_king, c_king)
        test2 = (r_b1, c_b1)
        test3 = (r_b2, c_b2)
        test4 = (r_b3, c_b3)
        test5 = (r_b4, c_b4)
        test6 = (r_b5, c_b5)
        test7 = (r_b6, c_b6)

        for building in this.buildings:
            if building.ret_type() == Cannon().ret_type():
                attack = False
                if building.ret_isdestroyed() == 0:
                    r = building.ret_row()
                    c = building.ret_col()
                    attack_area = set()

                    for i in range(Cannon().range + 1):
                        for j in range(Cannon().range + 1):
                            attack_area.add((r + i, c + j))
                            attack_area.add((r + i, c - j))
                            attack_area.add((r - i, c + j))
                            attack_area.add((r - i, c - j))

                    flag = 0
                    for i in range(Cannon().range + 1):
                        for j in range(Cannon().range + 1):
                            if (
                                screen[r + i][c + j] != 0
                                or screen[r + i][c - j] != 0
                                or screen[r - i][c + j] != 0
                                or screen[r - i][c - j] != 0
                            ):
                                flag = 1

                    if flag == 0:
                        return

                    if test1 in attack_area:
                        if king.ret_isdead() == 0:
                            king.on_attack(Cannon().damage)
                            attack = True
                    elif test2 in attack_area:
                        if barbarian1.ret_isdead() == 0:
                            barbarian1.on_attack(Cannon().damage)
                            attack = True
                    elif test3 in attack_area:
                        if barbarian2.ret_isdead() == 0:
                            barbarian2.on_attack(Cannon().damage)
                            attack = True
                    elif test4 in attack_area:
                        if barbarian3.ret_isdead() == 0:
                            barbarian3.on_attack(Cannon().damage)
                            attack = True
                    elif test5 in attack_area:
                        if archer1.ret_isdead() == 0:
                            archer1.on_attack(Cannon().damage)
                            attack = True
                    elif test6 in attack_area:
                        if archer2.ret_isdead() == 0:
                            archer2.on_attack(Cannon().damage)
                            attack = True
                    elif test7 in attack_area:
                        if archer3.ret_isdead() == 0:
                            archer3.on_attack(Cannon().damage)
                            attack = True

                    if attack:
                        screen[r][c] = Cannon().ret_type() + 1
                        os.system("aplay -q ./sounds/explosion.wav &")
                    else:
                        screen[r][c] = Cannon().ret_type()

    def tower_attack(
        this,
        screen,
        king,
        barbarian1,
        barbarian2,
        barbarian3,
        archer1,
        archer2,
        archer3,
        balloon1,
        balloon2,
        balloon3,
    ):
        r_king = king.ret_row()
        c_king = king.ret_col()
        r_b1 = barbarian1.ret_row()
        c_b1 = barbarian1.ret_col()
        r_b2 = barbarian2.ret_row()
        c_b2 = barbarian2.ret_col()
        r_b3 = barbarian3.ret_row()
        c_b3 = barbarian3.ret_col()
        r_b4 = archer1.ret_row()
        c_b4 = archer1.ret_col()
        r_b5 = archer2.ret_row()
        c_b5 = archer2.ret_col()
        r_b6 = archer3.ret_row()
        c_b6 = archer3.ret_col()
        r_7 = balloon1.ret_row()
        c_7 = balloon1.ret_col()
        r_8 = balloon2.ret_row()
        c_8 = balloon2.ret_col()
        r_9 = balloon3.ret_row()
        c_9 = balloon3.ret_col()
        test1 = (r_king, c_king)
        test2 = (r_b1, c_b1)
        test3 = (r_b2, c_b2)
        test4 = (r_b3, c_b3)
        test5 = (r_b4, c_b4)
        test6 = (r_b5, c_b5)
        test7 = (r_b6, c_b6)
        test8 = (r_7, c_7)
        test9 = (r_8, c_8)
        test10 = (r_9, c_9)

        for building in this.buildings:
            if building.ret_type() == WizardTower().ret_type():
                attack = False
                if building.ret_isdestroyed() == 0:
                    r = building.ret_row()
                    c = building.ret_col()

                    attack_area = set()

                    # setting attack_area
                    for i in range(WizardTower().range + 1):
                        for j in range(WizardTower().range + 1):
                            attack_area.add((r + i, c + j))
                            attack_area.add((r + i, c - j))
                            attack_area.add((r - i, c + j))
                            attack_area.add((r - i, c - j))

                    flag = 0
                    for i in range(Cannon().damage + 1):
                        for j in range(Cannon().damage + 1):
                            if (
                                screen[r + i][c + j] != 0
                                or screen[r + i][c - j] != 0
                                or screen[r - i][c + j] != 0
                                or screen[r - i][c - j] != 0
                            ):
                                flag = 1

                    if flag == 0:
                        return

                    r_attack = 0
                    c_attack = 0

                    if test1 in attack_area:
                        if king.ret_isdead() == 0:
                            r_attack = r_king
                            c_attack = c_king
                    elif test8 in attack_area:
                        if balloon1.ret_isdead() == 0:
                            r_attack = r_7
                            c_attack = c_7
                    elif test9 in attack_area:
                        if balloon1.ret_isdead() == 0:
                            r_attack = r_8
                            c_attack = c_8
                    elif test10 in attack_area:
                        if balloon1.ret_isdead() == 0:
                            r_attack = r_9
                            c_attack = c_9
                    elif test2 in attack_area:
                        if barbarian1.ret_isdead() == 0:
                            r_attack = r_b1
                            c_attack = c_b1
                    elif test3 in attack_area:
                        if barbarian2.ret_isdead() == 0:
                            r_attack = r_b2
                            c_attack = c_b2
                    elif test4 in attack_area:
                        if barbarian3.ret_isdead() == 0:
                            r_attack = r_b3
                            c_attack = c_b3
                    elif test5 in attack_area:
                        if archer1.ret_isdead() == 0:
                            r_attack = r_b4
                            c_attack = c_b4
                    elif test6 in attack_area:
                        if archer2.ret_isdead() == 0:
                            r_attack = r_b5
                            c_attack = c_b5
                    elif test7 in attack_area:
                        if archer3.ret_isdead() == 0:
                            r_attack = r_b6
                            c_attack = c_b6

                    attack_area_main = set()

                    # setting attack_area_main
                    for i in range(WizardTower().new_range + 1):
                        for j in range(WizardTower().new_range + 1):
                            attack_area_main.add((r_attack + i, c_attack + j))
                            attack_area_main.add((r_attack + i, c_attack - j))
                            attack_area_main.add((r_attack - i, c_attack + j))
                            attack_area_main.add((r_attack - i, c_attack - j))

                    if test1 in attack_area_main:
                        if king.ret_isdead() == 0:
                            king.on_attack(WizardTower().damage)
                            attack = True
                    if test2 in attack_area_main:
                        if barbarian1.ret_isdead() == 0:
                            barbarian1.on_attack(WizardTower().damage)
                            attack = True
                    if test3 in attack_area_main:
                        if barbarian2.ret_isdead() == 0:
                            barbarian2.on_attack(WizardTower().damage)
                            attack = True
                    if test4 in attack_area_main:
                        if barbarian3.ret_isdead() == 0:
                            barbarian3.on_attack(WizardTower().damage)
                            attack = True
                    if test5 in attack_area_main:
                        if archer1.ret_isdead() == 0:
                            archer1.on_attack(WizardTower().damage)
                            attack = True
                    if test6 in attack_area_main:
                        if archer2.ret_isdead() == 0:
                            archer2.on_attack(WizardTower().damage)
                            attack = True
                    if test7 in attack_area_main:
                        if archer3.ret_isdead() == 0:
                            archer3.on_attack(WizardTower().damage)
                            attack = True
                    if test8 in attack_area_main:
                        if balloon1.ret_isdead() == 0:
                            balloon1.on_attack(WizardTower().damage)
                            attack = True
                    if test9 in attack_area_main:
                        if balloon2.ret_isdead() == 0:
                            balloon2.on_attack(WizardTower().damage)
                            attack = True
                    if test10 in attack_area_main:
                        if balloon3.ret_isdead() == 0:
                            balloon3.on_attack(WizardTower().damage)
                            attack = True

                    if attack:
                        screen[r][c] = WizardTower().ret_type() + 1
                        # os.system("aplay -q ./sounds/explosion.wav &")
                    else:
                        screen[r][c] = WizardTower().ret_type()

    # showing all the buildings
    def show(this, screen, x):
        for i in range(game_ht[1]):
            for j in range(game_wd[1]):
                if this.a[i][j] != 0 and screen[i][j] == " ":
                    screen[i][j] = this.a[i][j]
        for building in this.buildings:
            if building.ret_type() != Wall().ret_type():
                s1 = building.ret_row_size()
                s2 = building.ret_col_size()
                if building.ret_isdestroyed() == 1:
                    for i in range(s1):
                        for j in range(s2):
                            screen[building.ret_row() + i][building.ret_col() + j] = " "

            elif building.ret_type() == Wall().ret_type():
                s1 = building.ret_row_size()
                s2 = building.ret_col_size()

                if building.ret_isdestroyed() == 1:
                    for i in range(s1):
                        for j in range(s2):
                            if (
                                screen[building.ret_row() + i][building.ret_col() + j]
                                == 3
                            ):
                                screen[building.ret_row() + i][
                                    building.ret_col() + j
                                ] = " "


# Inheritance implemented. Building is the parent class. Town Hall, Huts, Cannon, Wall are child classes.


class Building:
    # Building Object
    def __init__(this):
        this.__health = 0
        this.__type = 0
        this.__row = 0
        this.__col = 0
        this.__isdestroyed = 0
        this.__row_size = 0
        this.__col_size = 0

    # encapsulation
    def ret_health(this):
        return this.__health

    def upd_health(this, x):
        this.__health = x

    def ret_type(this):
        return this.__type

    def upd_type(this, x):
        this.__type = x

    def ret_row(this):
        return this.__row

    def upd_row(this, x):
        this.__row = x

    def ret_col(this):
        return this.__col

    def upd_col(this, x):
        this.__col = x

    def ret_isdestroyed(this):
        return this.__isdestroyed

    def upd_isdestroyed(this, x):
        this.__isdestroyed = x

    def ret_row_size(this):
        return this.__row_size

    def upd_row_size(this, x):
        this.__row_size = x

    def ret_col_size(this):
        return this.__col_size

    def upd_col_size(this, x):
        this.__col_size = x

    def on_attack(this, damage):
        this.upd_health(this.ret_health() - damage)
        if this.ret_health() <= 0:
            this.upd_isdestroyed(1)


class TownHall(Building):
    def __init__(this):
        Building.__init__(this)
        this.upd_type(1)
        this.upd_health(100)
        this.upd_row_size(4)
        this.upd_col_size(3)


class Hut(Building):
    def __init__(this):
        Building.__init__(this)
        this.upd_type(2)
        this.upd_health(50)
        this.upd_row_size(2)
        this.upd_col_size(2)


class Wall(Building):
    def __init__(this):
        Building.__init__(this)
        this.upd_type(3)
        this.upd_health(30)
        this.upd_row_size(1)
        this.upd_col_size(1)


class Cannon(Building):
    def __init__(this):
        Building.__init__(this)
        this.upd_type(4)
        this.upd_health(20)
        this.upd_row_size(1)
        this.upd_col_size(1)
        this.range = 5  # 5 tiles
        this.damage = 2  # 1 shot = 2 health


class WizardTower(Building):
    def __init__(this):
        Building.__init__(this)
        this.upd_type(6)
        this.upd_health(200)
        this.upd_row_size(1)
        this.upd_col_size(1)
        this.range = Cannon().range  # same as cannon
        this.new_range = 3
        this.damage = Cannon().damage
