import pygame
import random
from Scenes.SceneBase import SceneBase
from ImageCache.ImageLoader import GetImage
from Music.Boombox import Boombox
from UI.Button import Button
from UI.Text import Text
from Scenes.Levels.Level6Opening import Level6Opening
from UpgradeDataBullshit.UpgradeData import UpgradeData



class UranusUpgrade(SceneBase):
    
    def __init__(self):
        SceneBase.__init__(self)

        self.economybutton = Button("+10% Economy", (300,200), self.Economy, size=(200,60), font_size=20, bg=(109,177,255))
        self.defensebutton = Button("+500 Mothership HP", (300, 300), self.Defense, size=(200,60), font_size=20, bg=(109,177,255))


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
                if self.economybutton.IsClicked(mousepos) and not UpgradeData.economy:
                    self.economybutton.call_back_()

                if self.defensebutton.IsClicked(mousepos) and not UpgradeData.defense:
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

        screen.blit(GetImage("./Images/background.jpg"), (0, 0))
        
        if not UpgradeData.economy:
            self.economybutton.Draw(screen)
        if not UpgradeData.defense:
            self.defensebutton.Draw(screen)
        self.speedbutton.Draw(screen)
        self.ragebutton.Draw(screen)

    def Economy(self):
        UpgradeData.EconomyUpgrade(True)
        print("Economy upgraded")
        print(UpgradeData.economy)
        self.SwitchToScene("Scenes.Levels.Level6Opening.Level6Opening")

    def Defense(self):
        UpgradeData.DefenseUpgrade(True)
        print("Defense upgraded")
        print(UpgradeData.defense)
        self.SwitchToScene("Scenes.Levels.Level6Opening.Level6Opening")

    def Speed(self):
        print("Speed Spell gotten")
        self.SwitchToScene("Scenes.Levels.Level6Opening.Level6Opening")

    def Rage(self):
        print("Rage Spell gotten")
        self.SwitchToScene("Scenes.Levels.Level6Opening.Level6Opening")
        

        
    
    
        
