from PhysicalQuantity import PhysicalQuantity
from UnitOfMeasure import UnitOfMeasure


class Velocity(PhysicalQuantity):
    def __init__(self, value, unit):
        super(Velocity, self).__init__(value, unit)

        # meter per second
        new_unit = UnitOfMeasure(
            'm/s',
            lambda x: x,
            lambda y: y
        )
        new_unit.addAlias('meters per second')
        new_unit.addAlias('meter per second')
        self.registerUnitOfMeasure(new_unit)
