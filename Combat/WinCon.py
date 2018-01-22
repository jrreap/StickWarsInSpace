import pygame
from Scenes import*
from UnitManagement import*
from UnitManagement.UnitLoader import UnitLoader
from UnitManagement.UnitSpawner import UnitSpawner

class WinCon():
    @classmethod
    def AttackPlayer(cls, CurrentHealth, UnitHealth):
        PlayerHealth = CurrentHealth - UnitHealth
        #print PlayerHealth
        #print "playerhealth"
        if(PlayerHealth<=0):
            WinCon.WinLevel()
        variable = PlayerHealth
        return variable
    @classmethod
    def ReachedPlayer(cls, units, base, CurrentHealth=1000):
        x = 0
        BaseHealth = CurrentHealth
        if(base == 1):
            basePos = 9
        if(base == 0):
            basePos = 3531
        while(x<len(units)):
            CurrentUnit = units[x]
            x = x+1
            UnitRange = CurrentUnit.unitrange
            if abs(CurrentUnit.xpos-basePos)<10:
                Health = WinCon.AttackPlayer(BaseHealth, CurrentUnit.health)
                UnitLoader.DeleteUnit(CurrentUnit)
                x = len(units) + 1
                print Health
                return Health
            else:
                return BaseHealth

    @classmethod
    def ReachedEPlayer(cls, units, base, CurrentHealth=1000):
        x = 0
        BaseHealth = CurrentHealth
        if(base == 1):
            basePos = 9
        if(base == 0):
            basePos = 3531
        while(x<len(units)):
            CurrentUnit = units[x]
            x = x+1
            UnitRange = CurrentUnit.unitrange
            if abs(CurrentUnit.xpos-basePos)<10:
                Health = WinCon.AttackPlayer(BaseHealth, CurrentUnit.health)
                UnitSpawner.DeleteUnit(CurrentUnit)
                x = len(units) + 1
                print Health
                return Health
            else:
                return BaseHealth
        
                
    @classmethod
    def WinLevel(cls):
        print "Congrats you have won"
        #self.SwitchToScene("Scenes.MenuScene.MenuScene")


