import pygame
from Scenes.SceneBase import SceneBase
from Scenes.GameScene import GameScene
from Scenes.OptionsScene import OptionsScene
from ImageCache.ImageLoader import GetImage
from Music.Boombox import Boombox
from UI.Button import Button
from UI.Text import Text
from Scenes.Lore.SpaceMongolianLoreTohnborjin import SpaceMongolianLoreTohnborjin
from Scenes.Instructions import Instructions
from Scenes.Levels.Level1Opening import Level1Opening
from Scenes.Levels.Level3Opening import Level3Opening
from Scenes.SaturnGameScene import SaturnGameScene
from Scenes.Levels.Level2Opening import Level2Opening
from Scenes.Levels.Level4Opening import Level4Opening
from Scenes.Levels.Level5Opening import Level5Opening
from Scenes.Levels.Level6Opening import Level6Opening
from UpgradeDataBullshit.LevelData import LevelData


# This scene is responsible for rendering the menu "scene"
class LevelSelect(SceneBase):

    def __init__(self):
        SceneBase.__init__(self)
        self.text = Text(228, 600, "Level Select", bold=True,
                         color=(109, 177, 255), fontSize=45)
        self.marsbutton = Button("2. Mars", (690, 325), self.Mars, size=(120, 60), font_size=20,
                                  bg=(109, 177, 255))
        self.moonbutton = Button("1. Moon", (510, 325), self.Moon, size=(120, 60), font_size=20,
                                         bg=(109, 177, 255))
        self.saturnbutton = Button("3. Saturn", (510, 425), self.Saturn, size=(120, 60), font_size=20, bg=(109, 177, 255))
        self.mercurybutton = Button("4. Mercury", (690, 425), self.Mercury, size=(120, 60), font_size=20,
                                 bg=(109, 177, 255))

        self.uranusbutton = Button("5. Uranus", (510, 525), self.Uranus, size=(120,60), font_size=20, bg=(109,177,255))
        self.neptunebutton = Button("6. Neptune", (690, 525), self.Neptune, size=(120,60), font_size=20, bg=(109,177,255))

        self.continuebutton = Button("Back", (50, 625), self.Continue, size=(60, 30), bg=(109, 177, 255))
        # Start music
        b = Boombox()

        if not b.MusicStatus():
            b.PlayMusic("menumusic")

    def ProcessInput(self, events, pressed_keys):
        mousepos = pygame.mouse.get_pos()
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                self.SwitchToScene(None)

            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.SwitchToScene("Scenes.MenuScene.MenuScene")

            elif event.type == pygame.MOUSEBUTTONDOWN:

                # Check if the buttons has been pressed
                if self.marsbutton.IsClicked(mousepos) and LevelData.mars:
                    self.marsbutton.call_back_()

                if self.mercurybutton.IsClicked(mousepos) and LevelData.mercury:
                    self.mercurybutton.call_back_()

                if self.saturnbutton.IsClicked(mousepos) and LevelData.saturn:
                    self.saturnbutton.call_back_()

                if self.moonbutton.IsClicked(mousepos):
                    self.moonbutton.call_back_()

                if self.uranusbutton.IsClicked(mousepos) and LevelData.uranus:
                    self.uranusbutton.call_back_()

                if self.continuebutton.IsClicked(mousepos):
                    self.continuebutton.call_back_()

                if self.neptunebutton.IsClicked(mousepos) and LevelData.neptune:
                    self.neptunebutton.call_back_()

    def Update(self):
        pass

    def Render(self, screen):
        screen.fill((0, 0, 0))

        screen.blit(GetImage("./Images/MoonBG1.jpg"), (0, 0))

        self.text.Draw(screen)
        if LevelData.mars:
            self.marsbutton.Draw(screen)
        if LevelData.mercury:
            self.mercurybutton.Draw(screen)
        if LevelData.saturn:
            self.saturnbutton.Draw(screen)
        self.moonbutton.Draw(screen)
        if LevelData.uranus:
            self.uranusbutton.Draw(screen)
        self.continuebutton.Draw(screen)
        if LevelData.neptune:
            self.neptunebutton.Draw(screen)

    # Button functions
    def Mercury(self):
        print("Starting New Game : Mercury...")
        self.SwitchToScene("Scenes.Levels.Level4Opening.Level4Opening")


    def Mars(self):
        print("Starting New Game : Mars...")
        self.SwitchToScene("Scenes.Levels.Level2Opening.Level2Opening")

    def Saturn(self):
        print("Starting New Game : Saturn...")
        self.SwitchToScene("Scenes.Levels.Level3Opening.Level3Opening")


    def Moon(self):
        print("Starting New Game : Moon...")
        self.SwitchToScene("Scenes.Levels.Level1Opening.Level1Opening")

    def Uranus(self):
        print("Starting New Game : Ur ANUS...")
        self.SwitchToScene("Scenes.Levels.Level5Opening.Level5Opening")

    def Neptune(self):
        print("Starting New Game : Neptune...")
        self.SwitchToScene("Scenes.Levels.Level6Opening.Level6Opening")

    def Continue(self):
        print("returning to menu")
        self.SwitchToScene("Scenes.MenuScene.MenuScene")
        
