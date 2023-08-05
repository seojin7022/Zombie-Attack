import pygame, os, gameData
from guiManager import GUI, Button

tick = 50


class Sprite:
    def __init__(self, name) -> None:
        self.name = name
        self.animation = {}


class Character(Sprite):
    def __init__(self, name, pos=(0, 0), currentState="Idle"):
        super().__init__(name)
        self.name = name
        self.animation = self.LoadImage()
        self.animationNum = 0
        self.currentState = currentState
        self.pos = pos
        self.equipments = []
        self.tick = 0
        self.direction = "Front"
        self.hp = 100
        self.Guis = GUI(list(self.animation.values())[0][0].get_size())
        self.data = {}

        self.HPBar = GUI((self.Guis.get_width(), 15))
        self.HPBar.fill((0, 255, 0))

        self.Guis.add(self.HPBar, 0)

    def LoadImage(self) -> dict:
        animation = {}
        for i in os.listdir(f"./img/Characters/{self.name}"):
            animationName = i.split(".")[0].rstrip(i.split(".")[0][-1])

            if animation.get(animationName) == None:
                animation.update(
                    {
                        animationName: [
                            pygame.image.load(f"./img/Characters/{self.name}/{i}", i).convert_alpha()
                        ]
                    }
                )

            else:
                animation[animationName].append(
                    pygame.image.load(f"./img/Characters/{self.name}/{i}", i).convert_alpha()
                )
            # animation[i.split(".")[0].rstrip(i.split(".")[0][-1])].append(
            #     pygame.image.load(f"./img/Characters/{self.name}/{i}", i)
            # )

        return animation

    def Idle(self):
        newAnimation = self.animation.get(self.direction + self.currentState)
        self.NextFrame()
        return newAnimation[self.animationNum]

    def Walk(self):
        newAnimation = self.animation.get(self.direction + self.currentState)
        self.NextFrame()
        return newAnimation[self.animationNum]

    def PlayAnimation(self):
        self.tick = self.tick + 1 if self.tick < tick else 0
        if self.currentState == "Idle":
            return self.Idle()
        elif self.currentState == "Walk":
            return self.Walk()

    def StopAnimation(self):
        self.tick = 0
        self.animationNum = 0

    def NextFrame(self):
        newAnimation = self.animation[self.direction + self.currentState]
        self.animationNum = min(
            self.tick // (tick // (len(newAnimation))),
            (len(newAnimation) - 1),
        )

    def Damage(self, dmg):
        if self.hp - dmg > 0:
            self.hp -= dmg
            self.HPBar = GUI(
                (
                    (self.hp / self.data["Hp"]) * (self.HPBar.get_width()),
                    self.HPBar.get_height(),
                )
            )
            self.HPBar.fill((0, 255, 0))

            self.Guis.add(self.HPBar, 0)
        else:
            self.hp = 0


class Zombie(Character):
    def __init__(self, name, pos=(0, 0), currentState="Walk"):
        super().__init__(name, pos, currentState)
        self.data = gameData.zombies[name]
        self.attackCooldown = pygame.time.get_ticks()

    def Walk(self):
        newAnimation = self.animation[self.direction + self.currentState]
        self.NextFrame()
        return newAnimation[self.animationNum]


class Equipment:
    def __init__(self, name) -> None:
        self.image = pygame.image.load(f"./img/{name}.PNG")
        self.pos = (0, 0)
