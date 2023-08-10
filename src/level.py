import pygame
from pygame._sdl2.video import *
from src.settings import *
from src.tile import Tile, BG
from src.player import Player
from src.debug import debug

class Level:
    def __init__(self, app) -> None:
        
        self.app = app
        self.window = app.window
        self.renderer = app.renderer

        self.visible_sprites = YSortCameraGroup(app)
        self.obstacles_sprites = pygame.sprite.Group()

        self.create_map()

    def create_map(self):
        BG(self.app, self.visible_sprites)
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

    def custom_draw(self, player):
        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height

        for sprite in self.sprites():
            # sprite.rect.topleft -= self.offset
            self.renderer.blit(sprite.image, sprite.rect)