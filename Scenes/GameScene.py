from SceneBase import SceneBase
from ImageCache.ImageLoader import GetImage
from UnitManagement.UnitLoader import UnitLoader
from UnitManagement.UnitMovement import UnitMovement
from UnitManagement.UnitSpawner import UnitSpawner
from UI.Button import Button
from UI.Bar import Bar
from UI.StatBar import StatBar
from UI.ToggleMenu import ToggleMenu
from AI.BaseAI import BaseAI
from Camera import Camera
import pygame
import random


class GameScene(SceneBase):

    def __init__(self):
        SceneBase.__init__(self)

        self.counter = 0

        self.offset = 0

        self.UnitMovement = UnitMovement()
        self.AI = BaseAI(1)

        self.defendbutton = Button("Defend", (60,635), self.Attack, size=(120,30), font_size=20, bg=(109,177,255))
        self.holdbutton = Button("Hold", (185,635), self.HoldPosition, size=(120,30), font_size=20, bg=(109,177,255))
        self.attackbutton = Button("Attack", (310,635), self.DefendPosition, size=(120,30), font_size=20, bg=(109,177,255))
        self.openmenu = Button("Menu", (1130, 600), self.Menu, size=(120,30), font_size=20, bg=(109, 177, 255))

        self.resourcebar = Bar("Moon Crystals: 100", (1080, 15), size=(240,30), font_size=20, bg=(176,185,186))

        self.buildmenu = ToggleMenu((1140, 350), size=(100, 400), bg=(176,185,186), shown=False)
        
        self.buildrifleblaster = Button("RB", (1140, 225), self.BRB, size=(60,30), font_size=15, bg=(109,177,255))
        self.buildhorserifleblaster = Button("HRB", (1140, 425), self.BHRB, size=(60,30), font_size=15, bg=(109, 177, 255))
        self.buildspaceraider = Button("SR", (1140, 175), self.BSR, size = (60,30), font_size  = 15, bg = (109, 177, 255))
        self.buildtank = Button("TANK", (1140, 275), self.BTANK, size =(60,30), font_size = 15, bg = (109, 177, 255))
        self.buildplane = Button("PLANE", (1140, 325), self.BPLANE, size = (60,30), font_size = 15, bg = (109, 177, 255))
        self.buildturret = Button("TRT", (1140, 375), self.BTRT, size = (60,30), font_size = 15, bg = (109, 177, 255))

        
        self.buildmenutoggle = False

        self.buildqueue = StatBar(" ", (1090, 635), size=(200, 20), bg=(176, 185, 186), fg=(109, 177, 255))

        self.buildmenu.AddButton(self.buildhorserifleblaster)
        self.buildmenu.AddButton(self.buildrifleblaster)
        self.buildmenu.AddButton(self.buildspaceraider)
        self.buildmenu.AddButton(self.buildtank)
        self.buildmenu.AddButton(self.buildplane)
        self.buildmenu.AddButton(self.buildturret)

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

            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                self.offset = self.offset + 50
                Camera.SetCameraOffset(self.offset, 0)

            elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                self.offset = self.offset - 50
                Camera.SetCameraOffset(self.offset, 0)

            elif event.type == pygame.MOUSEBUTTONDOWN:

                if self.attackbutton.IsClicked(mousepos):
                    self.attackbutton.call_back_()

                if self.defendbutton.IsClicked(mousepos):
                    self.defendbutton.call_back_()

                if self.holdbutton.IsClicked(mousepos):
                    self.holdbutton.call_back_()

                if self.buildhorserifleblaster.IsClicked(mousepos):
                    self.buildhorserifleblaster.call_back_()

                if self.buildspaceraider.IsClicked(mousepos):
                    self.buildspaceraider.call_back_()

                if self.buildtank.IsClicked(mousepos):
                    self.buildtank.call_back_()

                if self.buildplane.IsClicked(mousepos):
                    self.buildplane.call_back_()

                if self.buildturret.IsClicked(mousepos):
                    self.buildturret.call_back_()

                if self.buildrifleblaster.IsClicked(mousepos):
                    self.buildrifleblaster.call_back_()

                if self.openmenu.IsClicked(mousepos):
                    self.buildmenutoggle = not self.buildmenutoggle
                    self.buildmenu.ToggleMenu(self.buildmenutoggle)

                

    def Update(self):

        self.cu = UnitLoader.GetCreatedUnits()
        self.ce = UnitSpawner.GetCreatedUnits()

        # Move all the units based on the current movement mode
        self.UnitMovement.MoveUnits()
        UnitLoader.BuildUnitsInQueue(self.buildqueue)

        # Call the AI
        self.AI.AIUpdate()

        # Move all spawned enemy units
        if(self.counter == 25):
            self.UnitMovement.MoveEnemyUnits()

            if (random.randint(0, 500) <= 15):
                UnitSpawner.EnqueueUnit(UnitSpawner.GetUnitByUnitClass("Rifle Blaster"))

            self.counter = 0
        else:
            self.counter = self.counter + 1


        UnitSpawner.BuildUnitsInQueue()

    def Render(self, screen):
        screen.fill((0, 0, 0))

        screen.blit(GetImage("./Images/MoonBG1.jpg"), (0, 0))

        # Draw all created units on screen
        for unit in self.cu:
           screen.blit(GetImage(unit.imagepath), (unit.xpos - Camera.GetXOffset(), unit.ypos))

        for unit in self.ce:
            screen.blit(GetImage(unit.imagepath), (unit.xpos - Camera.GetXOffset(), unit.ypos))
            
        # Draw the GUI
        self.attackbutton.Draw(screen)
        self.holdbutton.Draw(screen)
        self.defendbutton.Draw(screen)
        self.resourcebar.Draw(screen)
        self.resourcebar.Draw(screen)
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

    def BSR(self):
        unit = UnitLoader.GetUnitByUnitClass("Space Raider")
        unit.laneid = 1

        UnitLoader.EnqueueUnit(unit)

    def BTANK(self):
        unit = UnitLoader.GetUnitByUnitClass("Space Tank")
        unit.laneid = 1

        UnitLoader.EnqueueUnit(unit)

    def BPLANE(self):
        unit = UnitLoader.GetUnitByUnitClass("Space Plane")
        unit.laneid = 1

        UnitLoader.EnqueueUnit(unit)

    def BTRT(self):
        unit = UnitLoader.GetUnitByUnitClass("Space Turret")
        unit.laneid = 1

        UnitLoader.EnqueueUnit(unit)

        
