import pygame
from pygame._sdl2 import *
from src.settings import *

class Tile(pygame.sprite.Sprite):
    def __init__(self, app, pos, groups, texture) -> None:
        super().__init__(groups)
        self.image: Image = Image(texture.texture)
        self.rect = self.image.get_rect()
        self.rect.topleft = pos

class BG(pygame.sprite.Sprite):
    def __init__(self, app, groups) -> None:
        super().__init__(groups)

        self.image = Image(Texture.from_surface(app.renderer, pygame.transform.scale(pygame.image.load(f"./img/BG.PNG"), (WIDTH + 200, HEIGHT + 200))))
        self.rect = self.image.get_rect()
        self.rect.bottomleft = (0, 1080)

