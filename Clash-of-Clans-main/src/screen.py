from src.constants import *
from colorama import init, Fore, Back, Style

init()

# screen class
class Screen:
    def __init__(this, rows, cols):
        this.cols = cols
        this.rows = rows
        this.screen = []

        for i in range(this.rows):
            this.screen.append([])
            for j in range(this.cols):
                this.screen[i].append(" ")

    def ret_rows(this):
        return this.rows

    def ret_cols(this):
        return this.cols

    # display function plus writing to files for replay
    def display(this, iter, dir):
        name = str(iter)
        dir = str(dir)
        f = open("replays/" + dir + "/" + name, "w")
        for i in range(this.rows):
            for j in range(this.cols):
                tobeprinted = this.screen[i][j]
                if tobeprinted == 1:
                    print(Back.YELLOW + " " + Style.RESET_ALL, end="")
                    f.write(str(Back.YELLOW + " " + Style.RESET_ALL))
                elif tobeprinted == 2:
                    print(Back.BLUE + " " + Style.RESET_ALL, end="")
                    f.write(str(Back.BLUE + " " + Style.RESET_ALL))
                elif tobeprinted == 3:
                    print(Back.MAGENTA + " " + Style.RESET_ALL, end="")
                    f.write(str(Back.MAGENTA + " " + Style.RESET_ALL))
                elif tobeprinted == 4:
                    print(Back.RED + " " + Style.RESET_ALL, end="")
                    f.write(str(Back.RED + " " + Style.RESET_ALL))
                elif tobeprinted == 5:
                    print(Back.GREEN + " " + Style.RESET_ALL, end="")
                    f.write(str(Back.GREEN + " " + Style.RESET_ALL))
                elif tobeprinted == 6:
                    print(Back.LIGHTBLUE_EX + " " + Style.RESET_ALL, end="")
                    f.write(str(Back.LIGHTBLUE_EX + " " + Style.RESET_ALL))
                elif tobeprinted == 7:
                    print(Back.GREEN + " " + Style.RESET_ALL, end="")
                    f.write(str(Back.GREEN + " " + Style.RESET_ALL))
                elif tobeprinted == "B":
                    print(
                        Fore.CYAN + Style.BRIGHT + tobeprinted + Style.RESET_ALL, end=""
                    )
                    f.write(
                        str(Fore.CYAN + Style.BRIGHT + tobeprinted + Style.RESET_ALL)
                    )
                elif tobeprinted == "D":
                    print(Fore.CYAN + Style.DIM + "B" + Style.RESET_ALL, end="")
                    f.write(str(Fore.CYAN + Style.DIM + tobeprinted + Style.RESET_ALL))
                else:
                    print(tobeprinted, end="")
                    f.write(str(tobeprinted))
        f.close()


class Level:
    def __init__(this):
        this.__value = 1

    def ret_level(this):
        return this.__value

    def upd_level(this, x):
        this.__value = x
