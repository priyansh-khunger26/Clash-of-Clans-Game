# SASTA CLASH OF CLANS

## Style:
+ Code is writern in python3 using OOPS concepts
+ Main OOPS concepts are
    - ###  Encapsulation
        - Using OOP in Python, we can restrict access to methods and variables. This prevents data from direct modification which is called encapsulation. In Python, we denote private attributes using underscore as the prefix i.e single _ or double __.
        For example:
        - In *buildings.py*
        ```python
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
        ```

    - ### Polymorphism
        - Polymorphism is an ability (in OOP) to use a common interface for multiple forms (data types).
            Suppose, we need to color a shape, there are multiple shape options (rectangle, square, circle). However we could use the same method to color any shape. This concept is called Polymorphism.
        - In *spells.py*
    - ### Inhereitance
        - Inheritance is a way of creating a new class for using details of an existing class without modifying it. The newly formed class is a derived class (or child class). Similarly, the existing class is a base class (or parent class).
        - In *buildings.py*
    - ### Abstaraction
        - When methods are named intuitively so as to resemble their actual function. 
        - In *king.py*

## Libraries
+ [python3](https://www.python.org/downloads/)
+ [coloroma](https://pypi.org/project/colorama/)
## Execution
+ After installing the above libraries, Execute the game.py file using below command in the directory folder
```
python3 ./game.py
```

## Information
Sasta Clash of Clans is inspired from the widely popular game CoC. 

+ ### Elements
    - 3 levels implemented. You move n to the next level if you win in the previous one. Each level has a higher number of defensive buildings to increase the difficulty. 
    - Village: There are multiple buildings in the village.
        - Town Hall: Main building. 4x3 in size. Hitpoints = 100. Only 1 at the center of every village. Yellow in colour.
        - Huts: 5 huts spread around the village. 2x2 in size. Hitpoints = 50. Blue in colour.
        - Walls: Surround both Huts and Town Hall by default. Hitpoints = 30. Red in colour. 
        - Cannon: Defence mechanism of the village. 1x1 in size. 7 in number spread around the village (10 in level 2 and 15 in level 3). Deal a damage of health = 2 per shot. Pink in colour, turn blue while they are engaged with a troop or the king. Hitpoints = 20. Engage with anyone in a 5 tile radius. Cannot attack aerial troops. 
        - Wizard Tower: Similar to cannon. Extra health to balance out the game. Hitpoints = 200. Light blue in colour, turn green when attacking. 2 in level 1, 3 in level 2, 4 in level 3 spread around the village. 1x1 in size.
    - King: The main guy of the invading party. Hitpoints = 100. Deals a damge = 10 health per shot. Initial speed of 1 which can be increased by using spells. Moves up/down/left/right. Space is used to attack. Health bar is displayed at the side of the screen. *Leviathan axe* implemented. Attacks any building in a 5 tile radius.
    - Queen: Added in 2nd part of assignment. Option given at the start of the game to choose either King or Queen. Similar to King. 10 less hitpints than the king. Uses arrows to attack 8 tiles away and in a radius of 5x5. Damage is also less than the King.
    - Barbaians: 3 spawning points, controlled by 3 different buttons. When you press the button, they appear the button and their movements from then on are automated. They move to the closest building from their coordinate (according to Euclidean distance), and when they reach the building they attack. Hitpoints = 20. Deal a damage of 5 health per shot. Can be increased using spells. The colour of the barbarian dims when the less than 50% of the health is remaining.
    - Archers: 3 spawning points, controlled by 3 different buttons. When you press the button, they appear the button and their movements from then on are automated. They move to the closest building from their coordinate (according to Euclidean distance), and when they reach the building they attack. Half the health of barbarian, half the damge and twice the movement speed. Can be increased using spells. 
    - Balloons: Aerial troop. 3 spawning points, controlled by 3 different buttons. When you press the button, they appear the button and their movements from then on are automated. Prioritise attacking the cannons and wizard towers first. Then move on to the other buildings in the village. Can move over other buildings, that is they cannot stop its progress. Twice the damage of the barbarians, same health and twice the movement speed. 
    - Spells: Rage spell increases damage per shot (2 times) and movement speed (2 times) of all alive troops in the game. Can only be used once in the game. Heal spell icreases health (1.5 times) of all alive troops in the game. Can only be used once in the game.
    - Replay: Replays of all the games played are available. Run the replay.py file and choose the game number you want to replay.

+ ### Controls
    - 'w' - move king 1 step up.
    - 'a' - move king 1 step to the left.
    - 's' - move king 1 step down.
    - 'd' - move king 1 step to the right.
    - '[SPACE]' - make the king attack. Sword sound indiactes an attack.
    - 'p' - pause / unpause the game.
    - 'l' - activate 1st barbarian.
    - 'm' - activate 2nd barbarian.
    - 'n' - activate 3rd barbarian.
    - 'u' - activate 1st archer.
    - 'i' - activate 2nd archer.
    - 'o' - activate 3rd archer.
    - 'z' - activate 1st balloon.
    - 'x' - activate 2nd balloon.
    - 'c' - activate 3rd balloon.
    - 'r' - activate rage spell.
    - 'h' - activate heal spell.
    - 'q' - quit the game.

+ ### Rules
 - Win: When all the buildings have been destroyed of all the 3 levels and the King or Queen is alive.
 - Loss: If the King or Queen dies or you quit (q) the game.