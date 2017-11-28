from UnitManagement import*
from UnitManagement.UnitLoader import UnitLoader
from UnitManagement.UnitSpawner import UnitSpawner
import pygame

##SOME KINKS NEED TO WORKED OUT. I (Addison) WILL DO IT SOON SO PLS DONT FUCK TOO MUCH UP
class AttackDefend():
    @classmethod
    def InRange(cls, Unit1, Unit2):
        detect = False
        UnitRange = Unit1.unitrange
        if Unit2.xpos-Unit1.xpos<=UnitRange/100:
            detect = True
        else:
            detect = False
        return True

    @classmethod
    def Attack(cls, Friendlies, Enemies):
        x = 0
        y = 0
        while(x<len(Friendlies)):
              Unit1 = Friendlies[x]
              x = x+1
              while(y<len(Enemies)):
                  Unit2 = Enemies[y]
                  y = y+1
                  detected = AttackDefend.InRange(Unit1,Unit2)
                  if(Unit2.health>0):
                      Unit1.speed = 0
                      print Unit2.health
                      Unit2.DamageUnit(Unit1.damage)
                      print Unit2.health
                      if Unit2.health<1:
                          UnitSpawner.DeleteUnit(Unit2)
                          Unit1.speed = 2
                      

    
"""@classmethod
    def Attack(cls, Friendlies, Enemies):
        x = 0
        y = 0
        while x<len(Friendlies):
            x = x+1
            Unit1 = Friendlies[x-1]
            print Unit1.attacking
            if(Unit1.attacking == False):
                UnitTarget = None
            while y<len(Enemies):
                y = y+1
                if(Unit1.attacking == False):
                    Unit2 = Enemies[y-1]
                    print Unit2
                    detected = AttackDefend.InRange(Unit1, Unit2)
                if(Unit1.attacking == True):
                    detected = True
                #print detected
                if(detected == True):
                    Unit1.attacking = True
                    UnitTarget = Unit2
                    print Unit2
                if(detected == True and UnitTarget == Unit2):
                    if(Unit2.health >0):
                        Unit1.attacking = True
                        Unit1.speed = 0
                        print Unit2.health
                        print "health"
                        Unit2.health = Unit2.health - Unit1.damage
                        print Unit2.health
                        print "health"
                        if Unit2.health<1:
                            UnitSpawner.DeleteUnit(Unit2)
                            Unit1.speed = 2
                            UnitTarget = None
                            Unit.attacking = False
"""
