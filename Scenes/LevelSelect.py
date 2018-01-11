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


# This scene is responsible for rendering the menu "scene"
class LevelSelect(SceneBase):

    def __init__(self):
        SceneBase.__init__(self)
        self.startbutton = Button("Mars", (510, 325), self.StartGame, size=(120, 60), font_size=20,
                                  bg=(109, 177, 255))
        self.Instructionsbutton = Button("Moon", (690, 325), self.Instructions, size=(120, 60), font_size=20,
                                         bg=(109, 177, 255))
        self.Lorebutton = Button("Jupiter", (510, 425), self.Lore, size=(120, 60), font_size=20, bg=(109, 177, 255))
        self.exitbutton = Button("Other Planet", (690, 425), self.ExitGame, size=(120, 60), font_size=20,
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
                if self.startbutton.IsClicked(mousepos):
                    self.startbutton.call_back_()

                if self.exitbutton.IsClicked(mousepos):
                    self.exitbutton.call_back_()

                if self.Lorebutton.IsClicked(mousepos):
                    self.Lorebutton.call_back_()

                if self.Instructionsbutton.IsClicked(mousepos):
                    self.Instructionsbutton.call_back_()

    def Update(self):
        pass

    def Render(self, screen):
        screen.fill((0, 0, 0))

        screen.blit(GetImage("./Images/MoonBG1.jpg"), (0, 0))

        self.startbutton.Draw(screen)
        self.exitbutton.Draw(screen)
        self.Lorebutton.Draw(screen)
        self.Instructionsbutton.Draw(screen)

    # Button functions
    def ExitGame(self):
        print("Other planet")


    def StartGame(self):
        print("Starting New Game : Mars...")
        self.SwitchToScene("Scenes.Levels.Level1Opening.Level1Opening")

    def Lore(self):
        print("Jupiter")


    def Instructions(self):
        print("Moon")
