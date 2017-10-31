import pygame
from UnitManagement.Unit import Unit

class HorseRifleBlaster (Unit):

    def __init__(self, uid):
        unitclass = "Horse Rifle Blaster"
        damage = 50
        speed = 2
        health = 300
        unitcost = 200
        buildtime = 2
        attackrate = 1
        unitrange = 4
        imagepath = "Images/MongolCav1.jpg"

        Unit.__init__(self, unitclass, uid, damage, speed, health, unitcost, buildtime, attackrate, unitrange)

