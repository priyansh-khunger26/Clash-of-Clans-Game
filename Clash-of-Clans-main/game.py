from distutils.command.build import build
import os
from tracemalloc import start

from graphviz import render
from src.screen import *
from src.constants import *
from src.background import *
from src.buildings import *
from src.king import *
from src.barbarians import *
from src.spells import *
from src.input import *
from src.queen import *
from src.archer import *
from src.balloon import *
import time


os.system("clear")

# setting area of screen where game will be played
comp_screen = Screen(s_height, s_width)

# making a boundary for the village
background = Background()

# creating instance for Buildings class
buildings = Buildings()

# creating instance for King class
king = King()

# creating instance for Queen class
queen = Queen()

# creating instance for Spells class
spells = Spells()

# creating 1st troop
barbarian1 = Barbarians()
archer1 = Archer()
balloon1 = Balloon()
barbarian1.upd_col(game_wd[0] + 1)
archer1.upd_col(game_wd[0] + 1)
balloon1.upd_col(game_wd[0] + 1)

# creating 2nd troop
barbarian2 = Barbarians()
archer2 = Archer()
balloon2 = Balloon()
barbarian2.upd_col(game_wd[0] + 11)
archer2.upd_col(game_wd[0] + 11)
balloon2.upd_col(game_wd[0] + 11)

# creating 3rd troop
barbarian3 = Barbarians()
archer3 = Archer()
balloon3 = Balloon()
barbarian3.upd_col(game_wd[0] + 21)
archer3.upd_col(game_wd[0] + 21)
balloon3.upd_col(game_wd[0] + 21)

get = Get()
start_time = time.time()
render_time = time.time()
collapeseTime = time.time()
pause = 0
forward = 0
x = []
# global level
level = Level()


def reset():
    # x.append('here')
    global comp_screen
    global background
    # global buildings
    global king
    global queen
    global spells
    global barbarian1
    global barbarian2
    global barbarian3
    global archer1
    global archer2
    global archer3
    global balloon1
    global balloon2
    global balloon3
    global get
    global start_time
    global render_time
    global collapeseTime

    # setting area of screen where game will be played
    comp_screen = Screen(s_height, s_width)

    # making a boundary for the village
    background = Background()

    # creating instance for Buildings class
    # buildings = Buildings()

    # creating instance for King class
    king = King()

    # creating instance for Queen class
    queen = Queen()

    # creating instance for Spells class
    spells = Spells()

    # creating 1st troop
    barbarian1.reset()
    barbarian1 = Barbarians()
    archer1.reset()
    archer1 = Archer()
    balloon1.reset()
    balloon1 = Balloon()
    barbarian1.upd_col(game_wd[0] + 1)
    archer1.upd_col(game_wd[0] + 1)
    balloon1.upd_col(game_wd[0] + 1)

    # creating 2nd troop
    barbarian2.reset()
    barbarian2 = Barbarians()
    archer2.reset()
    archer2 = Archer()
    balloon2.reset()
    balloon2 = Balloon()
    barbarian2.upd_col(game_wd[0] + 11)
    archer2.upd_col(game_wd[0] + 11)
    balloon2.upd_col(game_wd[0] + 11)

    # creating 3rd troop
    barbarian3.reset()
    barbarian3 = Barbarians()
    archer3.reset()
    archer3 = Archer()
    balloon3.reset()
    balloon3 = Balloon()
    barbarian3.upd_col(game_wd[0] + 21)
    archer3.upd_col(game_wd[0] + 21)
    balloon3.upd_col(game_wd[0] + 21)

    get = Get()
    start_time = time.time()
    render_time = time.time()
    collapeseTime = time.time()
    
    global active1
    active1 = 0
    global active2
    active2 = 0
    global active3
    active3 = 0
    global active4
    active4 = 0
    global active5
    active5 = 0
    global active6
    active6 = 0
    global active7
    active7 = 0
    global active8
    active8 = 0
    global active9
    active9 = 0
    
    os.system("clear")


# generating all the buildings
def generate(buildings, cannons, towers, x):
    buildings.generator(cannons, towers, x)


# for pausing the game
def toggle_pause(pause):
    return 1 - pause


