from UnitManagement.UnitLoader import UnitLoader
from UnitManagement.UnitSpawner import UnitSpawner

# Main class that handles all Unit movement within the game

class UnitMovement:

    def __init__(self):
        self.movementmode = "H"

    # H = Hold, A = Attack and D = Defend
    def SetMovementMode(self, mode):
        self.movementmode = mode

    # Moves all the units one "frame" based on the movement mode
    def MoveUnits(self):

        # Fetch the latest updated CreatedUnit Database
        self.cu = UnitLoader.GetCreatedUnits()

        if self.movementmode == "H":
            pass
        elif self.movementmode == "A":
            for unit in self.cu:

                if(unit.xpos < 1175):
                    unit.SetPosition(unit.xpos + 5, unit.ypos)

        elif self.movementmode == "D":
            for unit in self.cu:
                if (unit.xpos > 15):
                    unit.SetPosition(unit.xpos - 5, unit.ypos)

        else:
            print("[ERROR] Movement mode code didn't match any of the known values!")
            print("Skipped frame movement")

    # Speical move method that moves all ENEMY units
    def MoveEnemyUnits(self):

        # Fetch the latest updated CreatedEnemies Database
        self.ce = UnitSpawner.GetCreatedUnits()

        for unit in self.ce:
            if (unit.xpos > 15):
                unit.SetPosition(unit.xpos - 5, unit.ypos)





