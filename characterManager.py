import pygame, os

tick = 50


class Character:
    def __init__(self, name, pos=(0, 0), currentState="Idle"):
        self.name = name
        self.animation = self.LoadImage()
        self.animationNum = 0
        self.currentState = currentState
        self.pos = pos
        self.equipments = []
        self.tick = 0

    def LoadImage(self) -> dict:
        animation = {"Idle": [], "Walk": [], "Attack": []}
        for i in os.listdir(f"./img/Characters/{self.name}"):
            animation[i.split(".")[0].rstrip(i.split(".")[0][-1])].append(
                pygame.image.load(f"./img/Characters/{self.name}/{i}", i)
            )

        return animation

    def Idle(self):
        if self.animationNum + 1 > len(self.animation["Idle"]):
            self.animationNum = -1
        self.animationNum += 1
        return self.animation["Idle"][self.animationNum]

    def Walk(self):
        return self.animation["Walk"][self.animationNum]

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
        self.animationNum = min(
            self.tick // (tick // (len(self.animation[self.currentState]))),
            (len(self.animation[self.currentState]) - 1),
        )


class Zombie(Character):
    def __init__(self, name, pos=(0, 0), currentState="Walk"):
        super().__init__(name, pos, currentState)

    def Walk(self):
        self.NextFrame()
        return self.animation["Walk"][self.animationNum]


class Equipment:
    def __init__(self, name) -> None:
        self.image = pygame.image.load(f"./img/{name}.PNG")
        self.pos = (0, 0)
