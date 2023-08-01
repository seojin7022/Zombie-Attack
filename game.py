import pygame


def Game(screen, data):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return False

        screen.fill((0, 0, 0))
        pygame.display.flip()
