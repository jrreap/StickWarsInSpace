from UnitManagement.HorseRifleBlaster import HorseRifleBlaster
from UnitManagement.Plane import Plane
from UnitManagement.RifleBlaster import RifleBlaster
from UnitManagement.SpaceRaider import SpaceRaider
from UnitManagement.Tank import Tank
from UnitManagement.Turret import Turret

# Utility class that manages the loading of Unit information and the various components
# to be used in the rendering of the unit on screen and the various functionality behind it

class UnitLoader():

    global CreatedUnits
    global QueuedUnits
    currentunit = None
    buildcount = 0
    unitgen = 0
    CreatedUnits = []
    QueuedUnits = []

    # Method that is called every frame to check if a unit needs to be constructed
    # If so it starts constructing it each frame until the queue is empty
    @classmethod
    def BuildUnitsInQueue(cls, statbar):

        if QueuedUnits.count() > 0:
            if cls.currentunit == None:
                cls.currentunit == QueuedUnits.pop()

            if cls.currentunit.buildtime == cls.buildcount:
                cls.unitgen += 1
                cls.InstantiateUnit(cls.currentunit, cls.unitgen)
            else:
                cls.buildcount += 1
                statbar.SetFillPercentage(cls.buildcount, cls.currentunit.buildtime)



    # Searches through all the created units and returns a created unit by it's ID
    @staticmethod
    def GetCreatedUnitByUnitID(unitid):
        for x in CreatedUnits:
            if x.unitid == unitid:
                return x

        return None

    # Searches through all the units types and returns an instance of the unit by class
    @staticmethod
    def GetUnitByUnitClass(unitclass):
        UnitList = [Plane(0), HorseRifleBlaster(0), RifleBlaster(0), SpaceRaider(0), Tank(0), Turret(0)]

        for x in UnitList:
            print("Searching for " + unitclass + " against " + x.unitclass)
            if x.unitclass == unitclass:
                return x

        return None


    # Instantiates a Unit and displays it to the screen
    @staticmethod
    def InstantiateUnit(unit, uid):

        unit.unitid = uid

        # Set starting position to be in the main lane
        unit.xpos = 15
        unit.ypos = 500

        CreatedUnits.append(unit)

    # Removes a Unit from the array of currently created units
    @staticmethod
    def DeleteUnit(unit):

         for x in CreatedUnits:
             if unit.unitid == x.unitid:
                 CreatedUnits.remove(x)

    # Returns the list of all currently existing units
    @staticmethod
    def GetCreatedUnits():
        return CreatedUnits