import pygame
from pygame._sdl2 import *
from src.scene import Scene
from src.settings import *

class Lobby(Scene):
    def __init__(self, app) -> None:
        super().__init__()

        self.app = app
        
        self.lobby_img = pygame.transform.scale(pygame.image.load(f"./img/Lobby.png"), (WIDTH / self.app.renderer.scale[0], HEIGHT / self.app.renderer.scale[1]))

    def LoadScene(self):
        pass

    def run(self, renderer):
        renderer.blit(Texture.from_surface(renderer, self.lobby_img), self.lobby_img.get_rect())
