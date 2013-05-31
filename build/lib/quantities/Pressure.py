from source.PhysicalQuantity import PhysicalQuantity
from source.UnitOfMeasure import UnitOfMeasure


class Pressure(PhysicalQuantity):

    def __init__(self, value, unit):
        super(Pressure, self).__init__(value, unit)
        # Pascal
        new_unit = UnitOfMeasure(
            'Pa',
            lambda x: x,
            lambda y: y
        )
        new_unit.addAlias('pascal')
        self.registerUnitOfMeasure(new_unit)

        # Atmosphere
        new_unit = UnitOfMeasure(
            'atm',
            lambda x: x / 101325,
            lambda y: y * 101325
        )
        new_unit.addAlias('atmosphere')
        new_unit.addAlias('atmospheres')
        self.registerUnitOfMeasure(new_unit)

        # Bar
        new_unit = UnitOfMeasure(
            'bar',
            lambda x: x / 1e5,
            lambda y: y * 1e5
        )
        new_unit.addAlias('bar')
        self.registerUnitOfMeasure(new_unit)

        # Inch of Mercury
        new_unit = UnitOfMeasure(
            'inHg',
            lambda x: x / 3.386389e3,
            lambda y: y * 3.386389e3
        )
        new_unit.addAlias('inches of mercury')
        self.registerUnitOfMeasure(new_unit)

        # Milimeter of Mercury
        new_unit = UnitOfMeasure(
            'mmHg',
            lambda x: x / 133.3224,
            lambda y: y * 133.3224
        )
        new_unit.addAlias('milimeters of mercury')
        new_unit.addAlias('torr')
        self.registerUnitOfMeasure(new_unit)

        # Pound per Square Inch
        new_unit = UnitOfMeasure(
            'psi',
            lambda x: x / 6.894757e3,
            lambda y: y * 6.894757e3
        )
        new_unit.addAlias('pounds per square inch')
        self.registerUnitOfMeasure(new_unit)
