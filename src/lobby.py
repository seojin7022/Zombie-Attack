import pygame, json

from src import initGame, game
pygame.init()

window_size = (1200, 675)

screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Zombie Attack")

GameLobby_bg = pygame.image.load(f"./img/GameLobby.png")
StartButton = pygame.image.load(f"./img/StartButton.png").convert_alpha()
OptionButton = pygame.image.load(f"./img/OptionButton.png")

isRunning = True


while isRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            isRunning = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if StartButton.get_bounding_rect().collidepoint(event.pos):
                isRunning = game.Game(screen, initGame.data["PlayerData"])
                break

    if not isRunning:
        break

    screen.fill((0, 0, 0))
    screen.blit(GameLobby_bg, (0, 0))
    screen.blit(StartButton, (0, 0))
    screen.blit(OptionButton, (0, 0))
    pygame.display.flip()

with open(f"./data/player-data.txt", "w") as playerData:
    playerData.write(json.dumps(initGame.data))
