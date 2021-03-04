import os
from pathlib import Path, PureWindowsPath

dirpath = "C:\\Users\\{}\\AppData\\Local\\Packages\\Microsoft.MinecraftUWP_8wekyb3d8bbwe\\LocalState\\logs".format(os.getlogin())

paths = sorted(Path(dirpath).iterdir(), key=os.path.getmtime)
paths.reverse()

for path in paths:
    if "ContentLog" in os.path.basename(path):
        with open(path, 'r') as content_log:
            coord = ""
            for line in content_log.readlines():
                if "[Molang][inform]-1.111" in line:
                    print(coord)
                    coord = ""
                elif("[Molang][inform]-" in line):
                    coord = coord + str(float(line.strip().split("-", 1)[1])) + " "
            print(coord)
            break
