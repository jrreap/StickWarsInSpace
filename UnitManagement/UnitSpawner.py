# Utility class that manages the loading of Unit information and the various components
# to be used in the rendering of the units on screen and the various functionality behind it
# PLEASE NOTE that all build times are in multiples of 50 frames. So a build time of 2
# will take 100 frames to finish... this generally makes the times work out

class UnitSpawner():

    units = {}
    currentunit = None
    buildcount = 0
    createdUnits = []
    queuedUnits = []

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

        if cls.currentunit is None:
            if len(cls.queuedUnits) > 0:
                cls.currentunit = cls.queuedUnits.pop()
        else:
            if cls.currentunit.buildtime * 50 == cls.buildcount:
                cls.InstantiateUnit(cls.currentunit)

                # Reset working variables
                cls.buildcount = 0
                cls.currentunit = None
            else:
                cls.buildcount = cls.buildcount + 1

    # Enqueues the designated unit into the build system to be built
    @classmethod
    def EnqueueUnit(cls, unit):
        cls.queuedUnits.append(unit)

    # Instantiates a Unit and displays it to the screen
    @classmethod
    def InstantiateUnit(cls, unit):

        # Set starting position to be in the main lane
        unit.xpos = 3000
        unit.ypos = 500

        cls.createdUnits.append(unit)

    # Removes a Unit from the array of currently created units
    @classmethod
    def DeleteUnit(cls, unit):
        cls.createdUnits.remove(unit)

    @classmethod
    def GetCreatedUnits(cls):
        return cls.createdUnits
