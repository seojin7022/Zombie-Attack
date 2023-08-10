import pygame
from pygame._sdl2.video import *
from src.settings import *

class Tile(pygame.sprite.Sprite):
    def __init__(self, app, pos, groups, name="Tile1") -> None:
        super().__init__(groups)
        self.name = name
        self.image = Image(Texture.from_surface(app.renderer, pygame.transform.scale(pygame.image.load(f"./img/Tile/{name}.png"), (TILESIZE, TILESIZE))))
        self.rect = self.image.get_rect()
        self.rect.topleft = pos
        self.hitbox = self.rect.inflate(-20, -10)

class BG(pygame.sprite.Sprite):
    def __init__(self, app, groups) -> None:
        super().__init__(groups)

        self.image = Image(Texture.from_surface(app.renderer, pygame.transform.scale(pygame.image.load(f"./img/BG.PNG"), (WIDTH + 200, HEIGHT + 200))))
        self.rect = self.image.get_rect()
        self.rect.bottomleft = (0, 1080)

