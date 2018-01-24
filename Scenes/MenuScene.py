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
from Scenes.LevelSelect import LevelSelect
from Scenes.Credits import Credits


# This scene is responsible for rendering the menu "scene"
class MenuScene(SceneBase):

    def __init__(self):
        SceneBase.__init__(self)
        self.startbutton = Button("New Game", (510, 325), self.StartGame, size=(120, 60), font_size=20,
                                  bg=(109, 177, 255))
        self.Instructionsbutton = Button("Instructions", (690, 325), self.Instructions, size=(120, 60), font_size=20,
                                         bg=(109, 177, 255))
        self.Lorebutton = Button("Read Lore", (510, 425), self.Lore, size=(120, 60), font_size=20, bg=(109, 177, 255))
        self.exitbutton = Button("Exit Game", (690, 425), self.ExitGame, size=(120, 60), font_size=20,
                                 bg=(109, 177, 255))
        self.optionsbutton = Button("Options", (1150, 625), self.Options, size=(90, 40), bg=(109, 177, 255))
        self.creditsbutton = Button("Credits", (600,525), self.Credits, size=(120,60), font_size=20, bg=(109,177,255))

        
        self.text = Text(228, 600, "Mongolian Space Stick Wars XD Special Day One Edition", bold=True,
                         color=(109, 177, 255), fontSize=45)

        self.text1 = Text(224, 600, "Mongolian Space Stick Wars XD Special Day One Edition", bold=True,
                          color=(255, 255, 255), font="Arial", fontSize=45)
    

        # Start music
        b = Boombox()

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

                if self.optionsbutton.IsClicked(mousepos):
                    self.optionsbutton.call_back_()

                if self.Instructionsbutton.IsClicked(mousepos):
                    self.Instructionsbutton.call_back_()

                if self.creditsbutton.IsClicked(mousepos):
                    self.creditsbutton.call_back_()
    def Update(self):
        pass

    def Render(self, screen):
        screen.fill((0, 0, 0))

        screen.blit(GetImage("./Images/MoonBG1.jpg"), (0, 0))

        self.text.DrawCenter(screen)
        self.text1.DrawCenter(screen)
        self.startbutton.Draw(screen)
        self.exitbutton.Draw(screen)
        self.Lorebutton.Draw(screen)
        self.optionsbutton.Draw(screen)
        self.Instructionsbutton.Draw(screen)
        self.creditsbutton.Draw(screen)

    # Button functions
    def ExitGame(self):
        print("Exiting Game...")
        self.next = None

    def StartGame(self):
        print("Starting New Game...")
        self.SwitchToScene(LevelSelect())

    def Lore(self):
        print("Going to Lore...")
        self.SwitchToScene(SpaceMongolianLoreTohnborjin())

    def Options(self):
        print("Going to Options...")
        self.SwitchToScene(OptionsScene())

    def Instructions(self):
        print("Going to Instructions...")
        self.SwitchToScene(Instructions())

    def Credits(self):
        print("going to credits...")
        self.SwitchToScene(Credits())
        