# checking if the game has ended (king has died or all the buildings have been destroyed)
def check_end(king, queen, buildings):
    result = 0
    end = 0
    if king.ret_isdead() or queen.ret_isdead():
        end = 1
        result = 0
        return end, result
    for i in buildings:
        if i.ret_isdestroyed() == 0:
            return end, result

    end = 1
    result = 1
    return end, result


# health bar for the king
def display_healthbar(health, maxHealth, healthDashes):
    dashConvert = int(
        maxHealth / healthDashes
    )  # Get the number to divide by to convert health to dashes (being 10)
    currentDashes = int(
        health / dashConvert
    )  # Convert health to dash count: 80/10 => 8 dashes
    remainingHealth = (
        healthDashes - currentDashes
    )  # Get the health remaining to fill as space => 12 spaces

    healthDisplay = "-" * currentDashes  # Convert dashes as a string:   "--------"
    remainingDisplay = (
        " " * remainingHealth
    )  # Convert spaces as a string: "            "
    percent = (
        str(int((health / maxHealth) * 100)) + "%"
    )  # Get the percent as a whole number:   40%

    print("|" + healthDisplay + remainingDisplay + "|")  # Print out textbased healthbar
    print("         " + percent)


"""
displaying the screen
i.e all the buildings, king, and barbarians (if they have been activated)
"""


def display(king, queen, i, dir, game):
    global active1
    global active2
    global active3
    global active4
    global active5
    global active6
    global active7
    global active8
    global active9
    # x.append(active1)
    background.show(comp_screen.screen)
    buildings.show(comp_screen.screen, x)
    # if len(x) == 0:
    #     x.append(comp_screen.screen) 
    if game == 0:
        king.show(comp_screen.screen)
        buildings.cannon_attack(
            comp_screen.screen,
            king,
            barbarian1,
            barbarian2,
            barbarian3,
            archer1,
            archer2,
            archer3,
        )
        buildings.tower_attack(comp_screen.screen,
            king,
            barbarian1,
            barbarian2,
            barbarian3,
            archer1,
            archer2,
            archer3,
            balloon1,
            balloon2,
            balloon3)
    else:
        queen.show(comp_screen.screen)
        buildings.cannon_attack(
            comp_screen.screen,
            queen,
            barbarian1,
            barbarian2,
            barbarian3,
            archer1,
            archer2,
            archer3,
        )
        buildings.tower_attack(comp_screen.screen,
            queen,
            barbarian1,
            barbarian2,
            barbarian3,
            archer1,
            archer2,
            archer3,
            balloon1,
            balloon2,
            balloon3)
    if active1 == 1:
        barbarian1.predict_path(comp_screen.screen, buildings.buildings)
        barbarian1.show(comp_screen.screen)
    if active2 == 1:
        barbarian2.predict_path(comp_screen.screen, buildings.buildings)
        barbarian2.show(comp_screen.screen)
    if active3 == 1:
        barbarian3.predict_path(comp_screen.screen, buildings.buildings)
        barbarian3.show(comp_screen.screen)
    if active4 == 1:
        archer1.predict_path(comp_screen.screen, buildings.buildings)
        archer1.show(comp_screen.screen)
    if active5 == 1:
        archer2.predict_path(comp_screen.screen, buildings.buildings)
        archer2.show(comp_screen.screen)
    if active6 == 1:
        archer3.predict_path(comp_screen.screen, buildings.buildings)
        archer3.show(comp_screen.screen)
    if active7 == 1:
        balloon1.predict_path(comp_screen.screen, buildings.buildings)
        balloon1.show(comp_screen.screen)
    if active8 == 1:
        balloon2.predict_path(comp_screen.screen, buildings.buildings)
        balloon2.show(comp_screen.screen)
    if active9 == 1:
        balloon3.predict_path(comp_screen.screen, buildings.buildings)
        balloon3.show(comp_screen.screen)
    comp_screen.display(i, dir)
    print("\033[0:0H")  # reposition the cursor


def level_up(x, result):
    global level
    global buildings
    if level.ret_level() == 3:
        over(buildings.buildings, x, result)

    level.upd_level(level.ret_level() + 1)
    reset()
    buildings = Buildings()
    if level.ret_level() == 2:
        generate(buildings, 10,3, x)
        # x.append(comp_screen.screen)
        buildings.show(comp_screen.screen, x)
    elif level.ret_level() == 3:
        generate(buildings, 15,4,x)
        # x.append(comp_screen.screen)
        buildings.show(comp_screen.screen, x)


