import pygame
from pygame._sdl2 import *
from src.settings import *


from src.debug import debug

from src.lobby import Lobby
import cv2

class Level:
    def __init__(self, app) -> None:
        
        self.app = app
        self.window = app.window
        self.renderer = app.renderer

        self.current_scene = Lobby(app)
        

    def run(self):
        
        self.current_scene.run(self.renderer)

