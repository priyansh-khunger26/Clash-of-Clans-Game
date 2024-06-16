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
import keyboard
import time
from person.Queen import Queen
from person.arhcer import Archer
from person.Balloon import Balloon
from spawning_point import SpawningPoint
from buildings.Wizard_tower import Wizard

action_log = []

my_village = Village(22, 50)

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
Canon3 = Cannon()
Canon4 = Cannon()

Canon1._place_building(6,22,my_village)
Canon2._place_building(14,25,my_village)
Canon3._place_building(11,20,my_village)
Canon4._place_building(8,27,my_village)

Wizard1 = Wizard()
Wizard2 = Wizard()
Wizard3 = Wizard()
Wizard4 = Wizard()

Wizard1._place_building(6, 25, my_village)
Wizard2._place_building(8, 20, my_village)
Wizard3._place_building(11, 27, my_village)
Wizard4._place_building(14, 22, my_village)

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
key = keyboard.read_key()
if key == "q":
    str = "Queen chosen"
    action_log.append(str)
    main_character = queen
    my_village.queen = queen
elif key == "k":
    str = "king chosen"
    action_log.append(str)
    my_village.king = king
    main_character = king

# new_key = keyboard.read_key()
# if new_key == '1':
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


archer_array = [False, False, False, False, False, False]

king_loc = False
    
