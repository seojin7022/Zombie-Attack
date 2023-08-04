import pygame, gameMath
from characterManager import Character, Zombie, Equipment


def createMap():
    return pygame.image.load(f"./img/Tile1.png")


player_pos = (0, 0)

Maps = [((i - 1) * 100, (j - 1) * 100) for i in range(15) for j in range(10)]
MapsImage = [createMap() for i in range(150)]

WDown = False
SDown = False
ADown = False
DDown = False

zombies = []


def Game(screen, data):
    global player_pos, WDown, SDown, ADown, DDown
    zombies.append(Zombie("WeakZombie", (0, 300)))
    player = Character("WeakZombie", (500, 200), currentState="Walk")
    player.equipments.append(Equipment("Sword"))
    while True:
        pygame.time.Clock().tick(120)
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

        if WDown or SDown or ADown or DDown:
            player.NextFrame()
        else:
            player.StopAnimation()

        screen.fill((0, 0, 0))
        for i in range(len(Maps)):
            screen.blit(
                MapsImage[i],
                (
                    Maps[i][0]
                    + min(max(player_pos[0], -1), 1) * (abs(player_pos[0]) % 100),
                    Maps[i][1]
                    + min(max(player_pos[1], -1), 1) * (abs(player_pos[1]) % 100),
                ),
            )

        for v in zombies:
            v.pos = gameMath.GetPositionWithDistance(
                v.pos, (player_pos[0], player_pos[1]), 2
            )
            screen.blit(
                v.PlayAnimation(),
                (
                    500 + player_pos[0] - v.pos[0],
                    200 + player_pos[1] - v.pos[1],
                ),
            )
        screen.blit(player.PlayAnimation(), player.pos)
        for v in player.equipments:
            screen.blit(v.image, player.pos)
        pygame.display.flip()
