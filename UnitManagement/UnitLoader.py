from UnitManagement.LaneManager import LaneManager
from CurrencyManagement.CurrencyManagement import CurrencyManagement

class UnitLoader():

    units = {}
    createdUnits = []
    queuedUnits = []
    currentUnit = None
    buildCount = 0
    lane = 0
    
    @classmethod
    def __init__(cls):
        file = open('UnitManagement/Units.txt')
        while file.readline()[:1] != "#":
            stats = []
            name = file.readline()[:-1]
            print name
            stats.append(file.readline()[17:-1])
            for i in range(1,12):
                line = file.readline()
                stats.append(float(line[line.find("=")+1:-1]))
            cls.units[name] = stats
            print stats
    
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
        if CurrencyManagement.GetMoonCrystals() - unit.unitcost >= 0:
            if len(cls.createdUnits)+len(cls.queuedUnits) < 40:

                if cls.lane > 2:
                    cls.lane = 1
                else:
                    cls.lane = cls.lane + 1

                unit.laneid = cls.lane
                CurrencyManagement.PurchaseUnit(unit)
                cls.queuedUnits.append(unit)
            else:
                print("Max unit count reached!")
   
    @classmethod
    def InstantiateUnit(cls,unit):
        # Set starting position to be in the main lane
        unit.xpos = 150 + (20*unit.laneid)
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

    @classmethod
    def GetUsedSupply(cls):
        return len(cls.createdUnits) + len(cls.queuedUnits)
