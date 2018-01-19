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


# This scene is responsible for rendering the menu "scene"
class LevelSelect(SceneBase):

    def __init__(self):
        SceneBase.__init__(self)
        self.text = Text(228, 600, "Level Select", bold=True,
                         color=(109, 177, 255), fontSize=45)
        self.marsbutton = Button("Mars", (510, 325), self.Mars, size=(120, 60), font_size=20,
                                  bg=(109, 177, 255))
        self.moonbutton = Button("Moon", (690, 325), self.Moon, size=(120, 60), font_size=20,
                                         bg=(109, 177, 255))
        self.saturnbutton = Button("Saturn", (510, 425), self.Saturn, size=(120, 60), font_size=20, bg=(109, 177, 255))
        self.otherbutton = Button("Other Planet", (690, 425), self.OtherPlanet, size=(120, 60), font_size=20,
                                 bg=(109, 177, 255))
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
                self.SwitchToScene(None)

            elif event.type == pygame.MOUSEBUTTONDOWN:

                # Check if the buttons has been pressed
                if self.marsbutton.IsClicked(mousepos):
                    self.marsbutton.call_back_()

                if self.otherbutton.IsClicked(mousepos):
                    self.exitbutton.call_back_()

                if self.saturnbutton.IsClicked(mousepos):
                    self.saturnbutton.call_back_()

                if self.moonbutton.IsClicked(mousepos):
                    self.moonbutton.call_back_()

    def Update(self):
        pass

    def Render(self, screen):
        screen.fill((0, 0, 0))

        screen.blit(GetImage("./Images/MoonBG1.jpg"), (0, 0))

        self.text.Draw(screen)
        self.marsbutton.Draw(screen)
        self.otherbutton.Draw(screen)
        self.saturnbutton.Draw(screen)
        self.moonbutton.Draw(screen)

    # Button functions
    def OtherPlanet(self):
        print("Other planet")


    def Mars(self):
        print("Starting New Game : Mars...")
        self.SwitchToScene("Scenes.Levels.Level1Opening.Level1Opening")

    def Saturn(self):
        print("Starting New Game : Saturn...")
        self.SwitchToScene("Scenes.Levels.Level3Opening.Level3Opening")


    def Moon(self):
        print("Moon")
