import pygame
from Scenes.Camera import Camera

pygame.init()

# Preset color presents to allow for quick colors to be set
WHITE = (255, 255, 255)
GREY = (200, 200, 200)
BLACK = (0, 0, 0)
RED = (255, 21, 0)


# Main class that handles the creation of toggle menus
class ToggleBox():
    def __init__(self, location, action, bg=BLACK, fg=BLACK, size=(80, 30), shown=False):
        self.color = bg
        self.bg = bg
        self.fg = fg
        self.size = size
        self.shown = shown
        self.location = location

        self.surface = pygame.surface.Surface(size)
        self.rect = self.surface.get_rect(center=Camera.RenderPosition(location[0], location[1]))

        self.call_back = action

    def ToggleBox(self):
        self.shown = not self.shown

    def IsToggled(self):
        return self.shown

    # Determines if the cursor is over the current button
    def IsClicked(self, pos):
        if self.rect.collidepoint(pos):
            return True
        else:
            return False

    # Determines if the cursor is over the current button and changes to its hovered color
    def Mouseover(self):
        pos = pygame.mouse.get_pos()
        self.bg = self.color
        if self.rect.collidepoint(pos):
            self.bg = GREY

    # Calls the action assigned to this button
    def CallAction(self):
        self.call_back_()

    def Draw(self, screen):

        if not self.shown:
            self.surface.fill(RED)

            self.rect = self.surface.get_rect(center=Camera.RenderUIPosition(self.location[0], self.location[1]))

            screen.blit(self.surface, self.rect)
        else:
            self.surface.fill(self.bg)

            self.rect = self.surface.get_rect(center=Camera.RenderUIPosition(self.location[0], self.location[1]))

            screen.blit(self.surface, self.rect)