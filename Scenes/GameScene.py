from SceneBase import SceneBase
from ImageCache.ImageLoader import GetImage
from UnitManagement.UnitLoader import UnitLoader
from UnitManagement.UnitMovement import UnitMovement
from UI.Text import Text
from UI.Button import Button
from UI.Bar import Bar
from UI.StatBar import StatBar
from UI.ToggleMenu import ToggleMenu
import pygame

class GameScene(SceneBase):

    def __init__(self):
        SceneBase.__init__(self)

        self.UnitMovement = UnitMovement()

        self.text = Text(20, 600, "GAME VIEW", bold=True, color=(45, 185, 255))

        self.defendbutton = Button("Defend", (60,635), self.Attack, size=(120,30), font_size=20, bg=(109,177,255))
        self.holdbutton = Button("Hold", (185,635), self.HoldPosition, size=(120,30), font_size=20, bg=(109,177,255))
        self.attackbutton = Button("Attack", (310,635), self.DefendPosition, size=(120,30), font_size=20, bg=(109,177,255))
        self.openmenu = Button("Menu", (1130, 600), self.Menu, size=(120,30), font_size=20, bg=(109, 177, 255))

        self.resourcebar = Bar("Moon Crystals: 100", (1120, 15), size=(160,30), font_size=20, bg=(176,185,186))

        self.buildmenu = ToggleMenu((1140, 350), size=(100, 400), bg=(176,185,186), shown=False)
        self.buildrifleblaster = Button("RB", (1140, 175), self.BRB, size=(60,30), font_size=15, bg=(109,177,255))
        self.buildhorserifleblaster = Button("HRB", (1140, 225), self.BHRB, size=(60,30), font_size=15, bg=(109, 177, 255))
        self.buildmenutoggle = False

        self.buildqueue = StatBar(" ", (1090, 635), size=(200, 20), bg=(176, 185, 186), fg=(109, 177, 255))

        self.buildmenu.AddButton(self.buildhorserifleblaster)
        self.buildmenu.AddButton(self.buildrifleblaster)

    def ProcessInput(self, events, pressed_keys):
        mousepos = pygame.mouse.get_pos()
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                self.SwitchToScene(None)
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.SwitchToScene(None)

            elif event.type == pygame.KEYDOWN and event.key == pygame.K_a:
                self.buildqueue.SetFillPercentage(10, 100)

            elif event.type == pygame.KEYDOWN and event.key == pygame.K_b:
                self.buildmenutoggle = not self.buildmenutoggle
                self.buildmenu.ToggleMenu(self.buildmenutoggle)

            elif event.type == pygame.MOUSEBUTTONDOWN:

                if self.attackbutton.IsClicked(mousepos):
                    self.attackbutton.call_back_()

                if self.defendbutton.IsClicked(mousepos):
                    self.defendbutton.call_back_()

                if self.holdbutton.IsClicked(mousepos):
                    self.holdbutton.call_back_()

                if self.buildhorserifleblaster.IsClicked(mousepos):
                    self.buildhorserifleblaster.call_back_()

                if self.buildrifleblaster.IsClicked(mousepos):
                    self.buildrifleblaster.call_back_()

                if self.openmenu.IsClicked(mousepos):
                    self.buildmenutoggle = not self.buildmenutoggle
                    self.buildmenu.ToggleMenu(self.buildmenutoggle)

    def Update(self):

        self.cu = UnitLoader.GetCreatedUnits()

        # Move all the units based on the current movement mode
        self.UnitMovement.MoveUnits()
        UnitLoader.BuildUnitsInQueue(self.buildqueue)

    def Render(self, screen):
        screen.fill((0, 0, 0))

        screen.blit(GetImage("./Images/MoonBG1.jpg"), (0, 0))

        # Draw all created units on screen
        for unit in self.cu:
           screen.blit(GetImage(unit.imagepath), (unit.xpos, unit.ypos))
            
        # Draw the GUI
        self.attackbutton.Draw(screen)
        self.holdbutton.Draw(screen)
        self.defendbutton.Draw(screen)
        self.resourcebar.Draw(screen)
        self.text.Draw(screen)
        self.buildqueue.Draw(screen)
        self.buildmenu.Draw(screen)
        self.openmenu.Draw(screen)

    # Button functions

    def DefendPosition(self):
        self.UnitMovement.SetMovementMode("A")

    def Menu(self):
        self.buildmenutoggle = not self.buildmenutoggle
        self.buildmenu.ToggleMenu(self.buildmenutoggle)

    def HoldPosition(self):
        self.UnitMovement.SetMovementMode("H")

    def Attack(self):
        self.UnitMovement.SetMovementMode("D")

    def BRB(self):
        unit = UnitLoader.GetUnitByUnitClass("Rifle Blaster")
        unit.laneid = 1

        UnitLoader.EnqueueUnit(unit)

    def BHRB(self):
        unit = UnitLoader.GetUnitByUnitClass("Horse Rifle Blaster")
        unit.laneid = 1

        UnitLoader.EnqueueUnit(unit)
