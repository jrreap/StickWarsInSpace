import pygame
from SceneBase import SceneBase
from ImageCache.ImageLoader import GetImage
from UI.Button import Button

#This scene is responsible for rendering the menu "scene"
class MenuScene(SceneBase):
    
    def __init__(self):
        SceneBase.__init__(self)
        self.menubutton = Button("BUTTON", (60,30), self.function)
    
    def ProcessInput(self, events, pressed_keys):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                self.SwitchToScene(None)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mousepos = pygame.mouse.get_pos()
                
                
                
    def Update(self):
        pass
    
    def Render(self, screen):
        screen.fill((0, 0, 0))
            
        screen.blit(GetImage("./Images/background.jpg"), (0,0))
        
        self.menubutton.Draw(screen)
        

    def function(self):
        print ("WHOOOOOOOOOO")
        
        
        
        
        
        