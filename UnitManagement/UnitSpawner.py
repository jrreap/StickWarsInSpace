# Utility class that manages the loading of Unit information and the various components
# to be used in the rendering of the units on screen and the various functionality behind it
# PLEASE NOTE that all build times are in multiples of 50 frames. So a build time of 2
# will take 100 frames to finish... this generally makes the times work out
from UnitManagement.LaneManager import LaneManager
from CurrencyManagement.CurrencyManagement import CurrencyManagement

class UnitSpawner():

    units = {}
    currentUnit = None
    buildCount = 0
    createdUnits = []
    queuedUnits = []
    lane = 0

    @classmethod
    def __init__(cls):
        file = open('UnitManagement/Units.txt')
        for j in range(0,4):
            stats = []
            name = file.readline()[:-1]
            print name
            for i in [3,7,6,12,6,6,14]:
                stats.append(float(file.readline()[i:-1]))
            stats.append(file.readline()[13:-1])
            cls.units[name] = stats
            print stats
            file.readline()

    # Method that is called every frame to check if a unit needs to be constructed
    # If so it starts constructing it each frame until the queue is empty
    @classmethod
    def BuildUnitsInQueue(cls):
        if cls.currentUnit is None:
            if len(cls.queuedUnits) > 0:
                cls.currentUnit = cls.queuedUnits.pop()
        else:
            if cls.currentUnit.buildtime * 50 == cls.buildCount:
                cls.InstantiateUnit(cls.currentUnit)

                # Reset working variables
                cls.buildCount = 0
                cls.currentUnit = None
            else:
                cls.buildCount += 1

    # Enqueues the designated unit into the build system to be built
    @classmethod
    def EnqueueUnit(cls, unit):
        if cls.lane > 2:
            cls.lane = 1
        else:
            cls.lane = cls.lane + 1
        unit.laneid = cls.lane        
        cls.queuedUnits.append(unit)

    # Instantiates a Unit and displays it to the screen
    @classmethod
    def InstantiateUnit(cls, unit):

        # Set starting position to be in the main lane
        unit.xpos = 3000 - (20*unit.laneid)
        unit.ypos = 550 - (50*unit.laneid)

        cls.createdUnits.append(unit)

        LaneManager.AddUnitToLane(unit, unit.laneid)

    # Removes a Unit from the array of currently created units
    @classmethod
    def DeleteUnit(cls, unit):
        cls.createdUnits.remove(unit)
        LaneManager.RemoveUnitFromLane(unit, unit.laneid)

    @classmethod
    def GetCreatedUnits(cls):
        return cls.createdUnits
