import subprocess
import os


def install(package):
    os.system("pip install ursina")


install("ursina")

from ursina import *

app = Ursina()


def input(key):
    if key == "escape":
        sys.exit()


app.run()
app.destroy()
sys.exit()
