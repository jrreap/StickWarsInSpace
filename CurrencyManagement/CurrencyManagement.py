# Main class to handle currency management for the player
# All costs are based on unit costs and their unit profit values, respectively

# All costs and resources should be managed through this class

class CurrencyManagement:

    mooncrystals = 100

    @classmethod
    # Returns true if the purchase was a success, false if it failed
    # Takes a unit as the input
    def PurchaseUnit(cls, unit):
        if cls.mooncrystals - unit.unitcost >= 0:
            cls.mooncrystals = cls.mooncrystals - unit.unitcost
            return True
        else:
            return False

    @classmethod
    # Added the specified amount of crystals to the player's bank
    def AddMoonCrystals(cls, amount):
        cls.mooncrystals = cls.mooncrystals + amount

    @classmethod
    # Removed the specified amount of crystals from the player's bank
    def RemoveMoonCrystals(cls, amount):
        cls.mooncrystals = cls.mooncrystals - amount

    @classmethod
    # Returns the current amount of moon crystals in the bank
    def GetMoonCrystals(cls):
        return cls.mooncrystals





