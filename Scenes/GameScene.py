import pygame
from SceneBase import SceneBase
from ImageCache.ImageLoader import GetImage
from UI.Text import Text
from UI.Button import Button
import pygame

class GameScene(SceneBase):

    def __init__(self):
        SceneBase.__init__(self)

        self.text = Text(20, 600, "GAME VIEW", bold=True, color=(45, 185, 255))

        self.attackbutton = Button("Attack", (60,635), self.Attack(), size=(120,30), font_size=20, bg=(109,177,255))
        self.holdbutton = Button("Hold", (185,635), self.HoldPosition(), size=(120,30), font_size=20, bg=(109,177,255))
        self.defendbutton = Button("Defense", (310,635), self.DefendPosition(), size=(120,30), font_size=20, bg=(109,177,255))

    def ProcessInput(self, events, pressed_keys):
        mousepos = pygame.mouse.get_pos()
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                self.SwitchToScene(None)
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.SwitchToScene(None)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                print("Input Caught")

    def Update(self):
        pass

    def Render(self, screen):
        screen.fill((0, 0, 0))

        screen.blit(GetImage("./Images/background.jpg"), (0, 0))

        self.attackbutton.Draw(screen)
        self.holdbutton.Draw(screen)
        self.defendbutton.Draw(screen)
        self.text.Draw(screen)

    # Button functions

    def Attack(self):
        print("Charge!")

    def HoldPosition(self):
        print("Hold Your Ground!")

    def DefendPosition(self):
        print("Retreat To The Ship!")
