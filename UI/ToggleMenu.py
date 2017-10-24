import pygame

pygame.init()

# Preset color presents to allow for quick colors to be set
WHITE = (255, 255, 255)
GREY = (200, 200, 200)
BLACK = (0, 0, 0)


# Main class that handles the creation of toggle menus
class ToggleMenu():
    def __init__(self, location, bg=BLACK, fg=BLACK, size=(80, 30), shown=True):
        self.color = bg
        self.bg = bg
        self.fg = fg
        self.size = size
        self.shown = shown

        self.surface = pygame.surface.Surface(size)
        self.rect = self.surface.get_rect(center=location)

    def ToggleMenu(self, toggle):
        self.shown = toggle

    def Draw(self, screen):

        if self.shown:
            self.surface.fill(self.bg)
            screen.blit(self.surface, self.rect)
        else:
            pass