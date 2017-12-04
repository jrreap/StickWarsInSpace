import pygame
from Scenes.Camera import Camera

pygame.init()

# Preset color presents to allow for quick colors to be set
WHITE = (255, 255, 255)
GREY = (200, 200, 200)
BLACK = (0, 0, 0)


# Main class that handles the creation of toggle menus
class ToggleBox():
    def __init__(self, location, bg=BLACK, fg=BLACK, size=(80, 30), shown=True):
        self.color = bg
        self.bg = bg
        self.fg = fg
        self.size = size
        self.shown = shown
        self.location = location

        self.buttons = []

        self.surface = pygame.surface.Surface(size)
        self.rect = self.surface.get_rect(center=Camera.RenderPosition(location[0], location[1]))

    def ToggleBox(self, toggle):
        self.shown = toggle

    def IsToggled(self):
        return self.shown

    def Draw(self, screen):

        if self.shown:
            self.surface.fill(self.bg)

            self.rect = self.surface.get_rect(center=Camera.RenderUIPosition(self.location[0], self.location[1]))

            screen.blit(self.surface, self.rect)
        else:
            pass