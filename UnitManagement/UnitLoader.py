import pygame
from UnitManagement.HorseRifleBlaster import HorseRifleBlaster
from UnitManagement.Plane import Plane
from UnitManagement.RifleBlaster import RifleBlaster
from UnitManagement.SpaceRaider import SpaceRaider
from UnitManagement.Tank import Tank
from UnitManagement.Turret import Turret

# Utility class that manages the loading of Unit information and the various components
# to be used in the rendering of the unit on screen and the various functionality behind it

class UnitLoader():

    def __init__(self):
        self.UnitList = [Plane(), HorseRifleBlaster(), RifleBlaster(), SpaceRaider(), Tank(), Turret()]
        self.CreatedUnits = []

    # Searches through all the units and returns an instance of the unit by class
    def GetUnitByUnitClass(self, unitclass):

        for unit in self.UnitList:
            if unit.unitclass == unitclass:
                return unit
            else:
                print("COULD NOT FIND UNIT WITH CLASS " + unitclass)
                return None

    # Instantiates a Unit and displays it to the screen
    def InstantiateUnit(self, unit):
        self.CreatedUnits.append(unit)

    # Removes a Unit from the array of currently created unitsK
    def DeleteUnit(self, unit):

         for x in self.CreatedUnits:
             if unit.unitid == x.unitid:
                 self.CreatedUnits.remove(x)

    # Returns the list of all currently existing units
    def GetCreatedUnits(self):
        return self.CreatedUnits