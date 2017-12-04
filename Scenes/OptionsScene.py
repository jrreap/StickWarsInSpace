import pygame
from Scenes.SceneBase import SceneBase
from ImageCache.ImageLoader import GetImage
from Music.Boombox import Boombox
from UI.Button import Button
from UI.Text import Text
from Scenes.Lore.SpaceMongolianLoreTohnborjin import SpaceMongolianLoreTohnborjin


# This scene is responsible for rendering the menu "scene"
class OptionsScene(SceneBase):
    def __init__(self):
        SceneBase.__init__(self)
        self.optionsbutton = Button("Options", (1150, 625), self.Options, size=(60, 30), bg=(109, 177, 255))

        self.text1 = Text(100, 600, "Options Menu", bold=True,
                          color=(255, 255, 255), font="Arial", fontSize=35)

        # Start music
        b = Boombox()
        b.playmusic("menumusic")

    def ProcessInput(self, events, pressed_keys):
        mousepos = pygame.mouse.get_pos()
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                self.SwitchToScene(None)
            elif event.type == pygame.MOUSEBUTTONDOWN:

                # Check if the buttons have been pressed
                if self.optionsbutton.IsClicked(mousepos):
                    self.optionsbutton.call_back_()


    def Update(self):
        pass

    def Render(self, screen):
        screen.fill((0, 0, 0))

        screen.blit(GetImage("./Images/MoonBG1.jpg"), (0, 0))

        self.text1.Draw(screen)

        self.optionsbutton.Draw(screen)

    # Button functions
    def Options(self):
        pass