while True:
    key = keyboard.read_key()
    
    if key == 'w':
        if main_character == queen:
            main_character.direction = "up"
            str = "queen up"
            action_log.appen(str)
        main_character.move(my_village, main_character.position[0] - 1, main_character.position[1])
        str = "mc up"
        action_log.append(str)
        if main_character.movement_speed > 1:
            main_character.move(my_village, main_character.position[0] - 1, main_character.position[1])
            str="mc double up"
            action_log.append(str)
    elif key == 'a':
        if main_character == queen:
            main_character.direction = "left"
            str = "queen left"
            action_log.append(str)
        main_character.move(my_village, main_character.position[0], main_character.position[1] - 1)
        str = "mc left"
        action_log.append(str)
        if main_character.movement_speed > 1:
            main_character.move(my_village, main_character.position[0], main_character.position[1] - 1)
            str = "mc again left"
            action_log.append(str)
    elif key == 's':
        if main_character == queen:
            main_character.direction = "down"
            str = "queen down"
            action_log.append(str)
        main_character.move(my_village, main_character.position[0] + 1, main_character.position[1])
        str = "mc down"
        action_log.append(str)
        if main_character.movement_speed > 1:
            main_character.move(my_village, main_character.position[0] + 1, main_character.position[1])
            str = "mc again down"
            action_log.append(str)
    elif key == 'd':
        if main_character == queen:
            main_character.direction = "right"
            str = "queen right"
            action_log.append(str)
        main_character.move(my_village, main_character.position[0], main_character.position[1] + 1)
        str = "mc right"
        action_log.append(str)
        if main_character.movement_speed > 1:
            main_character.move(my_village, main_character.position[0], main_character.position[1] + 1)
            str = "mc again right"
            action_log.append(str)
    elif key == 'r':
        main_character.apply_spell(rage)
        helper_rage = True        
        
        for i in range(0, list_count_barbarians):
            list_of_barbarians[i].apply_spell(rage)
            
        for i in range(0, list_count_archers):
            list_of_archers[i].apply_spell(rage)
            
        for i in range(0, list_count_balloons):
            list_of_balloons[i].apply_spell(rage)
            
        str = "rs activate"
        action_log.append(str)
    elif key == 'h':
        main_character.apply_spell(heal)
        helper_heal = True        
        
        for i in range(0, list_count_barbarians):
            list_of_barbarians[i].apply_spell(heal)
            
        for i in range(0, list_count_archers):
            list_of_archers[i].apply_spell(heal)
            
        for i in range(0, list_count_balloons):
            list_of_balloons[i].apply_spell(heal)
        
        str = "hs activate"
        action_log.append(str)
    elif key == '1':
        if list_count_barbarians < 6:
            list_of_barbarians[list_count_barbarians].place_person(my_village, spawning_point1.location[0],spawning_point1.location[1])
            list_count_barbarians = list_count_barbarians + 1
            str = "place barbarian sp1"
            action_log.append(str)
    elif key == '2':
        if list_count_barbarians < 6:
            list_of_barbarians[list_count_barbarians].place_person(my_village, spawning_point2.location[0],spawning_point2.location[1])
            list_count_barbarians = list_count_barbarians + 1
            str = "place barbarian sp2"
            action_log.append(str)
    elif key == '3':
        if list_count_barbarians < 6:
            list_of_barbarians[list_count_barbarians].place_person(my_village, spawning_point3.location[0],spawning_point3.location[1])
            list_count_barbarians = list_count_barbarians + 1
            str = "place barbarian sp3"
            action_log.append(str)
    elif key == '4':
        if list_count_archers < 6:
            list_of_archers[list_count_archers].place_person(my_village, spawning_point1.location[0],spawning_point1.location[1])
            list_count_archers = list_count_archers + 1
            str = "place archer sp1"
            action_log.append(str)
    elif key == '5':
        if list_count_archers < 6:
            list_of_archers[list_count_archers].place_person(my_village, spawning_point2.location[0],spawning_point2.location[1])
            list_count_archers = list_count_archers + 1
            str = "place archer sp2"
            action_log.append(str)
    elif key == '6':
        if list_count_archers < 6:
            list_of_archers[list_count_archers].place_person(my_village, spawning_point3.location[0],spawning_point3.location[1])
            list_count_archers = list_count_archers + 1
            str = "place archer sp3"
            action_log.append(str)
    elif key == '7':
        if list_count_balloons < 6:
            list_of_balloons[list_count_balloons].place_person(my_village, spawning_point1.location[0],spawning_point1.location[1])
            list_count_balloons = list_count_balloons + 1
            str = "place balloon sp1"
            action_log.append(str)
    elif key == '8':
        if list_count_balloons < 6:
            list_of_balloons[list_count_balloons].place_person(my_village, spawning_point2.location[0],spawning_point2.location[1])
            list_count_balloons = list_count_balloons + 1
            str = "place balloon sp2"
            action_log.append(str)
    elif key == '9':
        if list_count_balloons < 6:
            list_of_balloons[list_count_balloons].place_person(my_village, spawning_point3.location[0],spawning_point3.location[1])
            list_count_balloons = list_count_balloons + 1
            str = "place balloon sp3"
            action_log.append(str)
    elif key == 'space':
        if main_character == queen:
            main_character.attack(my_village)
            str = "queen attack"
            action_log.append(str)
        else:
            main_character.scan_and_attack(my_village)
            str = "king attack"
            action_log.append(str)
    
    for i in range(0, list_count_barbarians):
        new_temp = list_of_barbarians[i].health
        if new_temp > 0:
            list_of_barbarians[i].scan_and_attack(my_village)
            list_of_barbarians[i].move_towards_nearest_building(my_village)
            if i == 0:
                str = "barbarian 0 attack"
                action_log.append(str)
            elif i == 1:
                str = "barbarian 1 attack"
                action_log.append(str)
            elif i == 2:
                str = "barbarian 2 attack"
                action_log.append(str)
            elif i == 3:
                str = "barbarian 3 attack"
                action_log.append(str)
            elif i == 4:
                str = "barbarian 4 attack"
                action_log.append(str)
            elif i == 5:
                str = "barbarian 5 attack"
                action_log.append(str)
                
        
    for i in range(0, list_count_archers):
        new_temp = list_of_archers[i].health
        if new_temp > 0:
            archer_array[i] = list_of_archers[i].scan_and_attack(my_village)
            if i == 0:
                str = "archer 0 attack"
                action_log.append(str)
            elif i == 1:
                str = "archer 1 attack"
                action_log.append(str)
            elif i == 2:
                str = "archer 2 attack"
                action_log.append(str)
            elif i == 3:
                str = "archer 3 attack"
                action_log.append(str)  
            elif i == 4:
                str = "archer 4 attack"
                action_log.append(str)  
            elif i == 5:
                str = "archer 5 attack"
                action_log.append(str)
                
            
            if archer_array[i]:
                list_of_archers[i].move_towards_nearest_building(my_village)
                if i == 0:
                    str = "archer 0 move"
                    action_log.append(str)
                elif i == 1:
                    str = "archer 1 move"
                    action_log.append(str)
                elif i == 2:
                    str = "archer 2 move"
                    action_log.append(str)
                elif i == 3:
                    str = "archer 3 move"
                    action_log.append(str)
                elif i == 4:
                    str = "archer 4 move"
                    action_log.append(str)
                elif i == 5:
                    str = "archer 5 move"
                    action_log.append(str)
            
    for i in range(0, list_count_balloons):
        new_temp = list_of_balloons[i].health
        if new_temp > 0:
            if i == 0:
                str = "balloon 0 find"
                action_log.append(str)
            elif i == 1:
                str = "balloon 1 find"
                action_log.append(str)
            elif i == 2:
                str = "balloon 2 find"
                action_log.append(str)
            elif i == 3:
                str = "balloon 3 find"
                action_log.append(str)
            elif i == 4:
                str = "balloon 4 find"
                action_log.append(str)
            elif i == 5:
                str = "balloon 5 find"
                action_log.append(str)
                
            temp = list_of_balloons[i]._find_nearest_building(my_village)
            if temp:
                if list_of_balloons[i].move(temp, my_village) == "ok":
                    if i == 0:
                        str = "balloon 0 stopped"
                        action_log.append(str)
                    elif i == 1:
                        str = "balloon 1 stopped"
                        action_log.append(str)
                    elif i == 2:
                        str = "balloon 2 stopped"
                        action_log.append(str)
                    elif i == 3:
                        str = "balloon 3 stopped"
                        action_log.append(str)
                    elif i == 4:
                        str = "balloon 4 stopped"
                        action_log.append(str)
                    elif i == 5:
                        str = "balloon 5 stopped"
                        action_log.append(str)
                    
                    break
                elif list_of_balloons[i].move(temp, my_village) == True:
                    if list_of_balloons[i].attack(my_village):
                        if i == 0:
                            str = "balloon 0 finish"
                            action_log.append(str)
                        elif i == 1:
                            str = "balloon 1 finish"
                            action_log.append(str)
                        elif i == 2:
                            str = "balloon 2 finish"
                            action_log.append(str)
                        elif i == 3:
                            str = "balloon 3 finish"
                            action_log.append(str)
                        elif i == 4:
                            str = "balloon 4 finish"
                            action_log.append(str)
                        elif i == 5:
                            str = "balloon 5 finish"
                            action_log.append(str)
                        
                        row, col = list_of_balloons[i].position
                        my_village.grid[row][col] = list_of_balloons[i]
        
    if isinstance(my_village.grid[6][22], Cannon):
        Canon1.scan_and_attack(my_village)
        str = "cannon1 attack"
        action_log.append(str)
    
    if isinstance(my_village.grid[14][25], Cannon):
        Canon2.scan_and_attack(my_village)
        str = "cannon2 attack"
        action_log.append(str)
        
    if isinstance(my_village.grid[11][20], Cannon):
        Canon3.scan_and_attack(my_village)
        str = "cannon3 attack"
        action_log.append(str)
    
    if isinstance(my_village.grid[8][27], Cannon):
        Canon4.scan_and_attack(my_village)
        str = "cannon4 attack"
        action_log.append(str)
        
    if isinstance(my_village.grid[6][25], Wizard):
        Wizard1.scan_and_attack(my_village)
        str = "wizard1 sttack"
        action_log.append(str)
        
    if isinstance(my_village.grid[8][20], Wizard):
        Wizard2.scan_and_attack(my_village)
        str = "wizard2 sttack"
        action_log.append(str)
        
    if isinstance(my_village.grid[11][27], Wizard):
        Wizard3.scan_and_attack(my_village)
        str = "wizard3 sttack"
        action_log.append(str)
        
    if isinstance(my_village.grid[14][22], Wizard):
        Wizard4.scan_and_attack(my_village)
        str = "wizard4 attack"
        action_log.append(str)
        
    if my_village.all_buildings_destroyed():
        game2 = True
        print("\nAll buildings destroyed! You win")
        str = "win"
        action_log.append(str)
        break
    
    if my_village.all_troops_destroyed():
        print("\nAll troops destroyed! You lose!")
        str = "game over"
        action_log.append(str)
        break
    
    if helper_rage :
        if count_rage >= 15: 
            main_character.remove_spell(rage)

            for i in range(0, list_count_barbarians):
                list_of_barbarians[i].remove_spell(rage)
                
            for i in range(0, list_count_archers):
                list_of_archers[i].remove_spell(rage)
                
            for i in range(0, list_count_balloons):
                list_of_balloons[i].remove_spell(rage)
                    
            count_rage = 0
            helper_rage = False
            
            str = "rg remove"
            action_log.append(str)
        else:
            count_rage += 1
            
    if helper_heal :
        if count_heal >= 15: 
            main_character.remove_spell(heal)

            for i in range(0, list_count_barbarians):
                list_of_barbarians[i].remove_spell(heal)
                
            for i in range(0, list_count_archers):
                list_of_archers[i].remove_spell(heal)
                
            for i in range(0, list_count_balloons):
                list_of_balloons[i].remove_spell(heal)
                    
            count_heal = 0
            helper_heal = False
            
            str = "hs remove"
            action_log.append(str)
        else:
            count_heal += 1
        
    time.sleep(0.25)
    my_village.display_village()
    str = "display"
    action_log.append(str)
        
    print()
    
file_path = 'action_log2.json'

with open(file_path, 'w') as file:
    json.dump(action_log, file, indent=4)