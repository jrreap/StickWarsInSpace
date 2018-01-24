import pygame
from Scenes.SceneBase import SceneBase
from Scenes.GameScene import GameScene
from ImageCache.ImageLoader import GetImage
from UI.Button import Button
from UI.Text import Text

class Credits (SceneBase):

    def __init__ (self):
        SceneBase.__init__(self)
        self.text = Text(228, 600, "Special Thanks: Connor Daniel", bold=True, color=(109, 177, 255), fontSize=45)
        self.returnbutton = Button("Return to Menu", (900, 425), self.GoBack, size = (300,60), font_size = 20, bg = (109,177,255))

    def ProcessInput (self, events, pressed_keys):
        mousepos = pygame.mouse.get_pos()
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                self.SwitchToScene(None)
            elif event.type == pygame.MOUSEBUTTONDOWN:

                if self.returnbutton.IsClicked(mousepos):
                    self.returnbutton.call_back_()

    def Update(self):
        pass

    def Render (self, screen):
        screen.fill((0, 0, 0))

        screen.blit(GetImage("./Images/MoonBG1.jpg"), (0, 0))
        self.text.Draw(screen)
        self.returnbutton.Draw(screen)

    def GoBack(self):
        print("REturning to menu")
        self.SwitchToScene("Scenes.MenuScene.MenuScene")
