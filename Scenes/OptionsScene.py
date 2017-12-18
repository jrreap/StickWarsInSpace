import pygame
from Scenes.SceneBase import SceneBase
from Options.Options import Options
from ImageCache.ImageLoader import GetImage
from Music.Boombox import Boombox
from UI.Text import Text
from UI.ToggleBox import ToggleBox
from UI.Button import Button


# This scene is responsible for rendering the options "scene"
class OptionsScene(SceneBase):
    def __init__(self):
        SceneBase.__init__(self)

        self.hardcoremode = ToggleBox((600, 225), self.HardcoreMode, size=(30, 30), bg=(0, 170, 28))
        self.hardcoretext = Text(225, 500, "Hardcore Mode", bold=True, font="Arial", fontSize=18)

        self.backbutton = Button("Back", (50, 625), self.GoBack, size=(60, 30), bg=(109, 177, 255))

        self.text1 = Text(100, 600, "Options Menu", bold=True,
                          color=(255, 255, 255), font="Arial", fontSize=35)

    def ProcessInput(self, events, pressed_keys):
        mousepos = pygame.mouse.get_pos()
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                self.SwitchToScene(None)
            elif event.type == pygame.MOUSEBUTTONDOWN:

                # Check if the buttons have been pressed
                if self.hardcoremode.IsClicked(mousepos):
                    self.hardcoremode.ToggleBox()
                    self.hardcoremode.call_back()

                if self.backbutton.IsClicked(mousepos):
                    self.backbutton.call_back_()

    def Update(self):
        pass

    def Render(self, screen):
        screen.fill((0, 0, 0))

        screen.blit(GetImage("./Images/MoonBG1.jpg"), (0, 0))

        self.text1.Draw(screen)
        self.hardcoretext.Draw(screen)

        self.backbutton.Draw(screen)

        if Options.hardcoremode == True:
            self.hardcoremode.SetToggle(True)

        self.hardcoremode.Draw(screen)

    # Button functions
    def HardcoreMode(self):
        Options.SetHardcoreMode(self.hardcoremode.IsToggled())

    def GoBack(self):
        self.SwitchToScene("Scenes.MenuScene.MenuScene")
