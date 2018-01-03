import random
from UnitManagement.UnitSpawner import UnitSpawner
from UnitManagement.UnitLoader import UnitLoader
from UnitManagement.Unit import Unit

# The base AI class for all enemy "players"
class BaseAI():

    # Income variables
    mooncrystals = 500
    income = 1

    # Used to calculate the current "danger" posed to the AI and when it should drain its resources
    dangervalue = 0

    # Used to make sure the AI doesn't just build endless units
    cooldown = 0
    pausetime = 1000
    x = 0
    isPaused = False

    # Unit variables
    UnlockedUnits = ["RifleBlaster"]

    # Difficulty variables
    difficulty = 1

    def __init__(self, difficulty):
        self.difficulty = difficulty
        print("AI Instantiated Successfully")

    def AIUpdate(self):
        if random.randint(1, (1000 / self.difficulty)) <= 50:
            self.AddIncome()

        self.CalculateDangerValue()

        if self.cooldown >= 3:
            self.isPaused = True
            self.cooldown = self.cooldown - 3

        if self.isPaused:
            if self.x == 0:
                self.isPaused = False
                self.x = 0
            else:
                self.x = self.x + 1

        if self.mooncrystals > 0 and self.dangervalue >= 1 and not self.isPaused:
            self.BuildUnit()

    # AI decision methods

    def CalculateDangerValue(self):
        count = 0
        countai = 0
        for unit in UnitLoader.GetCreatedUnits():
            count = count + 1

        for unit in UnitSpawner.GetCreatedUnits():
            countai = countai + 1

        val = count - countai

        if val <= 0:
            self.dangervalue = 0
        elif val <= 5:
            self.dangervalue = 1
        elif val <= 10:
            self.dangervalue = 2
        elif val <= 20:
            self.dangervalue = 3
        elif val <= 25:
            self.dangervalue = 4
        else:
            self.dangervalue = 5


    # Unit construction methods

    def BuildUnit(self):
        randtemp = random.randint(0,len(self.UnlockedUnits)-1)
        unit = Unit(UnitSpawner.units['RifleBlaster'], "RifleBlaster")

        self.cooldown = self.cooldown + 1

        if (self.mooncrystals - unit.unitcost) >= 0:
            self.RemoveMoonCrystals(unit.unitcost)
            UnitSpawner.EnqueueUnit(unit)


    # Income methods

    def AddIncome(self):
        self.mooncrystals = self.mooncrystals + self.income

    def RemoveMoonCrystals(self, amount):
        self.mooncrystals = self.mooncrystals - amount

    def AddMoonCrystals(self, amount):
        self.mooncrystals = self.mooncrystals + amount
