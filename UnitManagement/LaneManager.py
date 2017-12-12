import pygame

class LaneManager():

    lane1 = []
    lane2 = []
    lane3 = []

    @classmethod
    def AddUnitToLane(cls, unit, unitlane=1):
        if unitlane == 1:
            cls.lane1.append(unit)
        elif unitlane == 2:
            cls.lane2.append(unit)
        elif unitlane == 3:
            cls.lane3.append(unit)
        else:
            print("[ERROR] That is not a valid lane id!")

    @classmethod
    def RemoveUnitFromLane(cls, unit, unitlane):
        if unitlane == 1:
            cls.lane1.remove(unit)
        elif unitlane == 2:
            cls.lane2.remove(unit)
        elif unitlane == 3:
            cls.lane3.remove(unit)
        else:
            print("[ERROR] That is not a valid lane id!")