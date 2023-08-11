import pygame
from pygame._sdl2.video import *
pygame.init()
font = pygame.font.Font(None, 30)

def debug(info, y = 10, x = 10):
    
    display_surface = pygame.display.get_surface()
    debug_surf = font.render(str(info), True, 'White')
    debug_rect = debug_surf.get_rect(topleft=(x, y))
    renderer.blit(Texture.from_surface(renderer, debug_surf), debug_rect)
    display_surface.blit(debug_surf, debug_rect)