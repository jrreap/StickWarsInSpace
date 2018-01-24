import pygame
import random
from Scenes.SceneBase import SceneBase
from ImageCache.ImageLoader import GetImage
from Music.Boombox import Boombox
from UI.Button import Button
from UI.Text import Text
from Scenes.Levels.Level2Opening import Level2Opening
from UpgradeDataBullshit.UpgradeData import UpgradeData



class MoonUpgrade(SceneBase):
    
    def __init__(self):
        SceneBase.__init__(self)
        
        
        self.economybutton = Button("+5 MoonCrystals Economy", (300,200), self.Economy, size=(240,60), font_size=20, bg=(109,177,255))

        self.defensebutton = Button("+500 Mothership HP", (300, 300), self.Defense, size=(240,60), font_size=20, bg=(109,177,255))


        self.damagebutton = Button("Unit Damage +10", (300,400), self.Damage, size=(240,60), font_size=20, bg=(109,177,255))

        self.healthbutton = Button("Unit Health +20", (300,500), self.Health, size=(240,60), font_size=20, bg=(109,177,255))


       


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

                if self.damagebutton.IsClicked(mousepos):
                    self.damagebutton.call_back_()

                if self.healthbutton.IsClicked(mousepos):
                    self.healthbutton.call_back_()


    def Update(self):
        pass

    def Render(self, screen):
        screen.fill((0, 0, 0))

        screen.blit(GetImage("./Images/background.jpg"), (0, 0))
        self.economybutton.Draw(screen)
        self.defensebutton.Draw(screen)
        self.damagebutton.Draw(screen)
        self.healthbutton.Draw(screen)

    def Economy(self):
        UpgradeData.EconomyUpgrade(True)
        print("Economy upgraded")
        print(UpgradeData.economy)
        self.SwitchToScene("Scenes.Levels.Level2Opening.Level2Opening")

    def Defense(self):
        UpgradeData.DefenseUpgrade(True)
        print("Defense upgraded")
        print(UpgradeData.defense)
        self.SwitchToScene("Scenes.Levels.Level2Opening.Level2Opening")

    def Damage(self):
        UpgradeData.DamageUpgrade(True)
        print("unit damage upgraded")
        self.SwitchToScene("Scenes.Levels.Level2Opening.Level2Opening")

    def Health(self):
        UpgradeData.HealthUpgrade(True)
        print("unit health upgraded")
        self.SwitchToScene("Scenes.Levels.Level2Opening.Level2Opening")

        
        
    
    
        
