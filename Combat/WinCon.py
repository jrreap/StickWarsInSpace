import pygame
from Scenes import*
from UnitManagement import*
from UnitManagement.UnitLoader import UnitLoader

class WinCon():
    @classmethod
    def AttackPlayer(cls, CurrentHealth, UnitHealth):
        PlayerHealth = CurrentHealth - UnitHealth
        print PlayerHealth
        print "playerhealth"
        if(PlayerHealth<=0):
            WinCon.WinLevel()
        variable = PlayerHealth
        return variable
    @classmethod
    def ReachedPlayer(cls, units, base, CurrentHealth=5000):
        x = 0
        BaseHealth = CurrentHealth
        if(base == 1):
            basePos = 0
        if(base == 0):
            basePos = 3531
        while(x<len(units)):
            CurrentUnit = units[x]
            x = x+1
            UnitRange = CurrentUnit.unitrange
            if (CurrentUnit.xpos-basePos)<=0:
                Health = WinCon.AttackPlayer(BaseHealth, CurrentUnit.health)
                UnitLoader.DeleteUnit(CurrentUnit)
                x = len(units) + 1
                return Health
                
    @classmethod
    def WinLevel(cls):
        print "Congrats you have won"
        #self.SwitchToScene("Scenes.MenuScene.MenuScene")


