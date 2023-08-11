import pygame, sys
from pygame._sdl2.video import Renderer, Image, Texture, Window
from src.settings import *
from src.level import Level
pygame.init()
class Game:
    def __init__(self):
        self.window = Window(size=(WIDTH, HEIGHT))
        self.window.maximize()
        
        self.renderer = Renderer(self.window)
        self.renderer.draw_color = (0, 0, 0, 255)
        # self.screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.DOUBLEBUF | pygame.FULLSCREEN)
        pygame.display.set_caption("Zombie Attack")
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

