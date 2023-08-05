import pygame, gameMath, gameOver, random
from characterManager import Character, Zombie, Equipment
from guiManager import GUI, Button

pygame.init()


def createMap():
    return pygame.image.load(f"./img/Tile1.png")


player_pos = (0, 0)

Maps = [((i - 1) * 100, (j - 1) * 100) for i in range(15) for j in range(10)]
MapsImage = [(createMap(), Maps[i]) for i in range(150)]

Map = pygame.Surface((1200, 675))
Map.blits(MapsImage)

WDown = False
SDown = False
ADown = False
DDown = False

zombies = []

spawnPoints = [
    (-700, -500),
    (-700, 0),
    (-700, 500),
    (700, -500),
    (700, 0),
    (700, 500),
    (0, -500),
    (0, 0),
    (0, 500),
]


def Game(screen, data):
    global player_pos, WDown, SDown, ADown, DDown
    player = Character("Player", (500, 200))
    player.data = data

    pygame.time.set_timer(
        pygame.USEREVENT + 1,
        1000,
    )
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

            if event.type == pygame.USEREVENT + 1:
                if len(zombies) < 30:
                    zombies.append(Zombie("WeakZombie", random.choice(spawnPoints)))

                pygame.time.set_timer(pygame.USEREVENT + 1, 500)

        if WDown:
            player_pos = (player_pos[0], player_pos[1] + 5)
            player.direction = "Back"
        if SDown:
            player_pos = (player_pos[0], player_pos[1] - 5)
            player.direction = "Front"
        if ADown:
            player_pos = (player_pos[0] + 5, player_pos[1])
            player.direction = "Left"
        if DDown:
            player_pos = (player_pos[0] - 5, player_pos[1])
            player.direction = "Right"

        if WDown or SDown or ADown or DDown:
            player.currentState = "Idle"  # 추후에 Walk 이미지로 교체
        else:
            player.currentState = "Idle"

        screen.fill((0, 0, 0))
        for i in range(3):
            screen.blit(
                Map, (player_pos[0] % 1200 - (1200 * i), player_pos[1] % 675 - 675)
            )
            screen.blit(
                Map, (player_pos[0] % 1200 - (1200 * i), player_pos[1] % 675 + 675)
            )
            screen.blit(Map, (player_pos[0] % 1200 - (1200 * i), player_pos[1] % 675))

        for v in zombies:
            if (
                gameMath.GetDistance(v.pos, (player_pos[0], player_pos[1]))
                <= v.data["Range"]
            ):
                v.currentState = "Walk"  # 나중에 Attack 으로 수정

                if (
                    pygame.time.get_ticks() - v.attackCooldown
                    >= v.data["AttackCooldown"]
                ):
                    v.attackCooldown = pygame.time.get_ticks()
                    player.Damage(v.data["Attack"])
                    print(player.hp)
            else:
                v.pos = gameMath.GetPositionWithDistance(
                    v.pos, (player_pos[0], player_pos[1]), v.data["Speed"]
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

        for v in zombies:
            v.Guis.update()
            screen.blit(
                v.Guis,
                (
                    500 + player_pos[0] - v.pos[0],
                    200 + player_pos[1] - v.pos[1],
                ),
            )
        player.Guis.update()
        screen.blit(player.Guis, (player.pos))

        if player.hp <= 0:
            gameOver.GameOver(screen)

        pygame.display.flip()
