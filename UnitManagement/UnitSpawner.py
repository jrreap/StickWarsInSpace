from UnitManagement.LaneManager import LaneManager
from CurrencyManagement.CurrencyManagement import CurrencyManagement

class UnitSpawner():

    units = {}
    createdUnits = []
    queuedUnits = []
    currentUnit = None
    buildCount = 0
    lane = 0
    
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
    
    @classmethod
    def EnqueueUnit(cls, unit):
        if len(cls.createdUnits)+len(cls.queuedUnits) < 40:
            if cls.lane > 2:
                cls.lane = 1
            else:
                cls.lane += 1
        unit.laneid = cls.lane
        cls.queuedUnits.append(unit)
   
    @classmethod
    def InstantiateUnit(cls,unit):
        # Set starting position to be in the main lane
        unit.xpos = 3000 + (20*unit.laneid)
        unit.ypos = 550 - (50*unit.laneid)

        cls.createdUnits.append(unit)

        # Add to lane
        LaneManager.AddUnitToLane(unit, unit.laneid)

    # Removes a Unit from the array of currently created units
    @classmethod
    def DeleteUnit(cls, unit):
        cls.createdUnits.remove(unit)

        # Remove from lane
        LaneManager.RemoveUnitFromLane(unit, unit.laneid)

    @classmethod
    def GetCreatedUnits(cls):
        return cls.createdUnits
