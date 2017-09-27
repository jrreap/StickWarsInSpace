#Main class for managing and adjusting unit and unit information
#Should be linked to every unit on the game screen

class Unit():
    
    unitclass = "Empty"
    unitid = 0
    damage = 0
    speed = 0
    health = 0
    unitcost = 0
    buildtime = 0
    
    def __init__(self, uclass, uid, udamage, uspeed, uhealth, upcost, umbt):
        self.unitclass = uclass
        self.unitid = uid
        self.damage = udamage
        self.speed = uspeed
        self.health = uhealth
        self.unitcost = upcost
        self.buildtime = umbt
        
    def DamageUnit(self, amount):
        self.health = self.health - amount
        
    def HealUnit(self, amount):
        self.health = self.health + amount
