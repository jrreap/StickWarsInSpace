import pygame
from Scenes.SceneBase import SceneBase
from Scenes.GameScene import GameScene
from ImageCache.ImageLoader import GetImage
from UI.Button import Button
from UI.Text import Text

#renders Lore
class SpaceMongolianLoreKraymer (SceneBase):

    def __init__(self):
        SceneBase.__init__(self)
        self.backbutton = Button("Back", (900,605), self.GoBack, size=(120,60), font_size=20, bg=(109,177,255))

    def ProcessInput(self, events, pressed_keys):
        mousepos = pygame.mouse.get_pos()
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                self.SwitchToScene(None)
            elif event.type == pygame.MOUSEBUTTONDOWN:

                # Check if the buttons has been pressed

                if self.backbutton.IsClicked(mousepos):
                    self.backbutton.call_back_()

                    
    def Update(self):
        pass

    def Render (self, screen):
        screen.fill((0, 0, 0))

        screen.blit(GetImage("./Images/Lore/kramerlore.jpg"), (0,0))


        self.backbutton.Draw(screen)


    def GoBack(self):
        print ("Returning to addisonlore...")
        self.SwitchToScene("Scenes.Lore.SpaceMongolianLoreAddison.SpaceMongolianLoreAddison")
