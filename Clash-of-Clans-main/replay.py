import time
from os.path import exists
from src.constants import *

render_time = time.time()
print("Total games played: ", len(os.listdir('replays/')))

dir = str(input("Which game do you want to replay?\n"))
path_exists1 = exists("replays/" + dir)

if not path_exists1:
    print("game does not exist!")
else:
    # rendering the replay
    path = 'replays/'+dir
    files = len(os.listdir(path))
    for i in range(1, files):
        name = str(i)
        path_exists = exists(path + "/" + name)
        if path_exists:
            f = open(path + "/" + name, "r")
            content = f.read()
            print(content)
            time.sleep(0.07)
            f.close()
    print("THE END!")