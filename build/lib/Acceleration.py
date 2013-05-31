from PhysicalQuantity import PhysicalQuantity
from UnitOfMeasure import UnitOfMeasure


class Acceleration(PhysicalQuantity):

    def __init__(self, value, unit):
        super(Acceleration, self).__init__(value, unit)

        # meters per second squared
        new_unit = UnitOfMeasure(
            'm/s^2',
            lambda x: x,
            lambda y: y)
        new_unit.addAlias('meters per second squared')
        self.registerUnitOfMeasure(new_unit)
