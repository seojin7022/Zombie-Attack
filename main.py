import src.install

import pygame, sys
from pygame._sdl2 import Renderer, Image, Texture, Window
from src.settings import *
from src.level import Level
pygame.init()
class Game:
    def __init__(self):
        self.window = Window(size=(WIDTH, HEIGHT))
        self.window.maximize()
        self.window.title = "Magical Library"
        
        self.renderer = Renderer(self.window)
        self.renderer.scale = (3,3)
        self.renderer.draw_color = (0, 0, 0, 255)
        self.clock = pygame.time.Clock()

        self.level = Level(self)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            self.renderer.clear()
            self.level.run()
            self.renderer.present()
            self.clock.tick(FPS)


if __name__ == "__main__":
    game = Game()
    game.run()

