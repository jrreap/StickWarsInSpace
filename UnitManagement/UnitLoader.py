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
        self.UnitList = [Plane(0), HorseRifleBlaster(0), RifleBlaster(0), SpaceRaider(0), Tank(0), Turret(0)]
        self.CreatedUnits = []
        self.idgen = 1

    # Searches through all the units and returns an instance of the unit by class
    def GetUnitByUnitClass(self, unitclass):

        for x in self.UnitList:
            print("Searching for " + unitclass + " against " + x.unitclass)
            if x.unitclass == unitclass:
                return x

        return None

    # Instantiates a Unit and displays it to the screen
    def InstantiateUnit(self, unit):

        # Generate a unique ID for this unit to reference later
        self.idgen = self.idgen + 1
        unit.unitid = self.idgen

        # Set starting position to be in the main lane
        unit.xpos = 15
        unit.ypos = 500

        self.CreatedUnits.append(unit)

    # Removes a Unit from the array of currently created unitsK
    def DeleteUnit(self, unit):

         for x in self.CreatedUnits:
             if unit.unitid == x.unitid:
                 self.CreatedUnits.remove(x)

    # Returns the list of all currently existing units
    def GetCreatedUnits(self):
        return self.CreatedUnits