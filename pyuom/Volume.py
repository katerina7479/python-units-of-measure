from PhysicalQuantity import PhysicalQuantity
from UnitOfMeasure import UnitOfMeasure


class Volume(PhysicalQuantity):

    def __init__(self, value, unit):
        super(Volume, self).__init__(value, unit)

        # Cubic meter
        new_unit = UnitOfMeasure(
            'm^3',
            lambda x: x,
            lambda y: y
        )
        new_unit.addAlias('m³')
        new_unit.addAlias('cubic meter')
        new_unit.addAlias('cubic meters')
        self.registerUnitOfMeasure(new_unit)

        # Cubic millimeter
        new_unit = UnitOfMeasure(
            'mm^3',
            lambda x: x / 1e-9,
            lambda y: y * 1e-9
        )
        new_unit.addAlias('mm³')
        new_unit.addAlias('cubic millimeter')
        new_unit.addAlias('cubic millimeters')
        self.registerUnitOfMeasure(new_unit)

        # Cubic centimeter
        new_unit = UnitOfMeasure(
            'cm^3',
            lambda x: x / 1e-6,
            lambda y: y * 1e-6
        )
        new_unit.addAlias('cm³')
        new_unit.addAlias('cubic centimeter')
        new_unit.addAlias('cubic centimeters')
        self.registerUnitOfMeasure(new_unit)

        # Cubic decimeter
        new_unit = UnitOfMeasure(
            'dm^3',
            lambda x: x / 1e-3,
            lambda y: y * 1e-3
        )
        new_unit.addAlias('dm³')
        new_unit.addAlias('cubic decimeter')
        new_unit.addAlias('cubic decimeters')
        self.registerUnitOfMeasure(new_unit)

        # Cubic kilometer
        new_unit = UnitOfMeasure(
            'km^3',
            lambda x: x / 1e9,
            lambda y: y * 1e9
        )
        new_unit.addAlias('km³')
        new_unit.addAlias('cubic kilometer')
        new_unit.addAlias('cubic kilometers')
        self.registerUnitOfMeasure(new_unit)

        # Cubic foot
        new_unit = UnitOfMeasure(
            'ft^3',
            lambda x: x / 2.831685e-2,
            lambda y: y * 2.831685e-2
        )
        new_unit.addAlias('ft³')
        new_unit.addAlias('cubic foot')
        new_unit.addAlias('cubic feet')
        self.registerUnitOfMeasure(new_unit)

        # Cubic inch
        new_unit = UnitOfMeasure(
            'in^3',
            lambda x: x / 1.638706e-5,
            lambda y: y * 1.638706e-5
        )
        new_unit.addAlias('in³')
        new_unit.addAlias('cubic inch')
        new_unit.addAlias('cubic inches')
        self.registerUnitOfMeasure(new_unit)

        # Cubic yard
        new_unit = UnitOfMeasure(
            'yd^3',
            lambda x: x / 7.645549e-1,
            lambda y: y * 7.645549e-1
        )
        new_unit.addAlias('yd³')
        new_unit.addAlias('cubic yard')
        new_unit.addAlias('cubic yards')
        self.registerUnitOfMeasure(new_unit)

        # Milliliters
        new_unit = UnitOfMeasure(
            'ml',
            lambda x: x / 1e-6,
            lambda y: y * 1e-6
        )
        new_unit.addAlias('milliliter')
        new_unit.addAlias('milliliters')
        self.registerUnitOfMeasure(new_unit)

        # Centiliters
        new_unit = UnitOfMeasure(
            'cl',
            lambda x: x / 1e-5,
            lambda y: y * 1e-5
        )
        new_unit.addAlias('centiliter')
        new_unit.addAlias('centiliters')
        self.registerUnitOfMeasure(new_unit)

        # Deciliter
        new_unit = UnitOfMeasure(
            'dl',
            lambda x: x / 1e-4,
            lambda y: y * 1e-4
        )
        new_unit.addAlias('deciliter')
        new_unit.addAlias('deciliters')
        self.registerUnitOfMeasure(new_unit)

        # Liter
        new_unit = UnitOfMeasure(
            'l',
            lambda x: x / 1e-3,
            lambda y: y * 1e-3
        )
        new_unit.addAlias('liter')
        new_unit.addAlias('liters')
        self.registerUnitOfMeasure(new_unit)

        # Decaliter
        new_unit = UnitOfMeasure(
            'dal',
            lambda x: x / 1e-2,
            lambda y: y * 1e-2
        )
        new_unit.addAlias('decaliter')
        new_unit.addAlias('decaliters')
        self.registerUnitOfMeasure(new_unit)

        # Hectoliter
        new_unit = UnitOfMeasure(
            'hl',
            lambda x: x / 1e-1,
            lambda y: y * 1e-1
        )
        new_unit.addAlias('hectoliter')
        new_unit.addAlias('hectoliters')
        self.registerUnitOfMeasure(new_unit)

        # Cup
        new_unit = UnitOfMeasure(
            'cup',
            lambda x: x / 2.365882e-4,
            lambda y: y * 2.365882e-4
        )
        new_unit.addAlias('cup')
        new_unit.addAlias('cups')
        self.registerUnitOfMeasure(new_unit)
