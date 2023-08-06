import pygame
from src import guiManager

pygame.init()


def GameOver(screen: pygame.Surface):
    isRivived = False
    isExited = False
    GameOverBackgroundImage = pygame.image.load(
        f"./img/GUIs/GameOverBackground.PNG"
    ).convert_alpha()
    GameOverBackgroundImage.set_colorkey((0, 0, 0))
    GameOverGui = guiManager.GUI((GameOverBackgroundImage.get_size()))

    ReviveButton = guiManager.Button("ReviveButton")
    ExitButton = guiManager.Button("ExitButton")
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return False

            if event.type == pygame.MOUSEMOTION:
                ReviveButton.Hover(event.pos)
                ExitButton.Hover(event.pos)

            if event.type == pygame.MOUSEBUTTONDOWN:
                isRivived = ReviveButton.Click(event.pos)
                isExited = ExitButton.Click(event.pos)

        if isRivived:
            print("SS")
            return True
        elif isExited:
            return False
        GameOverGui.blit(GameOverBackgroundImage, (0, 0))
        GameOverGui.blit(ReviveButton, (0, 0))
        GameOverGui.blit(ExitButton, (0, 0))
        screen.blit(GameOverGui, (0, 0))
        pygame.display.flip()
