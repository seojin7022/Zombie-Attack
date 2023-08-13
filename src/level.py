import pygame
from pygame._sdl2 import *
from src.settings import *
from src.tile import Tile, BG
from src.player import Player
from src.debug import debug
from pytmx.util_pygame_sdl2 import load_pygame_sdl2, PygameSDL2Tile


class Level:
    def __init__(self, app) -> None:
        
        self.app = app
        self.window = app.window
        self.renderer = app.renderer

        
        

        self.visible_sprites = YSortCameraGroup(app)
        self.obstacles_sprites = pygame.sprite.Group()

        self.create_map()

    def create_map(self):
        self.tmx_data = load_pygame_sdl2(self.renderer, f"./map/map.tmx")


        for layer in self.tmx_data.layers:
            if hasattr(layer, "data"):
                for x, y, surf in layer.tiles():
                    if layer.name == "Floor":
                        Tile(self.app, (x * TILESIZE, y * TILESIZE), [self.visible_sprites], surf)
                    if layer.name == "Box":
                        gid = self.tmx_data.get_tile_gid(x, y, self.tmx_data.layers.index(layer))
                        newRect = pygame.Rect(0, 0, 0, 0)
                        for id, collider_group in self.tmx_data.get_tile_colliders():
                            if id == gid:
                                newRect.width = collider_group[0].width
                                newRect.height = collider_group[0].height
                                print(collider_group[0].height)
                        
                        Tile(self.app, (x * TILESIZE, y * TILESIZE), [self.visible_sprites, self.obstacles_sprites], surf, newRect)

                

        for obj in self.tmx_data.objects:
            if obj.name == "Player":
                self.player = Player(self.app, (obj.x, obj.y), [self.visible_sprites], self.obstacles_sprites)

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
        self.offset.x = player.rect.centerx - self.half_width / self.renderer.scale[0]
        self.offset.y = player.rect.centery - self.half_height / self.renderer.scale[1]

        

        for sprite in self.sprites():
            offset = sprite.rect.center -self.offset
            
            rect = sprite.rect.copy()
            rect.center = offset
            self.renderer.blit(sprite.image, rect)