

class PhysicalQuantity(object):
    def __init__(self, value, unit):
        self._original_value = value
        self._original_unit = unit
        self._unit_definitions = []

    def _toString(self):
        self._original_unit = self.findUnitOfMeasureByNameOrAlias(self._original_unit)
        canonical_unit_name = self._original_unit.getName()

        return "%s %s" % (self._original_value, canonical_unit_name)

    def registerUnitOfMeasure(self, unit):
        self._unit_definitions.append(unit)

    def toUnit(self, unit):
        self._original_unit = self.findUnitOfMeasureByNameOrAlias(self._original_unit)
        self._native_unit_value = self._original_unit.convertValueToNativeUnitOfMeasure(self._original_value)

        to_unit = self.findUnitOfMeasureByNameOrAlias(unit)
        to_unit_value = to_unit.convertValueFromNativeUnitOfMeasure(self._native_unit_value)

        return to_unit_value, to_unit

    def add(self, quantity):
        if type(quantity) is type(self):
            new_value = self._original_value + quantity._original_value
            return (new_value, self._original_unit)
        else:
            raise Exception("PhysicalQuantityMismatch", "Cannot add type (%s) to type (%s)" % (type(quantity), type(self)))

    def subtract(self, quantity):
        if type(quantity) is type(self):
            new_value = self._original_value - quantity._original_value
            return (new_value, self._original_unit)
        else:
            raise Exception("PhysicalQuantityMismatch", "Cannot subtract type (%s) from type (%s)" % (type(quantity), type(self)))

    def findUnitOfMeasureByNameOrAlias(self, unit):
        for unit_of_measure in self._unit_definitions:
            if (unit is unit_of_measure.getName()) or (unit_of_measure.isAliasOf(unit) is True):
                return unit_of_measure
            else:
                pass
        raise Exception('UnknownUnitOfMeasure', unit)
