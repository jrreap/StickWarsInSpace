import pygame
import random
from UpgradeDataBullshit.UpgradeData import UpgradeData

class EconomyUpgrade():

    def __init__(self):
        print("fuck the upgrade system")
        global economy
        economy = 1
        global economy

    def seteconomy(self):#setter
        global economy
        economy = economy + .1
        print("over here")
        print(economy)
        
        
    def returneconomy(self): # getter
        print("and here")
        return economy


    
    
    
