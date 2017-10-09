import pygame
from Scenes.SceneBase import SceneBase
from Scenes.GameScene import GameScene
from ImageCache.ImageLoader import GetImage
from UI.Button import Button
from UI.Text import Text

#This scene is responsible for rendering the menu "scene"
class MenuScene(SceneBase):
    
    def __init__(self):
        SceneBase.__init__(self)
        self.startbutton = Button("Start Game", (600,325), self.StartGame, size=(120,60), font_size=20, bg=(109,177,255))
        self.exitbutton = Button("Exit Game", (600,425), self.ExitGame, size=(120,60), font_size=20, bg=(109,177,255))
                
        self.text = Text(225, 600, "Mongolian Space Stick Wars XD Special Day One Edition", bold=True, color=(109,177,255))

        self.text1 = Text(224, 600, "Mongolian Space Stick Wars XD Special Day One Edition", bold=True, color = (0,0,0), font = "Segoe Print", fontSize = 35 )


    def ProcessInput(self, events, pressed_keys):
        mousepos = pygame.mouse.get_pos()
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                self.SwitchToScene(None)
            elif event.type == pygame.MOUSEBUTTONDOWN:

                #Check if the buttons has been pressed
                if self.startbutton.IsClicked(mousepos):
                    self.startbutton.call_back_()

                if self.exitbutton.IsClicked(mousepos):
                    self.exitbutton.call_back_()
                
                
                
    def Update(self):
        pass
    
    def Render(self, screen):
        screen.fill((0, 0, 0))
            
        screen.blit(GetImage("./Images/background.jpg"), (0,0))
        
        self.text.DrawCenter(screen)
        self.text1.DrawCenter(screen)
        self.startbutton.Draw(screen)
        self.exitbutton.Draw(screen)
        

    #Button functions
    def ExitGame(self):
        print("Exiting Game...")
        self.next = None

    def StartGame(self):
        print("Starting New Game...")
        self.SwitchToScene(GameScene())
        
        
        
        
        
        
        
