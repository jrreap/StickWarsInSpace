import pygame
from UnitManagement.Unit import Unit

class Turret (Unit):

   def __init__(self, uid):
        unitclass = "Space Turret"
        damage = 50
        speed = 0
        health = 500
        unitcost = 500
        buildtime = 5
        attackrate = .5
        unitrange = 10
        Unit.__init__(self, unitclass, uid, damage, speed, health, unitcost, buildtime, attackrate, unitrange)
