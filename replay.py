from buildings.town_hall import TownHall
from buildings.hut import Hut
from buildings.Wall import Wall
from buildings.cannon import Cannon
from person.King import King
from village import Village
from person.Barbarian import Barbarian
from spells.heal_spell import HealSpell
from spells.rage_spell import RageSpell
import json
import time
from person.Queen import Queen
from person.arhcer import Archer
from person.Balloon import Balloon
from spawning_point import SpawningPoint
from buildings.Wizard_tower import Wizard
import subprocess


# File path to load the list from
file_path = 'action_log.json'

# Load the list from the JSON file
with open(file_path, 'r') as file:
    action_log = json.load(file)

my_village = Village(22, 50)

game_1 = False

townHall = TownHall()
townHall._place_building(9,23, my_village)

list_of_walls = []
for i in range(0,19):
    temp = Wall()
    list_of_walls.append(temp)

list_of_walls[0]._place_building(8,22, my_village)
list_of_walls[1]._place_building(8,23, my_village)
list_of_walls[2]._place_building(8,24, my_village)
list_of_walls[3]._place_building(8,25, my_village)
list_of_walls[4]._place_building(8,26, my_village)
list_of_walls[5]._place_building(9,22, my_village)
list_of_walls[6]._place_building(10,22, my_village)
list_of_walls[7]._place_building(11,22, my_village)
list_of_walls[8]._place_building(12,22, my_village)
list_of_walls[9]._place_building(13,22, my_village)
list_of_walls[10]._place_building(13,23, my_village)
list_of_walls[11]._place_building(13,24, my_village)
list_of_walls[12]._place_building(13,25, my_village)
list_of_walls[13]._place_building(13,26, my_village)
list_of_walls[14]._place_building(12,26, my_village)
list_of_walls[15]._place_building(11,26, my_village)
list_of_walls[16]._place_building(10,26, my_village)
list_of_walls[17]._place_building(9,26, my_village)
list_of_walls[18]._place_building(8,26, my_village)

Canon1 = Cannon()
Canon2 = Cannon()
# Canon3 = Cannon()
# Canon4 = Cannon()

Canon1._place_building(6,22,my_village)
Canon2._place_building(14,25,my_village)
# Canon3._place_building(11,20,my_village)
# Canon4._place_building(8,27,my_village)

Wizard1 = Wizard()
Wizard2 = Wizard()
# Wizard3 = Wizard()
# Wizard4 = Wizard()

Wizard1._place_building(6, 25, my_village)
Wizard2._place_building(8, 20, my_village)
# Wizard3._place_building(11, 27, my_village)
# Wizard4._place_building(14, 22, my_village)

hut1 = Hut()
hut2 = Hut()
hut3 = Hut()
hut4 = Hut()
hut5 = Hut()
hut6 = Hut()

hut1._place_building(5,22,my_village)
hut2._place_building(13,20,my_village)
hut3._place_building(10,18,my_village)
hut4._place_building(10,16,my_village)
hut5._place_building(10,29,my_village)
hut6._place_building(10,49,my_village)

spawning_point1 = SpawningPoint((5,12))
spawning_point2 = SpawningPoint((13,9))
spawning_point3 = SpawningPoint((19,25))

spawning_point1.add_spawning_point(my_village)
spawning_point2.add_spawning_point(my_village)
spawning_point3.add_spawning_point(my_village)

king = King()
queen = Queen()
main_character = king

if action_log[0] == "Queen chosen":
    main_character = queen
    my_village.queen = queen
elif action_log[0] == "king chosen":
    my_village.king = king
    main_character = king

main_character.place_person(my_village, spawning_point1.location[0],spawning_point1.location[1])
# elif new_key == '2':
#     main_character.place_person(my_village, spawning_point2.location[0],spawning_point2.location[1])
# elif new_key == '3':
#     main_character.place_person(my_village, spawning_point3.location[0],spawning_point3.location[1])

barbarian1 = Barbarian()
barbarian2 = Barbarian()
barbarian3 = Barbarian()
barbarian4 = Barbarian()
barbarian5 = Barbarian()
barbarian6 = Barbarian()

list_of_barbarians = [barbarian1, barbarian2, barbarian3, barbarian4, barbarian5, barbarian6]
list_count_barbarians = 0

archer1 = Archer()
archer2 = Archer()
archer3 = Archer()
archer4 = Archer()
archer5 = Archer()
archer6 = Archer()

list_of_archers = [archer1, archer2, archer3, archer4, archer5, archer6]
list_count_archers = 0

balloon1 = Balloon()
balloon2 = Balloon()
balloon3 = Balloon()
balloon4 = Balloon()
balloon5 = Balloon()
balloon6 = Balloon()

list_of_balloons = [balloon1, balloon2, balloon3, balloon4, balloon5, balloon6]
list_count_balloons = 0

rage = RageSpell(15)
count_rage = 0
helper_rage = False

heal = HealSpell(15)
count_heal = 0
helper_heal = False

my_village.display_village()


archer_array = [False, False, False, False, False, False]

