import pygame
from Scenes.Camera import Camera

pygame.init()

# Preset color presents to allow for quick colors to be set
WHITE = (255, 255, 255)
GREY = (200, 200, 200)
BLACK = (0, 0, 0)


# Main class tat handles creation and rendering of StatBar objects (like healthbars)
class StatBar():
    def __init__(self, txt, location, bg=WHITE, fg=BLACK, size=(100, 30), font_name="Segoe Print", font_size=16):
        self.color = bg
        self.bg = bg
        self.fg = fg
        self.size = size
        self.location = location

        self.font = pygame.font.SysFont(font_name, font_size, True, False)
        self.txt = txt
        self.txt_surf = self.font.render(self.txt, 1, self.fg)
        self.txt_rect = self.txt_surf.get_rect(center=[s // 2 for s in self.size])

        self.surfacebg = pygame.surface.Surface(size)
        self.rectbg = self.surfacebg.get_rect(center=location)

        self.surfacefg = pygame.surface.Surface(size)
        self.rectfg = self.surfacefg.get_rect(center=location)

        self.SetFillPercentage(0,100)

    # Method that is used to set the percentage of the bar to fill
    # Takes the current value (min) and the maximum is can be (max)
    def SetFillPercentage(self, min1, max1):

        # Render the percent based on the size of the rectangle
        rpercent = int(max(min(min1 / float(max1) * self.size[0], self.size[0]), 0))

        self.surfacefg = pygame.surface.Surface((rpercent, self.size[1]))

    def Draw(self, screen):

        self.surfacebg.fill(self.bg)
        self.surfacebg.blit(self.txt_surf, self.txt_rect)

        self.surfacefg.fill(self.fg)
        self.surfacefg.blit(self.txt_surf, self.txt_rect)

        self.rectbg = self.surfacebg.get_rect(center=Camera.RenderUIPosition(self.location[0], self.location[1]))
        self.rectfg = self.surfacefg.get_rect(center=Camera.RenderUIPosition(self.location[0], self.location[1]))

        screen.blit(self.surfacebg, self.rectbg)
        screen.blit(self.surfacefg, self.rectfg)