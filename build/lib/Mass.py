from PhysicalQuantity import PhysicalQuantity
from UnitOfMeasure import UnitOfMeasure


class Mass(PhysicalQuantity):

    def __init__(self, value, unit):
        super(Mass, self).__init__(value, unit)

        # Kilogram
        new_unit = UnitOfMeasure(
            'kg',
            lambda x: x,
            lambda y: y
        )

        new_unit.addAlias('kilogram')
        new_unit.addAlias('kilograms')
        self.registerUnitOfMeasure(new_unit)

        # Milligram
        new_unit = UnitOfMeasure(
            'mg',
            lambda x: x / 1e-6,
            lambda y: y * 1e-6
        )
        new_unit.addAlias('milligram')
        new_unit.addAlias('milligrams')
        self.registerUnitOfMeasure(new_unit)

        # Centigram
        new_unit = UnitOfMeasure(
            'cg',
            lambda x: x / 1e-5,
            lambda y: y * 1e-5
        )
        new_unit.addAlias('centigram')
        new_unit.addAlias('centigrams')
        self.registerUnitOfMeasure(new_unit)

        # Gram
        new_unit = UnitOfMeasure(
            'g',
            lambda x: x / 1e-3,
            lambda y: y * 1e-3
        )
        new_unit.addAlias('gram')
        new_unit.addAlias('grams')
        self.registerUnitOfMeasure(new_unit)

        # Tonne (metric)
        new_unit = UnitOfMeasure(
            't',
            lambda x: x / 1e3,
            lambda y: y * 1e3
        )
        new_unit.addAlias('ton')
        new_unit.addAlias('tons')
        new_unit.addAlias('tonne')
        new_unit.addAlias('tonnes')
        self.registerUnitOfMeasure(new_unit)

        # Pound
        new_unit = UnitOfMeasure(
            'lb',
            lambda x: x / 4.535924e-1,
            lambda y: y * 4.535924e-1
        )
        new_unit.addAlias('lbs')
        new_unit.addAlias('pound')
        new_unit.addAlias('pounds')
        self.registerUnitOfMeasure(new_unit)

        # Ounce
        new_unit = UnitOfMeasure(
            'oz',
            lambda x: x / 2.834952e-2,
            lambda y: y * 2.834952e-2
        )
        new_unit.addAlias('ounce')
        new_unit.addAlias('ounces')
        self.registerUnitOfMeasure(new_unit)
