from UnitManagement.HorseRifleBlaster import HorseRifleBlaster
from UnitManagement.Plane import Plane
from UnitManagement.RifleBlaster import RifleBlaster
from UnitManagement.SpaceRaider import SpaceRaider
from UnitManagement.Tank import Tank
from UnitManagement.Turret import Turret

# Utility class that manages the loading of Unit information and the various components
# to be used in the rendering of the unit on screen and the various functionality behind it
# PLEASE NOTE that all build times are in multiples of 100 frames. So a build time of 2
# will take 200 frames to finish... this generally makes the times work out

class UnitLoader():

    currentunit = None
    buildcount = 0
    unitgen = 0
    CreatedUnits = []
    QueuedUnits = []

    # Method that is called every frame to check if a unit needs to be constructed
    # If so it starts constructing it each frame until the queue is empty
    @classmethod
    def BuildUnitsInQueue(cls, statbar):

        print(cls.buildcount)

        if len(cls.QueuedUnits) > 0:
            if cls.currentunit is None:
                cls.currentunit = cls.QueuedUnits[0]

            elif cls.currentunit.buildtime * 100 == cls.buildcount:
                cls.unitgen = cls.unitgen + 1
                cls.InstantiateUnit(cls.currentunit, cls.unitgen)

                # Reset working variables
                cls.buildcount = 0
                cls.currentunit = None
                cls.QueuedUnits.pop()
                statbar.SetFillPercentage(0, 100)

            else:
                cls.buildcount = cls.buildcount + 1
                statbar.SetFillPercentage(cls.buildcount, cls.currentunit.buildtime * 100)



    # Searches through all the created units and returns a created unit by it's ID
    @classmethod
    def GetCreatedUnitByUnitID(cls, unitid):
        for x in cls.CreatedUnits:
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

    # Enqueues the designated unit into the build system to be built
    @classmethod
    def EnqueueUnit(cls, unit):
        cls.QueuedUnits.append(unit)

    # Instantiates a Unit and displays it to the screen
    @classmethod
    def InstantiateUnit(cls, unit, uid):

        unit.unitid = uid

        # Set starting position to be in the main lane
        unit.xpos = 15
        unit.ypos = 500

        cls.CreatedUnits.append(unit)

    # Removes a Unit from the array of currently created units
    @classmethod
    def DeleteUnit(cls, unit):

         for x in cls.CreatedUnits:
             if unit.unitid == x.unitid:
                 cls.CreatedUnits.remove(x)

    # Returns the list of all currently existing units
    @classmethod
    def GetCreatedUnits(cls):
        return cls.CreatedUnits