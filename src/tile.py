import pygame
from src.settings import *

class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, groups, name="Tile1") -> None:
        super().__init__(groups)
        self.name = name
        self.image = pygame.transform.scale(pygame.image.load(f"./img/Tile/{name}.png").convert_alpha(), (TILESIZE, TILESIZE))
        self.rect = self.image.get_bounding_rect()
        self.rect.topleft = pos
        self.hitbox = self.rect.inflate(0, -10)

class BG(pygame.sprite.Sprite):
    def __init__(self, groups) -> None:
        super().__init__(groups)

        self.image = pygame.transform.scale(pygame.image.load(f"./img/BG.PNG").convert(), (WIDTH + 200, HEIGHT + 200))
        self.rect = self.image.get_rect()
        self.rect.bottomleft = (0, 1080)

