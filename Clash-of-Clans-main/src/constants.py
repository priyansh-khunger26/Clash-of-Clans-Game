import os
from colorama import init, Fore, Back, Style

init()

# setting constants needed for the game
dims = os.get_terminal_size()
s_height = dims[1]
s_width = dims[0]
game_ht = (0, int(s_height / 1.1))  # height range of game in total screen
# width range of game in total screen
game_wd = (int(s_width / 5), int(s_width - int(s_width / 4)))
frametransition = 0.07
levels = 3

# on completion of the game
def over(buildings, x, result):
    os.system("clear")
    print(
        Fore.CYAN
        + Style.BRIGHT
        + "\t\t\t####    ####   ##   ##  ######           ####   ##  ##  ######  ######         "
        + Style.RESET_ALL
    )
    print(
        Fore.CYAN
        + Style.BRIGHT
        + "\t\t\t#      ##  ##  ### ###  ##              ##  ##  ##  ##  ##      ##  ##         "
        + Style.RESET_ALL
    )
    print(
        Fore.CYAN
        + Style.BRIGHT
        + "\t\t\t# ###  ######  ## # ##  ####            ##  ##  ##  ##  ####    #####          "
        + Style.RESET_ALL
    )
    print(
        Fore.CYAN
        + Style.BRIGHT
        + "\t\t\t#  ##  ##  ##  ##   ##  ##              ##  ##   ####   ##      ##  ##         "
        + Style.RESET_ALL
    )
    print(
        Fore.CYAN
        + Style.BRIGHT
        + "\t\t\t####   ##  ##  ##   ##  ######           ####     ##    ######  ##  ##         "
        + Style.RESET_ALL
    )

    if result:
        print(
            Fore.CYAN
            + Style.BRIGHT
            + str("\n\t\t\t\t\t\t\tGAME RESULT: WON\n")
            + Style.RESET_ALL
        )
        # os.system("aplay -q ./sounds/victory.wav &")
    else:
        print(
            Fore.CYAN
            + Style.BRIGHT
            + str("\n\t\t\t\t\t\t\tGAME RESULT: LOST\n")
            + Style.RESET_ALL
        )
    # print(x)
        # os.system("aplay -q ./sounds/victory.wav &")
    quit()
