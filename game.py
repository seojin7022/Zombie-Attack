import pygame


def createMap():
    return pygame.image.load(f"./img/Map.png")


player_pos = (0, 0)

Maps = [((i - 1) * 1200, (j - 1) * 675) for i in range(0, 3) for j in range(0, 3)]

WDown = False
SDown = False
ADown = False
DDown = False


def Game(screen, data):
    global player_pos, WDown, SDown, ADown, DDown
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    WDown = True

                elif event.key == pygame.K_s:
                    SDown = True

                if event.key == pygame.K_a:
                    ADown = True

                elif event.key == pygame.K_d:
                    DDown = True

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    WDown = False

                elif event.key == pygame.K_s:
                    SDown = False

                if event.key == pygame.K_a:
                    ADown = False

                elif event.key == pygame.K_d:
                    DDown = False

        if WDown:
            player_pos = (player_pos[0], player_pos[1] + 5)
        if SDown:
            player_pos = (player_pos[0], player_pos[1] - 5)
        if ADown:
            player_pos = (player_pos[0] + 5, player_pos[1])
        if DDown:
            player_pos = (player_pos[0] - 5, player_pos[1])

        screen.fill((0, 0, 0))
        for i in range(len(Maps)):
            screen.blit(
                createMap(),
                (
                    Maps[i][0]
                    + min(max(player_pos[0], -1), 1) * (abs(player_pos[0]) % 1200),
                    Maps[i][1]
                    + min(max(player_pos[1], -1), 1) * (abs(player_pos[1]) % 675),
                ),
            )
        pygame.display.flip()
