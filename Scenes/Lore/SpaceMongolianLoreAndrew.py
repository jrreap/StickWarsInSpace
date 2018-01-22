import pygame
from Scenes.SceneBase import SceneBase
from Scenes.GameScene import GameScene
from ImageCache.ImageLoader import GetImage
from UI.Button import Button
from UI.Text import Text
from Scenes.Lore.SpaceMongolianLoreJaydon import SpaceMongolianLoreJaydon
from Music.Boombox import Boombox


#renders Lore
class SpaceMongolianLoreAndrew (SceneBase):

    def __init__(self):
        SceneBase.__init__(self)
        self.continuebutton = Button("Continue", (900, 525), self.Continue, size=(120,60), font_size=20, bg=(109,177,255))
        self.backbutton = Button("Back", (900,605), self.GoBack, size=(120,60), font_size=20, bg=(109,177,255))

        b = Boombox()
        if not b.MusicStatus():
            b.PlayMusic("loremusic")
            
    def ProcessInput(self, events, pressed_keys):
        mousepos = pygame.mouse.get_pos()
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                self.SwitchToScene(None)
            elif event.type == pygame.MOUSEBUTTONDOWN:

                # Check if the buttons has been pressed
                if self.continuebutton.IsClicked(mousepos):
                    self.continuebutton.call_back_()

                if self.backbutton.IsClicked(mousepos):
                    self.backbutton.call_back_()
                    
    def Update(self):
        pass

    def Render (self, screen):
        screen.fill((0, 0, 0))

        screen.blit(GetImage("./Images/Lore/andrewlore.jpg"), (0,0))

        self.continuebutton.Draw(screen)
        self.backbutton.Draw(screen)

    def Continue(self):
        print("Next Lore")
        self.SwitchToScene(SpaceMongolianLoreJaydon())

    def GoBack(self):
        print("Returning to tohnlore")
        self.SwitchToScene("Scenes.Lore.SpaceMongolianLoreTohnborjin.SpaceMongolianLoreTohnborjin")
