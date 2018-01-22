import pygame
import random
from Scenes.SceneBase import SceneBase
from ImageCache.ImageLoader import GetImage
from Music.Boombox import Boombox
from UI.Button import Button
from UI.Text import Text
from UpgradeDataBullshit.EconomyUpgrade import EconomyUpgrade
from Scenes.Levels.Level4Opening import Level4Opening


class SaturnUpgrade(SceneBase):
    
    def __init__(self):
        SceneBase.__init__(self)

        a = EconomyUpgrade()
        global x
        x = 0
        
        if a.returneconomy() is 1:
            self.economybutton = Button("+10% Economy", (300,200), self.Economy, size=(200,60), font_size=20, bg=(109,177,255))
            x = 1
            print("success")
        self.defensebutton = Button("+10% Mothership HP", (300, 300), self.Defense, size=(200,60), font_size=20, bg=(109,177,255))


        self.speedbutton = Button("Speed Spell", (300,400), self.Speed, size=(200,60), font_size=20, bg=(109,177,255))

        self.ragebutton = Button("Rage Spell", (300,500), self.Rage, size=(200,60), font_size=20, bg=(109,177,255))



        b = Boombox()

        if not b.MusicStatus():
            b.PlayMusic("menumusic")

    def ProcessInput(self, events, pressed_keys):
        global x 
        mousepos = pygame.mouse.get_pos()
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                self.SwitchToScene(None)

            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.SwitchToScene(None)

            elif event.type == pygame.MOUSEBUTTONDOWN:

                # Check if the buttons has been pressed
                if self.economybutton.IsClicked(mousepos) and x is 1:
                    self.economybutton.call_back_()

                if self.defensebutton.IsClicked(mousepos):
                    self.defensebutton.call_back_()

                if self.speedbutton.IsClicked(mousepos):
                    self.speedbutton.call_back_()

                if self.ragebutton.IsClicked(mousepos):
                    self.ragebutton.call_back_()


    def Update(self):
        pass

    def Render(self, screen):
        global x
        screen.fill((0, 0, 0))

        screen.blit(GetImage("./Images/MoonBG1.jpg"), (0, 0))
        if x is 1:
            self.economybutton.Draw(screen)
        self.defensebutton.Draw(screen)
        self.speedbutton.Draw(screen)
        self.ragebutton.Draw(screen)

    def Economy(self):
        print("Economy upgraded")
        a = EconomyUpgrade()
        a.seteconomy()
        self.SwitchToScene("Scenes.Levels.Level4Opening.Level4Opening")

    def Defense(self):
        print("Defense upgraded")
        self.SwitchToScene("Scenes.Levels.Level4Opening.Level4Opening")

    def Speed(self):
        print("Speed Spell gotten")
        self.SwitchToScene("Scenes.Levels.Level4Opening.Level4Opening")

    def Rage(self):
        print("Rage Spell gotten")
        self.SwitchToScene("Scenes.Levels.Level4Opening.Level4Opening")
            
    
        
