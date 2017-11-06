import pygame
from Scenes.Camera import Camera

pygame.init()

# Preset color presents to allow for quick colors to be set
WHITE = (255,255,255)
GREY = (200,200,200)
BLACK = (0,0,0)


# Main class that handles the creation of buttons. Also manages the tracking of if the button has been clicked
# and then calling the call back function (aka the action)
class Button():
    def __init__(self, txt, location, action, bg=WHITE, fg=BLACK, size=(80,30), font_name="Arial", font_size=16):
        self.color = bg
        self.bg = bg
        self.fg = fg
        self.size = size
        self.location = location
        
        self.font = pygame.font.SysFont(font_name, font_size, True, False)
        self.txt = txt
        self.txt_surf = self.font.render(self.txt, 1, self.fg)
        self.txt_rect = self.txt_surf.get_rect(center=[s//2 for s in self.size])
        
        self.surface = pygame.surface.Surface(size)
        self.rect = self.surface.get_rect(center=location)
        
        self.call_back_ = action
        
    def Draw(self, screen):
        self.Mouseover()
        
        self.surface.fill(self.bg)
        self.surface.blit(self.txt_surf, self.txt_rect)

        self.rect = self.surface.get_rect(center=Camera.RenderUIPosition(self.location[0], self.location[1]))

        screen.blit(self.surface, self.rect)

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