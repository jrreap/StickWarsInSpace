import pygame
from Scenes.Camera import Camera

pygame.init()

# Preset color presents to allow for quick colors to be set
WHITE = (255, 255, 255)
GREY = (200, 200, 200)
BLACK = (0, 0, 0)


# Main class that handles the creation of static bar objects
class Bar():
    def __init__(self, txt, location, bg=BLACK, fg=BLACK, size=(80, 30), font_name="Arial", font_size=16):
        self.color = bg
        self.bg = bg
        self.fg = fg
        self.size = size
        self.location = location

        self.font = pygame.font.SysFont(font_name, font_size, True, False)
        self.txt = txt
        self.txt_surf = self.font.render(self.txt, 1, self.fg)
        self.txt_rect = self.txt_surf.get_rect(center=[s // 2 for s in self.size])

        self.surface = pygame.surface.Surface(size)
        self.rect = self.surface.get_rect(center=location)

    # Draws the UI element on screen
    def Draw(self, screen):
        self.surface.fill(self.bg)
        self.surface.blit(self.txt_surf, self.txt_rect)

        self.rect = self.surface.get_rect(center= Camera.RenderUIPosition(self.location[0], self.location[1]))

        screen.blit(self.surface, self.rect)

    # Changes the text element of the UI object
    def SetText(self, txt):
        self.txt = txt
        self.txt_surf = self.font.render(self.txt, 1, self.fg)
        self.txt_rect = self.txt_surf.get_rect(center=[s // 2 for s in self.size])