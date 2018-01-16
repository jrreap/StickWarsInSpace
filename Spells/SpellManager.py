from UnitManagement.UnitLoader import UnitLoader

# Main class responsible for handling all of the spells and spell related functions

class SpellManager():

    energy = 0
    regenrate = 1

    @classmethod
    def CastDamageSpell(cls, laneid):
        if (cls.energy - 25) >= 0:
            for unit in UnitLoader.GetCreatedUnits():
                if unit.laneid == laneid:
                    unit.health = unit.health - 10

    @classmethod
    def RegenerateEnergy(cls):
        pass