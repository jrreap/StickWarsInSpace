import pygame

pygame.init()

#Class that is responsible for the creation of text on the screen
class Text():
    
    def __init__(self, height, width, text, color=(255,255,255), bold=False):
        
        self.x = width
        self.y = height
        
        self.font = pygame.font.SysFont("Segoe Print", 35)
        self.txt = self.font.render(text, bold, color)
        self.size = self.font.size(text)
        
    def Draw(self, screen):
        drawX = self.x - (self.size[0] / 2.)
        drawY = self.y - (self.size[1] / 2.)
        coords = (drawX, drawY)
        screen.blit(self.txt, coords)
        
        
        