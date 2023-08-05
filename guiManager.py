import pygame


class GUI(pygame.Surface):
    def __init__(self, size, pos=(0, 0)) -> None:
        super().__init__(size, pygame.SRCALPHA)
        self.children = [None for i in range(10)]
        self.pos = pos

    def add(self, gui, order):
        self.children[order] = gui

    def update(self):
        self.fill((0, 0, 0, 0))
        for i in self.children:
            if i != None:
                self.blit(i, i.pos)


class Button(GUI):
    def __init__(self, name) -> None:
        self.image = pygame.image.load(f"./img/GUIs/{name}.PNG").convert_alpha()
        self.hoverImage = pygame.image.load(
            f"./img/GUIs/{name}Hover.PNG"
        ).convert_alpha()
        super().__init__(self.image.get_size())

        self.blit(self.image, (0, 0))

    def Hover(self, mousePos):
        if self.image.get_bounding_rect().collidepoint(mousePos):
            self.fill((0, 0, 0, 0))
            self.blit(self.hoverImage, (0, 0))
        else:
            self.fill((0, 0, 0, 0))
            self.blit(self.image, (0, 0))
