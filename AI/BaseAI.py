import random
from UnitManagement.UnitSpawner import UnitSpawner
import pygame

# The base AI class for all enemy "players"
class BaseAI():

    # Income variables
    mooncrystals = 100
    income = 5

    # Unit variables
    UnlockedUnits = ["Space Rifle Blaster"]

    # Difficulty variables
    difficulty = 1

    def __init__(self):
        print("AI Instantiated Successfully")


    def AIUpdate(self):
        if random.randint(1, (1000 / self.difficulty)) <= 50:
            self.AddIncome()

        if self.mooncrystals > 0:
            self.BuildUnit()

    # Unit construction methods

    def BuildUnit(self):
        randtemp = random.randint(0,len(self.UnlockedUnits))
        unit = UnitSpawner.GetUnitByUnitClass(self.UnlockedUnits[randtemp])

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