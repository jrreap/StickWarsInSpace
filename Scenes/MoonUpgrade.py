import pygame
import random
from Scenes.SceneBase import SceneBase
from ImageCache.ImageLoader import GetImage
from Music.Boombox import Boombox
from UI.Button import Button
from UI.Text import Text
from Scenes.UpgradeData import UpgradeData

class SaturnUpgrade(SceneBase):

    def __init__(self):
        SceneBase.__init__(self)
        self.economybutton = Button("+20% Economy", (300,200), self.Economy, size=(120,60), font_size=20, bg=(109,177,255))
        self.defensebutton = Button("+20% Mothership HP", (300, 300), self.Defense, size=(120,60), font_size=20, bg=(109,177,255))
        self.speedbutton = Button("Speed Spell", (300,400), self.Speed, size=(120,60), font_size=20, bg=(109,177,255))
        self.ragebutton = Button("Rage Spell", (300,500), self.Rage, size=(120,60), font_size=20, bg=(109,177,255))

        self.nextbutton = Button("Continue...", (500, 600), self.Next, size=(120,60), font_size=20, bg=(109,177,255))


        b = Boombox()

        if not b.MusicStatus():
            b.PlayMusic("menumusic")

    def ProcessInput(self, events, pressed_keys):
        mousepos = pygame.mouse.get_pos()
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                self.SwitchToScene(None)

            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.SwitchToScene(None)

            elif event.type == pygame.MOUSEBUTTONDOWN:

                # Check if the buttons has been pressed
                if self.economybutton.IsClicked(mousepos):
                    self.economybutton.call_back_()

                if self.defensebutton.IsClicked(mousepos):
                    self.defensebutton.call_back_()

                if self.speedbutton.IsClicked(mousepos):
                    self.speedbutton.call_back_()

                if self.ragebutton.IsClicked(mousepos):
                    self.ragebutton.call_back_()

                if self.nextbutton.IsClicked(mousepos):
                    self.nextbutton.call_back_()

    def Update(self):
        pass

    def Render(self, screen):
        screen.fill((0, 0, 0))

        screen.blit(GetImage("./Images/MoonBG1.jpg"), (0, 0))
        self.text.DrawCenter(screen)
        self.text1.DrawCenter(screen)
        self.economybutton.Draw(screen)
        self.defensebutton.Draw(screen)
        self.speedbutton.Draw(screen)
        self.ragebutton.Draw(screen)
        self.nextbutton.Draw(screen)

    def Economy(self):
        print("Economy upgraded")
        EconomyUpgrade(1);

    def Defense(self):
        print("Defense upgraded")
        DefenseUpgrade(1);

    def Speed(self):
        print("Speed Spell gotten")
        SpeedSpell(1);

    def Rage(self):
        print("Rage Spell gotten")
        RageSpell(1);

    def Next(self):
        print("moving onwards...")
        
    
    
        
