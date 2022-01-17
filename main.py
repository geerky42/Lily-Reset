from msilib.schema import Error
import os
import psutil
import yaml

PATH_INFO_FILE = "path_info.yml"
PROGRAM_NAME = "Game.exe"
SAVE_PATH = "www\\save\\"
CONFIG_NAME = "config.rpgsave"

def reset():
    os.chdir(PATH)

    if not os.path.exists(SAVE_PATH):
        os.makedirs('www\\save')

    for proc in psutil.process_iter():
        # check whether the process name matches
        if proc.name() == PROGRAM_NAME:
            proc.kill()

    for filename in os.listdir(SAVE_PATH):
        if filename == CONFIG_NAME:
            continue
        os.remove(SAVE_PATH + filename)

    os.startfile(PROGRAM_NAME)

if __name__ == "__main__":
    with open(PATH_INFO_FILE) as cr:
        config_vals = yaml.safe_load(cr)

    global PATH
    PATH = config_vals['PATH']

    if not PATH:
        raise Error("Missing Path Info")

    reset()
