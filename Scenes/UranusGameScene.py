from SceneBase import SceneBase
from ImageCache.ImageLoader import GetImage
from UnitManagement.UnitLoader import UnitLoader
from UnitManagement.UnitMovement import UnitMovement
from UnitManagement.UnitSpawner import UnitSpawner
from UnitManagement.Unit import Unit
from UnitManagement.LaneManager import LaneManager
from UI.Button import Button
from UI.Bar import Bar
from UI.StatBar import StatBar
from UI.ToggleMenu import ToggleMenu
from Combat.Detect import Detect
from Combat.AttackDefend import AttackDefend
from Combat.WinCon import WinCon
from AI.BaseAI import BaseAI
from Camera import Camera
from Music.Boombox import Boombox
from CurrencyManagement.CurrencyManagement import CurrencyManagement
from Options.Options import Options
import pygame
import random
from Scenes.Levels.Level5Victory import Level5Victory


class UranusGameScene(SceneBase):

    def __init__(self):
        SceneBase.__init__(self)
        UnitLoader.__init__()

        self.counter = 0
        self.AttackRate = 0
        self.EAttackRate = 0
        self.EHealth = 1000
        self.Health = 1000

        self.offset = 0
        self.movecamera = 0
        self.scrollfactor = 25

        self.UnitMovement = UnitMovement()

        if Options.hardcoremode:
            self.AI = BaseAI(6)
        else:
            self.AI = BaseAI(1)

        self.defendbutton = Button("Defend", (60, 635), self.Attack, size=(120, 30), font_size=20, bg=(109, 177, 255))
        self.holdbutton = Button("Hold", (185, 635), self.HoldPosition, size=(120, 30), font_size=20,
                                 bg=(109, 177, 255))
        self.attackbutton = Button("Attack", (310, 635), self.DefendPosition, size=(120, 30), font_size=20,
                                   bg=(109, 177, 255))
        self.openmenu = Button("Build List", (1130, 600), self.Menu, size=(120, 30), font_size=20, bg=(109, 177, 255))

        self.resourcebar = Bar("Moon Crystals: 100", (1080, 15), size=(240, 30), font_size=20, bg=(176, 185, 186))
        self.supplybar = Bar("Units: 0/40", (1080, 45), size=(240, 30), font_size=20, bg=(176, 185, 186))

        self.buildmenu = ToggleMenu((1140, 350), size=(160, 400), bg=(176, 185, 186), shown=False)

        self.buildrifleblaster = Button("RifleBlaster", (1130, 225), self.BRB, size=(120, 30), font_size=15,
                                        bg=(109, 177, 255))
        self.buildhorserifleblaster = Button("HorseRifleBlaster", (1130, 425), self.BHRB, size=(120, 30), font_size=15,
                                             bg=(109, 177, 255))
        self.buildspaceraider = Button("SpaceRaider", (1130, 175), self.BSR, size=(120, 30), font_size=15,
                                       bg=(109, 177, 255))
        self.buildtank = Button("Tank", (1130, 275), self.BTANK, size=(120, 30), font_size=15, bg=(109, 177, 255))
        self.buildplane = Button("Plane", (1130, 325), self.BPLANE, size=(120, 30), font_size=15, bg=(109, 177, 255))
        self.buildturret = Button("Turret", (1130, 375), self.BTRT, size=(120, 30), font_size=15, bg=(109, 177, 255))

        self.buildmenutoggle = False

        self.buildqueue = StatBar(" ", (1090, 635), size=(200, 20), bg=(176, 185, 186), fg=(109, 177, 255))

        self.buildmenu.AddButton(self.buildhorserifleblaster)
        self.buildmenu.AddButton(self.buildrifleblaster)
        self.buildmenu.AddButton(self.buildspaceraider)
        self.buildmenu.AddButton(self.buildtank)
        self.buildmenu.AddButton(self.buildplane)
        self.buildmenu.AddButton(self.buildturret)

        b = Boombox()
        b.PlayMusic("level5playmusic")

    def ProcessInput(self, events, pressed_keys):

        mousepos = pygame.mouse.get_pos()

        for event in events:

            # Keydown events
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.SwitchToScene(None)

                elif event.key == pygame.K_ESCAPE:
                    self.SwitchToScene("Scenes.Levels.Level5Victory.Level5Victory")

                elif event.key == pygame.K_a:
                    self.buildqueue.SetFillPercentage(10, 100)

                elif event.key == pygame.K_b:
                    self.buildmenutoggle = not self.buildmenutoggle
                    self.buildmenu.ToggleMenu(self.buildmenutoggle)
                
                elif event.key == pygame.K_RIGHT:
                    print "downR"
                    if self.movecamera >= 0:
                        self.movecamera += self.scrollfactor

                elif event.key == pygame.K_LEFT:
                    print "downL"
                    if self.movecamera <= 3600:
                        self.movecamera -= self.scrollfactor

                elif event.key == pygame.K_m:
                    CurrencyManagement.AddMoonCrystals(100)
                    
            elif event.type == pygame.KEYUP:
                print "up"
                if event.key == pygame.K_RIGHT:
                    if self.movecamera >= 0:
                        self.movecamera -= self.scrollfactor

                elif event.key == pygame.K_LEFT:
                    if self.movecamera <= 3600:
                        self.movecamera += self.scrollfactor

            # Mouse click events
            elif event.type == pygame.MOUSEBUTTONDOWN:

                if self.attackbutton.IsClicked(mousepos):
                    self.attackbutton.call_back_()

                elif self.defendbutton.IsClicked(mousepos):
                    self.defendbutton.call_back_()

                elif self.holdbutton.IsClicked(mousepos):
                    self.holdbutton.call_back_()

                elif self.buildhorserifleblaster.IsClicked(mousepos):
                    self.buildhorserifleblaster.call_back_()

                elif self.buildspaceraider.IsClicked(mousepos):
                    self.buildspaceraider.call_back_()

                elif self.buildtank.IsClicked(mousepos):
                    self.buildtank.call_back_()

                elif self.buildplane.IsClicked(mousepos):
                    self.buildplane.call_back_()

                elif self.buildturret.IsClicked(mousepos):
                    self.buildturret.call_back_()

                elif self.buildrifleblaster.IsClicked(mousepos):
                    self.buildrifleblaster.call_back_()

                elif self.openmenu.IsClicked(mousepos):
                    self.buildmenutoggle = not self.buildmenutoggle
                    self.buildmenu.ToggleMenu(self.buildmenutoggle)

    def Update(self):
        if self.movecamera != 0:
                self.offset += self.movecamera
                Camera.SetCameraOffset(self.offset, 0)
                
        self.cu = UnitLoader.GetCreatedUnits()
        self.ce = UnitSpawner.GetCreatedUnits()

        # Move all the units based on the current movement mode
        self.UnitMovement.MoveUnits()
        self.UnitMovement.MoveEnemyUnits()
        UnitLoader.BuildUnitsInQueue(self.buildqueue)

        # Move all spawned enemy units
        if(self.counter == 25):
            self.UnitMovement.MoveEnemyUnits()
            if (random.randint(0, 100) <= 5):
                #UnitSpawner.EnqueueUnit(UnitSpawner.units["RifleBlaster"])
                pass
            self.counter = 0
        else:
            self.counter = self.counter + 1

        # Call the AI
        self.AI.AIUpdate()

        # Move all spawned enemy units
        self.UnitMovement.MoveEnemyUnits()

        UnitSpawner.BuildUnitsInQueue()
    
        #You attack
        if(self.AttackRate == 30):
            pass
        # You attack
        if(self.AttackRate == 30):
            UnitSpawner.BuildUnitsInQueue()
        
        # You attack
        if (self.AttackRate == 30):
            AttackDefend.Attack(self.cu, self.ce, self.AttackRate)
            self.AttackRate = 0
        else:
            AttackDefend.Attack(self.cu, self.ce, self.AttackRate)
            self.AttackRate = self.AttackRate + 1

        #Attack Base
        if(self.Health!=1000):
            if(len(self.cu)>0):
                self.Health = WinCon.ReachedPlayer(self.cu, 0, self.Health)
        if(self.Health==1000):
            if(len(self.cu)>0):
                self.Health = WinCon.ReachedPlayer(self.cu, 0)
        if(self.Health<=0):
            print "Congrats you have won"
            self.SwitchToScene("Scenes.Levels.Level5Victory.Level5Victory")
        #self.EHealth = WinCon.ReachedPlayer(self.ce, 1, self.EHealth)
        
        # AI attacks
        #if(self.EAttackRate == 30):

        #self.Health = WinCon.ReachedPlayer(self.cu, 0, self.Health)
            
        # AI attacks
        if (self.EAttackRate == 30):
            AttackDefend.EAttack(self.ce, self.cu, self.EAttackRate)
            self.EAttackRate = 0
        else:
            AttackDefend.EAttack(self.ce, self.cu, self.EAttackRate)
            self.EAttackRate = self.EAttackRate + 1

    def Render(self, screen):
        screen.fill((0, 0, 0))

        screen.blit(GetImage("Images/URANUSHAHAH.jpg"), (0 - Camera.GetXOffset(), 0))

        # Draw your units on screen
        for unit in self.cu:
            topLeft = (unit.xpos - Camera.GetXOffset(), unit.ypos, unit.width, unit.hight)
            bottomRight = (unit.animate.frame, 0, unit.width, unit.hight)
            if (self.UnitMovement.movementmode == "A"):
                unit.animate.nextFrame()
                screen.blit(GetImage(unit.imagepath + "walk.png"), topLeft, bottomRight)
            else:
                unit.animate.prevFrame()
                screen.blit(pygame.transform.flip(GetImage(unit.imagepath + "walk.png"), True, False), topLeft, bottomRight)
        # Draw enemy units on screen
        for unit in self.ce:
            unit.animate.prevFrame()
            topLeft = (unit.xpos - Camera.GetXOffset(), unit.ypos, unit.width, unit.hight)
            bottomRight = (unit.animate.frame, 0, unit.width, unit.hight)
            screen.blit(pygame.transform.flip(GetImage(unit.imagepath + "walk.png"), True, False), topLeft, bottomRight)

        # Draw the GUI
        self.attackbutton.Draw(screen)
        self.holdbutton.Draw(screen)
        self.defendbutton.Draw(screen)

        # Make sure not to update the text unless it has changed
        if "Moon Crystals: " + str(CurrencyManagement.GetMoonCrystals()) != self.resourcebar.txt:
            self.resourcebar.SetText("Moon Crystals: " + str(CurrencyManagement.GetMoonCrystals()))

        if "Units: " + str(UnitLoader.GetUsedSupply()) + "/40" != self.supplybar.txt:
            self.supplybar.SetText("Units: " + str(UnitLoader.GetUsedSupply()) + "/40")

        self.resourcebar.Draw(screen)
        self.supplybar.Draw(screen)

        self.buildqueue.Draw(screen)
        self.buildmenu.Draw(screen)
        self.openmenu.Draw(screen)

    # Cleanup function
    def Terminate(self):
        UnitLoader.createdUnits = []
        UnitLoader.buildCount = 0
        UnitLoader.lane = 0

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
        unit = Unit(UnitLoader.units["RifleBlaster"])

        UnitLoader.EnqueueUnit(unit)

    def BHRB(self):
        unit = Unit(UnitLoader.units["HorseRifleBlaster"])

        UnitLoader.EnqueueUnit(unit)

    def BSR(self):
        unit = Unit(UnitLoader.units["SpaceRaider"])

        UnitLoader.EnqueueUnit(unit)

    def BTANK(self):
        unit = Unit(UnitLoader.units["Tank"])

        UnitLoader.EnqueueUnit(unit)

    def BPLANE(self):
        unit = Unit(UnitLoader.units["Plane"])

        UnitLoader.EnqueueUnit(unit)

    def BTRT(self):
        unit = Unit(UnitLoader.units["Turret"])

        UnitLoader.EnqueueUnit(unit)