"""
getting input from user and executing the commands
"""


def get_input(pause, forward, game):
    global active1
    global active2
    global active3
    global active4
    global active5
    global active6
    global active7
    global active8
    global active9
    ch = input_to(get, frametransition)
    # x.append(active1)

    if ch == "w":
        if game == 0:
            king.move_up(comp_screen.screen)
        else:
            queen.move_up(comp_screen.screen)
    if ch == "a":
        if game == 0:
            king.move_left(comp_screen.screen)
        else:
            queen.move_left(comp_screen.screen)
    if ch == "s":
        if game == 0:
            king.move_down(comp_screen.screen)
        else:
            queen.move_down(comp_screen.screen)
    if ch == "d":
        if game == 0:
            king.move_right(comp_screen.screen)
        else:
            queen.move_right(comp_screen.screen)
    if ch == "p":
        return (toggle_pause(pause), forward)
    if ch == " ":
        if game == 0:
            king.attack(comp_screen.screen, buildings.buildings)
        else:
            queen.attack(comp_screen.screen, buildings.buildings)
    if ch == "l":
        barbarian1.show(comp_screen.screen)
        active1 = 1
        barbarian1.upd_active(active1)
    if ch == "m":
        barbarian2.show(comp_screen.screen)
        active2 = 1
        barbarian2.upd_active(active2)
    if ch == "n":
        barbarian3.show(comp_screen.screen)
        active3 = 1
        barbarian3.upd_active(active3)
    if ch == "u":
        archer1.show(comp_screen.screen)
        active4 = 1
        archer1.upd_active(active4)
    if ch == "i":
        archer2.show(comp_screen.screen)
        active5 = 1
        archer2.upd_active(active5)
    if ch == "o":
        archer3.show(comp_screen.screen)
        active6 = 1
        archer3.upd_active(active6)
    if ch == "z":
        balloon1.show(comp_screen.screen)
        active7 = 1
        balloon1.upd_active(active7)
    if ch == "x":
        balloon2.show(comp_screen.screen)
        active8 = 1
        balloon2.upd_active(active8)
    if ch == "c":
        balloon3.show(comp_screen.screen)
        active9 = 1
        balloon3.upd_active(active9)
    if ch == "r":
        spells.spell(barbarian1, barbarian2, barbarian3, king, archer1, archer2, archer3, balloon1, balloon2, balloon3)
    if ch == "h":
        spells.spell(barbarian1, barbarian2, barbarian3, king, archer1, archer2, archer3, balloon1, balloon2, balloon3, 1)
    if ch == "q":
        over(buildings.buildings, x, 0)

    return pause, forward


# main function
if __name__ == "__main__":
    # commands for replay
    i = 0
    path = "replays/"
    dir = len(os.listdir(path))
    dir += 1
    command = "mkdir replays/" + str(dir)
    os.system(command)

    hero = 2
    while hero != 0 or hero != 1:
        hero = int(input("Who is your hero?\n 0. King\n 1.Queen\n"))
        if hero != 0 and hero != 1:
            "incorrect input yr"
        else:
            break

    game = 0
    if hero:
        game = 1

    # checking if barbarians are active
    global active1
    active1 = 0
    global active2
    active2 = 0
    global active3
    active3 = 0
    global active4
    active4 = 0
    global active5
    active5 = 0
    global active6
    active6 = 0
    global active7
    active7 = 0
    global active8
    active8 = 0
    global active9
    active9 = 0

    generate(buildings, 7, 2, x)  # number of huts and wizard towers
    while True:
        i += 1
        pause, forward = get_input(pause, forward, game)

        if forward == 1:
            forward = 0
            pause = 1
        while pause:
            pause, forward = get_input(pause, forward, game)

        if time.time() - render_time >= frametransition:
            end, result = check_end(king, queen, buildings.buildings)
            if end == 1 and result == 1:
                level_up(x, result)
                end = 0
                result = 0
            elif end == 1 and result == 0:
                end = 0
                result = 0
                over(buildings.buildings, x, result)

            display(king, queen, i, dir, game)
            if game == 0:
                display_healthbar(king.ret_health(), king.ret_total_health(), 20)
            else:
                display_healthbar(queen.ret_health(), queen.ret_total_health(), 20)
            render_time = time.time()
