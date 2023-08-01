import pygame, initGame

window_size = (1200, 675)

screen = pygame.display.set_mode(window_size)

isRunning = True

while isRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            isRunning = False
