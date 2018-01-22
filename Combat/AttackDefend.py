from UnitManagement import*
from UnitManagement.UnitLoader import UnitLoader
from UnitManagement.UnitSpawner import UnitSpawner
from CurrencyManagement.CurrencyManagement import CurrencyManagement
import pygame

class AttackDefend():
    @classmethod
    def InRange(cls, Unit1, Unit2):
        detect = False
        UnitRange = Unit1.unitrange
        if abs(Unit2.xpos-Unit1.xpos)<=UnitRange*10:
            if(Unit2.ypos == Unit1.ypos):
                detect = True
            else:
                detect = False
        else:
            detect = False
        return detect

    @classmethod
    def Attack(cls, Friendlies, Enemies, EnemyList, Rate, OGSpeed=0, EOGSpeed=0):
        if(Friendlies.speed!=0):
            OGSpeed = Friendlies.speed
        Friendlies.speed = 0
        if((Rate)>29):
            Enemies.DamageUnit(Friendlies.damage)
            if(Enemies.health<1):
                UnitSpawner.DeleteUnit(Enemies)
                CurrencyManagement.AddMoonCrystals(100)

    @classmethod
    def EAttack(cls, Friendlies, Enemies, EnemyList, Rate, OGSpeed=0, EOGSpeed=0):
        if(Friendlies.speed!=0):
            OGSpeed = Friendlies.speed
        Friendlies.speed = 0
        if((Rate)>29):
            Enemies.DamageUnit(Friendlies.damage)
            if(Enemies.health<1):
                UnitLoader.DeleteUnit(Enemies)
                CurrencyManagement.AddMoonCrystals(100)
            
    @classmethod
    def UnitsAttack(cls, Units, Enemies, AttackRate, EAttackRate):
        # You attack
        fe = 0
        fu = 0
        while(fu<len(Units)):
            while(fe<len(Enemies)):
                detect = AttackDefend.InRange(Units[fu], Enemies[fe])
                if(detect==True):
                    AttackDefend.Attack(Units[fu], Enemies[fe], Enemies, AttackRate)
                fe = fe + 1
            fu = fu + 1
        #if AttackRate>30:
         #   AttackRate=0
        #else:
         #   AttackRate += 1

        # AI attacks
        ee = 0
        eu = 0
        while(ee<len(Enemies)):
            while(eu<len(Units)):
                detect = AttackDefend.InRange(Enemies[ee], Units[eu])
                if(detect):
                    AttackDefend.EAttack(Enemies[ee], Units[eu], Units, EAttackRate)
                eu = eu + 1
            ee = ee + 1
      #  if (EAttackRate > 30):
       #     EAttackRate=0
        #else:
         #   EAttackRate += 1

        #Make units move again
        a=0
        b=0
        detect = False
        while(a<len(Enemies)):
            while(b<len(Units)):
                detect = AttackDefend.InRange(Enemies[a], Units[b])
                if(detect):
                    break
                b += 1
            if(detect==False):
                Enemies[a].speed = Enemies[a].OGSpeed
            detect = False
            a += 1
        a=0
        b=0
        while(a<len(Units)):
            while(b<len(Enemies)):
                detect = AttackDefend.InRange(Units[a], Enemies[b])
                if(detect):
                    break
                b += 1
            if(detect==False):
                Units[a].speed = Units[a].OGSpeed
            detect = False
            a += 1
        a=0
        b=0
        if(len(Units)==0):
            while(b<len(Enemies)):
                Enemies[b].speed = Enemies[b].OGSpeed
                b += 1
        if(len(Enemies)==0):
            while(a<len(Units)):
                Units[a].speed = Units[b].OGSpeed
                a += 1
                
        
'''        x = 0
        y = 0
        Rate = AttackRate
        while(x<len(Friendlies)):
              Unit1 = Friendlies[x]
              x = x+1
              y = 0
              while(y<len(Enemies)):
                  Unit2 = Enemies[y]
                  y = y+1
                  detected = AttackDefend.InRange(Unit1,Unit2)
                  if(Unit1.speed!= 0):
                      OGSpeed = Unit1.speed
                  if(Unit2.health>0):
                      if(detected == True):
                          Unit1.speed = 0
                          if(Rate == 30):
                              Unit1.speed = 0
                              Unit2.DamageUnit(Unit1.damage)                         
                              if Unit2.health<1:
                                  Unit2.damage = 0
                                  UnitSpawner.DeleteUnit(Unit2)
                                  CurrencyManagement.AddMoonCrystals(100)
                                  Unit1.speed = OGSpeed
                  if(Unit2.health<1):
                      Unit1.speed = OGSpeed

'''          
'''    @classmethod
    def EAttack(cls, Enemies, Friendlies, EAttackRate, OGSpeed=0):
        x = 0
        y = 0
        ERate = EAttackRate
        while(x<len(Enemies)):
              Unit1 = Enemies[x]
              x = x+1
              y = 0
              while(y<len(Friendlies)):
                  Unit2 = Friendlies[y]
                  y = y+1
                  detected = AttackDefend.InRange(Unit1,Unit2)
                  if(Unit1.speed!= 0):
                      OGSpeed = Unit1.speed
                  if(Unit2.health>0):
                      if(detected == True):
                          Unit1.speed = 0
                          if(ERate == 30):
                              Unit1.speed = 0
                              Unit2.DamageUnit(Unit1.damage)                         
                              if Unit2.health<1:
                                  Unit2.damage = 0
                                  UnitLoader.DeleteUnit(Unit2)
                                  Unit1.speed = OGSpeed
                                  d = 0
                                  s = 0
                                  while(d<len(Enemies)):
                                      while(s<len(Friendlies)):
                                          still = AttackDefend.InRange(Enemies[d], Friendlies[s])
                                          if(still==False):
                                              Enemies[d].speed = OGSpeed
                                          s = s+1
                                      d = d+1
                  if(Unit2.health<1):
                      Unit1.speed = OGSpeed
             

   ''' 
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
