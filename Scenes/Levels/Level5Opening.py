import pygame
from Scenes.SceneBase import SceneBase
from Scenes.GameScene import GameScene
from ImageCache.ImageLoader import GetImage
from UI.Button import Button
from Scenes.UranusGameScene import UranusGameScene




class Level5Opening (SceneBase):

    def __init__(self):
        SceneBase.__init__(self)
        self.continuebutton = Button("Continue", (900,500), self.Continue, size=(160,60), font_size=20, bg=(109,177,255))

    def ProcessInput(self, events, pressed_keys):
        mousepos = pygame.mouse.get_pos()
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                self.SwitchToScene(None)
            elif event.type == pygame.MOUSEBUTTONDOWN:

                if self.continuebutton.IsClicked(mousepos):
                    self.continuebutton.call_back_()
                    
    def Update(self):
        pass
    
    def Render(self, screen):
        screen.fill((0, 0, 0))
            
        screen.blit(GetImage("./Images/level5opening.jpg"), (0,0))
        self.continuebutton.Draw(screen)

    def Continue(self):
        print("going to uranus game")
        self.SwitchToScene(UranusGameScene())
        

      
