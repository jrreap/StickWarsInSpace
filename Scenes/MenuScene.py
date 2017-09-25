import pygame
from SceneBase import SceneBase
from ImageCache.ImageLoader import GetImage
from UI.Button import Button
from UI.Text import Text

#This scene is responsible for rendering the menu "scene"
class MenuScene(SceneBase):
    
    def __init__(self):
        SceneBase.__init__(self)
        self.startbutton = Button("Start Game", (600,325), self.function, size=(120,60), font_size=20, bg=(255,45,45))
        self.exitbutton = Button("Exit Game", (600,425), self.function, size=(120,60), font_size=20, bg=(255,45,45))
        
        self.text = Text(225, 600, "Mongolian Space Stick Wars XD Special Day One Edition", bold=True, color=(45,185,255))
    
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
        
        self.text.DrawCenter(screen)
        
        self.startbutton.Draw(screen)
        self.exitbutton.Draw(screen)
        

    def function(self):
        SceneBase.next = None
        
        
        
        
        
        
        