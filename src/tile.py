import pygame
from pygame._sdl2 import *
from src.settings import *



class Tile(pygame.sprite.Sprite):
    def __init__(self, app, pos, groups, texture, newRect=pygame.Rect(0, 0, TILESIZE, TILESIZE)) -> None:
        super().__init__(groups)
        self.image: Image = Image(texture.texture)
        self.image.srcrect.width = newRect.width
        self.image.srcrect.height = newRect.height
        self.image.srcrect.top = texture.srcrect.top
        
        # self.image.srcrect = 
        self.rect = self.image.get_rect()
        self.rect.topleft = pos
        self.hitbox = self.rect.inflate(0, 0)
        self.hitbox = self.rect.fit(self.rect)

class BG(pygame.sprite.Sprite):
    def __init__(self, app, groups) -> None:
        super().__init__(groups)

        self.image = Image(Texture.from_surface(app.renderer, pygame.transform.scale(pygame.image.load(f"./img/BG.PNG"), (WIDTH + 200, HEIGHT + 200))))
        self.rect = self.image.get_rect()
        self.rect.bottomleft = (0, 1080)

