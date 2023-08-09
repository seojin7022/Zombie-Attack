import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups, obstacle_sprites) -> None:
        super().__init__(groups)
        self.image = pygame.image.load(f"./img/Characters/Dog.PNG").convert_alpha()
        self.rect = self.image.get_bounding_rect()
        self.image = pygame.transform.scale(self.image, (self.rect.width / 3, self.rect.height / 3))
        self.rect = self.image.get_rect()
        self.rect.bottomleft = pos
        self.hitbox = self.rect.inflate(-20, -100)

        self.direction = pygame.math.Vector2()
        self.speed = 5
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
            if self.isFliped:
                self.isFliped = False
                self.image = pygame.transform.flip(self.image, True, False)
        elif keys[pygame.K_a]:
            self.direction.x = -1
            if not self.isFliped:
                self.isFliped = True
                self.image = pygame.transform.flip(self.image, True, False)
        else:
            self.direction.x = 0

    def move(self, speed):
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()



        self.hitbox.x += self.direction.x * speed
        self.collision('horizontal')
        # self.hitbox.y += self.direction.y * speed
        # self.collision('vertical')
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