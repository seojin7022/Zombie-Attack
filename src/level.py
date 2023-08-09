from typing import Iterable, Union
import pygame
from pygame.sprite import AbstractGroup
from src.settings import *
from src.tile import Tile, BG
from src.player import Player
from src.debug import debug

class Level:
    def __init__(self) -> None:

        self.display_surface = pygame.display.get_surface()

        self.visible_sprites = YSortCameraGroup()
        self.obstacles_sprites = pygame.sprite.Group()

        self.create_map()

    def create_map(self):
        BG(self.visible_sprites)
        with open(f"./data/MapData.txt", "r") as Map:
            
            MapData = Map.readlines()

            for i in range(len(MapData)):
                for j in range(len(MapData[i])):
                    x = j * TILESIZE
                    y = i * TILESIZE

                    if MapData[i][j] == "1":
                        Tile((x, y), [self.visible_sprites, self.obstacles_sprites], name="Box")

                    elif MapData[i][j] == "p":
                        self.player = Player((x, y), [self.visible_sprites], self.obstacles_sprites)

    def run(self):
        self.visible_sprites.custom_draw(self.player)
        self.visible_sprites.update()
        debug(self.player.direction)

class YSortCameraGroup(pygame.sprite.Group):
    def __init__(self) -> None:
        super().__init__()

        self.display_surface = pygame.display.get_surface()
        self.half_width = self.display_surface.get_size()[0] // 2
        self.half_height = self.display_surface.get_size()[1] // 2
        self.offset = pygame.math.Vector2()

    def custom_draw(self, player):
        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height

        for sprite in self.sprites():
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image, offset_pos)