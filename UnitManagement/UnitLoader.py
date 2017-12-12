from UnitManagement.LaneManager import LaneManager

class UnitLoader():

    units = {}
    createdUnits = []
    queuedUnits = []
    currentUnit = None
    buildCount = 0
    
    @classmethod
    def __init__(cls):
        file = open('UnitManagement/Units.txt')
        for j in range(0,6):
            stats = []
            name = file.readline()[:-1]
            print name
            for i in [3,7,6,12,6,6,14]:
                stats.append(float(file.readline()[i:-1]))
            cls.units[name] = stats
            print stats
            file.readline()
    
    @classmethod
    def BuildUnitsInQueue(cls, statbar):
        if cls.currentUnit is None:
            if len(cls.queuedUnits) > 0:
                cls.currentUnit = cls.queuedUnits.pop()
        else:
            if cls.currentUnit.buildtime * 50 == cls.buildCount:
                cls.InstantiateUnit(cls.currentUnit)

                # Reset working variables
                cls.buildCount = 0
                cls.currentUnit = None
                statbar.SetFillPercentage(0, 100)
            else:
                cls.buildCount += 1
                statbar.SetFillPercentage(cls.buildCount, cls.currentUnit.buildtime * 50)

    @classmethod
    def EnqueueUnit(cls, unit):
        if len(cls.createdUnits)+len(cls.queuedUnits) < 10:
            cls.queuedUnits.append(unit)
        else:
            print("Max unit count reached!")
   
    @classmethod
    def InstantiateUnit(cls,unit,lane = 0):
        # Set starting position to be in the main lane
        if unit.laneid >= 2:
            lane = 0
        unit.laneid = lane + 1
        unit.xpos = 15
        unit.ypos = 500

        cls.createdUnits.append(unit)

        # Create in lane
        LaneManager.AddUnitToLane(unit, lane)

    # Removes a Unit from the array of currently created units
    @classmethod
    def DeleteUnit(cls, unit):
        cls.createdUnits.remove(unit)

        # Now remove it from the lane
        LaneManager.RemoveUnitFromLane(unit)

    @classmethod
    def GetCreatedUnits(cls):
        return cls.createdUnits

    @classmethod
    def GetUsedSupply(cls):
        return 20
