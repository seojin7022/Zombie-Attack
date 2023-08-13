import pygame
from pygame._sdl2 import *
from src.settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self, app, pos, groups, obstacle_sprites) -> None:
        super().__init__(groups)
        self.image = Image(Texture.from_surface(app.renderer, pygame.transform.scale(pygame.image.load(f"./img/Characters/Dog.PNG"), (TILESIZE, TILESIZE))))
        self.rect = self.image.get_rect()
        self.rect.bottomright = pos
        self.hitbox = self.rect.inflate(0, 0)

        self.direction = pygame.math.Vector2()
        self.speed = 3
        self.isFliped = False

        self.obstacle_sprites = obstacle_sprites

    def input(self):
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_w]:
            self.direction.y = -1
        elif keys[pygame.K_s]:
            self.direction.y = 1
        else:
            self.direction.y = 0

        if keys[pygame.K_d]:
            self.direction.x = 1
            
            if self.image.flip_x:
                self.image.flip_x = False
                
        elif keys[pygame.K_a]:
            self.direction.x = -1
            if not self.image.flip_x:
                self.image.flip_x = True
        else:
            self.direction.x = 0

    def move(self, speed):
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()



        self.hitbox.x += self.direction.x * speed
        self.collision('horizontal')
        self.hitbox.y += self.direction.y * speed
        self.collision('vertical')
        self.rect.center = self.hitbox.center
        

    def collision(self, direction):
        if direction == 'horizontal':
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.x > 0:
                        self.hitbox.right = sprite.hitbox.left
                    elif self.direction.x < 0:
                        self.hitbox.left = sprite.hitbox.right
        if direction == 'vertical':
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.y > 0:
                        self.hitbox.bottom = sprite.hitbox.top
                    elif self.direction.y < 0:
                        self.hitbox.top = sprite.hitbox.bottom

    
    def update(self):
        self.input()
        self.move(self.speed)