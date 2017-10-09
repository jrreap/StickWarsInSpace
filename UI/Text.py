import pygame

pygame.init()

# Class that is responsible for the creation of text on the screen
# It takes 3 main variables and then you can configure the color and bold as extras
# height and width are the location of the text from the top left corner
# text is the actual text... can be whatever you want it to be as long as its a string
class Text():
    
    def __init__(self, height, width, text, color=(255,255,255), bold=False, font="Segoe Print", fontSize = 35):

        self.x = width
        self.y = height
        self.font = pygame.font.SysFont(font, fontSize)
        self.txt = self.font.render(text, bold, color)
        self.size = self.font.size(text)
        
    def DrawCenter(self, screen):
        drawX = (screen.get_width() / 2.) - (self.size[0] / 2.)
        drawY = self.y - (self.size[1] / 2.)
        coords = (drawX, drawY)
        screen.blit(self.txt, coords)
        
    def Draw(self, screen):
        drawX = self.x - (self.size[0] / 2.)
        drawY = self.y - (self.size[1] / 2.)
        coords = (drawX, drawY)
        screen.blit(self.txt, coords)
        
        
        
