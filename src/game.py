import pygame, random
from src import gameMath, gameOver
from src.characterManager import *
from src.guiManager import GUI, Button, Text

pygame.init()


def createMap():
    return pygame.image.load(f"./img/Tile1.png")




Maps = [((i - 1) * 100, (j - 1) * 100) for i in range(15) for j in range(10)]
MapsImage = [(createMap(), Maps[i]) for i in range(150)]

Map = pygame.Surface((1200, 675))
Map.blits(MapsImage)

WDown = False
SDown = False
ADown = False
DDown = False



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

COINTEXT=2


def Game(screen, data):
    global player_pos, WDown, SDown, ADown, DDown
    zombies = []
    GUIs = []
    player_pos = (0, 0)
    player = Character("Player", (500, 200))
    player.data = data
    Sword = Weapon("Sword")
    Sword.pos = (15, 40)
    player.Equip(Sword)

    TopBar = GUI(screen.get_size())
    GUIs.append(TopBar)
    #Gray Color Bar
    TopGrayBar = GUI((TopBar.get_width(), 70))
    TopGrayBar.fill((104, 104, 104))

    #Coin And Crystal Values
    Value = GUI(TopBar.get_size())
    Value.blit(pygame.image.load(f"./img/GUIs/Value.PNG").convert_alpha(), (0, 0))

    #Coin Text
    CoinText = Text((TopBar.get_width(), TopGrayBar.get_height()),str(player.data["Coin"]), (220, 170, 79), fontSize=40 )
    CoinText.pos = (120, CoinText.get_height() / 4)

    #Setting Button
    SettingButton = Button("SettingButton")

    #MenuButton
    MenuButton = Button("MenuButton")
    

    #Add Elements to TopBar
    TopBar.add(TopGrayBar, 0)
    TopBar.add(Value, 1)
    TopBar.add(CoinText, COINTEXT)
    TopBar.add(SettingButton, 3)
    
    # GUIs.append(MenuButton)

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
            screen.blit(v.image, (player.pos[0] + v.pos[0], player.pos[1] + v.pos[1]))
            if type(v) == Weapon:
                isMouseClicked, damage = v.NormalAttack()

                if isMouseClicked:
                    for i in zombies:
                        if gameMath.GetDistance(player_pos, i.pos) <= v.data["Range"]:
                            isDead = i.Damage(damage)

                            if isDead:
                                i.Reward(player)
                                GUIs[0].children[COINTEXT].text = str(player.data["Coin"])
                                zombies.remove(i)

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
        for i in GUIs:
            # i.update()
            screen.blit(i, (0, 0))

        if player.hp <= 0:
            if gameOver.GameOver(screen):
                Game(screen, data)
                return False
            else:
                return False

        pygame.display.flip()

