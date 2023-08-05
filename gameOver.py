import pygame, guiManager

pygame.init()


def GameOver(screen: pygame.Surface):
    GameOverBackgroundImage = pygame.image.load(
        f"./img/GUIs/GameOverBackground.PNG"
    ).convert_alpha()
    GameOverGui = guiManager.GUI((GameOverBackgroundImage.get_size()))
    ReviveButton = guiManager.Button("ReviveButton")
    ExitButton = guiManager.Button("ExitButton")
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

            if event.type == pygame.MOUSEMOTION:
                ReviveButton.Hover(event.pos)
                ExitButton.Hover(event.pos)
        GameOverGui.blit(GameOverBackgroundImage, (0, 0))
        GameOverGui.blit(ReviveButton, (0, 0))
        GameOverGui.blit(ExitButton, (0, 0))
        screen.blit(GameOverGui, (0, 0))
        pygame.display.flip()
