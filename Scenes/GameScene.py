import pygame
from SceneBase import SceneBase
from ImageCache.ImageLoader import GetImage
from UnitManagement.UnitLoader import UnitLoader
from UnitManagement.UnitMovement import UnitMovement
from UI.Text import Text
from UI.Button import Button
from UI.Bar import Bar
import pygame

class GameScene(SceneBase):

    def __init__(self):
        SceneBase.__init__(self)

        self.unitidgen = 0

        self.UnitMovement = UnitMovement()

        self.text = Text(20, 600, "GAME VIEW", bold=True, color=(45, 185, 255))

        self.attackbutton = Button("Attack", (60,635), self.Attack, size=(120,30), font_size=20, bg=(109,177,255))
        self.holdbutton = Button("Hold", (185,635), self.HoldPosition, size=(120,30), font_size=20, bg=(109,177,255))
        self.defendbutton = Button("Defend", (310,635), self.DefendPosition, size=(120,30), font_size=20, bg=(109,177,255))
        self.resourcebar = Bar("Moon Crystals: 100", (1120, 15), size=(160,30), font_size=20, bg=(176,185,186))

        self.buildhorserifleblaster = Button("RB", (1140, 635), self.BRB, size=(60,30), font_size=15, bg=(109,177,255))

    def ProcessInput(self, events, pressed_keys):
        mousepos = pygame.mouse.get_pos()
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                self.SwitchToScene(None)
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.SwitchToScene(None)

            elif event.type == pygame.MOUSEBUTTONDOWN:

                if self.attackbutton.IsClicked(mousepos):
                    self.Attack()

                if self.defendbutton.IsClicked(mousepos):
                    self.DefendPosition()

                if self.holdbutton.IsClicked(mousepos):
                    self.HoldPosition()

                if self.buildhorserifleblaster.IsClicked(mousepos):
                    self.BRB()

    def Update(self):

        self.cu = UnitLoader.GetCreatedUnits()

        # Move all the units based on the current movement mode
        self.UnitMovement.MoveUnits()

    def Render(self, screen):
        screen.fill((0, 0, 0))

        screen.blit(GetImage("./Images/MoonBG1.jpg"), (0, 0))

        # Draw all created units on screen
        for unit in self.cu:
            screen.blit(GetImage("Images/StickSoldier.jpg"), (unit.xpos, unit.ypos))

        # Draw the GUI
        self.attackbutton.Draw(screen)
        self.holdbutton.Draw(screen)
        self.defendbutton.Draw(screen)
        self.resourcebar.Draw(screen)
        self.buildhorserifleblaster.Draw(screen)
        self.text.Draw(screen)

    # Button functions

    def Attack(self):
        self.UnitMovement.SetMovementMode("A")

    def HoldPosition(self):
        self.UnitMovement.SetMovementMode("H")

    def DefendPosition(self):
        self.UnitMovement.SetMovementMode("D")

    def BRB(self):
        unit = UnitLoader.GetUnitByUnitClass("Rifle Blaster")
        unit.laneid = 1

        self.unitidgen += 1

        UnitLoader.InstantiateUnit(unit, self.unitidgen)
