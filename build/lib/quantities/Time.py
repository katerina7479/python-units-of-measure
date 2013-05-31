from source.PhysicalQuantity import PhysicalQuantity
from source.UnitOfMeasure import UnitOfMeasure


class Time(PhysicalQuantity):

    def __init__(self, value, unit):
        super(Time, self).__init__(value, unit)

        # Second
        new_unit = UnitOfMeasure(
            's',
            lambda x: x,
            lambda y: y
        )
        new_unit.addAlias('second')
        new_unit.addAlias('seconds')
        self.registerUnitOfMeasure(new_unit)