king_loc = False


for i in action_log:
    time.sleep(0.1)
    if i == "queen up":
        main_character.direction = "up"
    elif i == "mc up":
        main_character.move(my_village, main_character.position[0] - 1, main_character.position[1])
    elif i == "mc double up":
        main_character.move(my_village, main_character.position[0] - 1, main_character.position[1])
    elif i == "queen left":
        main_character.direction = "left"
    elif i == "mc left":
        main_character.move(my_village, main_character.position[0], main_character.position[1] - 1)
    elif i == "mc again left":
        main_character.move(my_village, main_character.position[0], main_character.position[1] - 1)
    elif i == "queen down":
        main_character.direction = "down"
    elif i == "mc down":
        main_character.move(my_village, main_character.position[0] + 1, main_character.position[1])
    elif i == "mc again down":
        main_character.move(my_village, main_character.position[0] + 1, main_character.position[1])
    elif i == "queen right":
        main_character.direction = "right"
    elif i == "mc right":
        main_character.move(my_village, main_character.position[0], main_character.position[1] + 1)
    elif i == "mc again right":
        main_character.move(my_village, main_character.position[0], main_character.position[1] + 1)
    elif i == "rs activate":
        main_character.apply_spell(rage)      
        
        for i in range(0, list_count_barbarians):
            list_of_barbarians[i].apply_spell(rage)
            
        for i in range(0, list_count_archers):
            list_of_archers[i].apply_spell(rage)
            
        for i in range(0, list_count_balloons):
            list_of_balloons[i].apply_spell(rage)
    elif i == "hs activate":
        main_character.apply_spell(heal)    
        
        for i in range(0, list_count_barbarians):
            list_of_barbarians[i].apply_spell(heal)
            
        for i in range(0, list_count_archers):
            list_of_archers[i].apply_spell(heal)
            
        for i in range(0, list_count_balloons):
            list_of_balloons[i].apply_spell(heal)
    elif i == "place barbarian sp1":
        list_of_barbarians[list_count_barbarians].place_person(my_village, spawning_point1.location[0],spawning_point1.location[1])
        list_count_barbarians = list_count_barbarians + 1
    elif i == "place barbarian sp2":
        list_of_barbarians[list_count_barbarians].place_person(my_village, spawning_point2.location[0],spawning_point2.location[1])
        list_count_barbarians = list_count_barbarians + 1
    elif i == "place barbarian sp3":
        list_of_barbarians[list_count_barbarians].place_person(my_village, spawning_point3.location[0],spawning_point3.location[1])
        list_count_barbarians = list_count_barbarians + 1
    elif i == "place archer sp1":
        list_of_archers[list_count_archers].place_person(my_village, spawning_point1.location[0],spawning_point1.location[1])
        list_count_archers = list_count_archers + 1
    elif i == "place archer sp2":
        list_of_archers[list_count_archers].place_person(my_village, spawning_point2.location[0],spawning_point2.location[1])
        list_count_archers = list_count_archers + 1
    elif i == "place archer sp3":
        list_of_archers[list_count_archers].place_person(my_village, spawning_point3.location[0],spawning_point3.location[1])
        list_count_archers = list_count_archers + 1
    elif i == "place balloon sp1":
        list_of_balloons[list_count_balloons].place_person(my_village, spawning_point1.location[0],spawning_point1.location[1])
        list_count_balloons = list_count_balloons + 1
    elif i == "place balloon sp2":
        list_of_balloons[list_count_balloons].place_person(my_village, spawning_point2.location[0],spawning_point2.location[1])
        list_count_balloons = list_count_balloons + 1
    elif i == "place balloon sp3":
        list_of_balloons[list_count_balloons].place_person(my_village, spawning_point3.location[0],spawning_point3.location[1])
        list_count_balloons = list_count_balloons + 1
    elif i == "queen attack":
        main_character.attack(my_village)
    elif i == "king attack":
        main_character.scan_and_attack(my_village)
    elif i == "barbarian 0 attack":
        list_of_barbarians[0].scan_and_attack(my_village)
        list_of_barbarians[0].move_towards_nearest_building(my_village)
    elif i == "barbarian 1 attack":
        list_of_barbarians[1].scan_and_attack(my_village)
        list_of_barbarians[1].move_towards_nearest_building(my_village)
    elif i == "barbarian 2 attack":
        list_of_barbarians[2].scan_and_attack(my_village)
        list_of_barbarians[2].move_towards_nearest_building(my_village)
    elif i == "barbarian 3 attack":
        list_of_barbarians[3].scan_and_attack(my_village)
        list_of_barbarians[3].move_towards_nearest_building(my_village)
    elif i == "barbarian 4 attack":
        list_of_barbarians[4].scan_and_attack(my_village)
        list_of_barbarians[4].move_towards_nearest_building(my_village)
    elif i == "barbarian 5 attack":
        list_of_barbarians[5].scan_and_attack(my_village)
        list_of_barbarians[5].move_towards_nearest_building(my_village)
    elif i == "archer 0 attack":
        archer_array[0] = list_of_archers[0].scan_and_attack(my_village)
    elif i == "archer 1 attack":
        archer_array[1] = list_of_archers[1].scan_and_attack(my_village)
    elif i == "archer 2 attack":
        archer_array[2] = list_of_archers[2].scan_and_attack(my_village)
    elif i == "archer 3 attack":
        archer_array[3] = list_of_archers[3].scan_and_attack(my_village)
    elif i == "archer 4 attack":
        archer_array[4] = list_of_archers[4].scan_and_attack(my_village)
    elif i == "archer 5 attack":
        archer_array[5] = list_of_archers[5].scan_and_attack(my_village)
    elif i == "archer 0 move":
        list_of_archers[0].move_towards_nearest_building(my_village)
    elif i == "archer 1 move":
        list_of_archers[1].move_towards_nearest_building(my_village)
    elif i == "archer 2 move":
        list_of_archers[2].move_towards_nearest_building(my_village)
    elif i == "archer 3 move":
        list_of_archers[3].move_towards_nearest_building(my_village)
    elif i == "archer 4 move":
        list_of_archers[4].move_towards_nearest_building(my_village)
    elif i == "archer 5 move":
        list_of_archers[5].move_towards_nearest_building(my_village)
    elif i == "balloon 0 find":
        temp = list_of_balloons[0]._find_nearest_building(my_village)
    elif i == "balloon 1 find":
        temp = list_of_balloons[1]._find_nearest_building(my_village)
    elif i == "balloon 2 find":
        temp = list_of_balloons[2]._find_nearest_building(my_village)
    elif i == "balloon 3 find":
        temp = list_of_balloons[3]._find_nearest_building(my_village)
    elif i == "balloon 4 find":
        temp = list_of_balloons[4]._find_nearest_building(my_village)
    elif i == "balloon 5 find":
        temp = list_of_balloons[5]._find_nearest_building(my_village)
    elif i == "cannon1 attack":
        Canon1.scan_and_attack(my_village)
    elif i == "cannon2 attack":
        Canon2.scan_and_attack(my_village)
    elif i == "wizard1 sttack":
        Wizard1.scan_and_attack(my_village)
    elif i == "wizard2 attack":
        Wizard2.scan_and_attack(my_village)
    elif i == "game over":
        print("\nAll troops destroyed! You lose!")
        break
    elif i == "rg remove":
        main_character.remove_spell(rage)

        for i in range(0, list_count_barbarians):
            list_of_barbarians[i].remove_spell(rage)
            
        for i in range(0, list_count_archers):
            list_of_archers[i].remove_spell(rage)
            
        for i in range(0, list_count_balloons):
            list_of_balloons[i].remove_spell(rage)
                
        count_rage = 0
        helper_rage = False
    elif i == "hs remove":
        main_character.remove_spell(heal)

        for i in range(0, list_count_barbarians):
            list_of_barbarians[i].remove_spell(heal)
            
        for i in range(0, list_count_archers):
            list_of_archers[i].remove_spell(heal)
            
        for i in range(0, list_count_balloons):
            list_of_balloons[i].remove_spell(heal)
                
        count_heal = 0
        helper_heal = False
    elif i == "display":
        my_village.display_village()
    elif i == "balloon 0 stopped":
        list_of_balloons[0].move(temp, my_village)
    elif i == "balloon 1 stopped":
        list_of_balloons[1].move(temp, my_village)
    elif i == "balloon 2 stopped":
        list_of_balloons[2].move(temp, my_village)
    elif i == "balloon 3 stopped":
        list_of_balloons[3].move(temp, my_village)
    elif i == "balloon 4 stopped":
        list_of_balloons[4].move(temp, my_village)
    elif i == "ballon 5 stopped":
        list_of_balloons[5].move(temp, my_village)
    elif i == "balloon 0 finish":
        list_of_balloons[0].attack(my_village)
        row, col = list_of_balloons[0].position
        my_village.grid[row][col] = list_of_balloons[0]
    elif i == "balloon 1 finish":
        list_of_balloons[1].attack(my_village)
        row, col = list_of_balloons[1].position
        my_village.grid[row][col] = list_of_balloons[1]
    elif i == "balloon 2 finish":
        list_of_balloons[2].attack(my_village)
        row, col = list_of_balloons[2].position
        my_village.grid[row][col] = list_of_balloons[2]
    elif i == "balloon 3 finish":
        list_of_balloons[3].attack(my_village)
        row, col = list_of_balloons[3].position
        my_village.grid[row][col] = list_of_balloons[3]
    elif i == "balloon 4 finish":
        list_of_balloons[4].attack(my_village)
        row, col = list_of_balloons[4].position
        my_village.grid[row][col] = list_of_balloons[4]
    elif i == "balloon 5 finish":
        list_of_balloons[5].attack(my_village)
        row, col = list_of_balloons[5].position
        my_village.grid[row][col] = list_of_balloons[5]
    elif i == "shift to level2":
        subprocess.run(['python3', 'replay2.py'])
    