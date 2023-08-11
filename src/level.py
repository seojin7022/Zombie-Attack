import pygame
from pygame._sdl2.video import *
from src.settings import *
from src.tile import Tile, BG
from src.player import Player
from src.debug import debug

floor = pygame.Surface((TILESIZE * 50, TILESIZE * 50))

for i in range(-25, 25):
    for j in range(-25, 25):
        floor.blit(pygame.image.load(f"./img/Tile/PurpleTile.png"), (j * TILESIZE, i * TILESIZE))

class Level:
    def __init__(self, app) -> None:
        
        self.app = app
        self.window = app.window
        self.renderer = app.renderer

        self.visible_sprites = YSortCameraGroup(app)
        self.obstacles_sprites = pygame.sprite.Group()

        self.create_map()

    def create_map(self):
        with open(f"./data/MapData.txt", "r") as Map:
            
            MapData = Map.readlines()

            for i in range(len(MapData)):
                for j in range(len(MapData[i])):
                    x = j * TILESIZE
                    y = i * TILESIZE

                    if MapData[i][j] == "1":
                        Tile(self.app, (x, y), [self.visible_sprites, self.obstacles_sprites], name="Box")

                    elif MapData[i][j] == "p":
                        self.player = Player(self.app, (x, y), [self.visible_sprites], self.obstacles_sprites)

    def run(self):
        self.visible_sprites.custom_draw(self.player)
        self.visible_sprites.update()

class YSortCameraGroup(pygame.sprite.Group):
    def __init__(self, app) -> None:
        super().__init__()
        
        self.window = app.window
        self.renderer = app.renderer
        self.half_width = self.window.size[0] // 2
        self.half_height = self.window.size[1] // 2
        self.offset = pygame.math.Vector2()

        self.floor_Image = Image(Texture.from_surface(self.renderer, floor))
        self.floor_rect = self.floor_Image.get_rect()
        self.floor_rect.topleft = (0 ,0)

    def custom_draw(self, player):
        self.offset.x = player.rect.left - self.half_width
        self.offset.y = player.rect.top - self.half_height
        print(self.floor_rect.topleft)
        offset = self.floor_rect.topleft -self.offset
        rect = self.floor_rect.copy()
        rect.topleft = offset
        # print(self.floor_rect.topleft)
        self.renderer.blit(self.floor_Image, rect)

        for sprite in self.sprites():
            offset = sprite.rect.topleft -self.offset
            rect = sprite.rect.copy()
            rect.topleft = offset
            self.renderer.blit(sprite.image, rect)