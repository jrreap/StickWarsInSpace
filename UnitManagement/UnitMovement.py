from UnitManagement.UnitLoader import UnitLoader

# Main class that handles all Unit movement within the game

class UnitMovement:

    def __init__(self):
        self.uloader = UnitLoader()
        self.movementmode = "H"

    # H = Hold, A = Attack and D = Defend
    def SetMovementMode(self, mode):
        self.movementmode = mode

    # Moves all the units one "frame" based on the movement mode
    def MoveUnits(self):
        if self.movementmode == "H":
            pass
        elif self.movementmode == "A":
            pass



