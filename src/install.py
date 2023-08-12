import os

with open(f"./requirements.txt", 'r') as requirements:
    for requirement in requirements.readlines():
       os.system(f"pip install {requirement}") 