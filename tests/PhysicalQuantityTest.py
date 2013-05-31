import unittest
from pyuom.PhysicalQuantity import PhysicalQuantity
from pyuom.UnitOfMeasure import UnitOfMeasure
from pyuom.Angle import Angle


class PhysicalQuantityTest(unittest.TestCase):

    def setUp(self):
        unittest.TestCase.setUp(self)

        self.__class__.PQ = PhysicalQuantity(1.63, "quatloos")
        self.__class__.PQ2 = PhysicalQuantity(4, "doublequat")

        # base
        new_unit = UnitOfMeasure(
            'q',
            lambda x: x,
            lambda y: y)
        new_unit.addAlias('quatloos')
        new_unit.addAlias('quatloo')
        self.__class__.PQ.registerUnitOfMeasure(new_unit)
        self.__class__.PQ2.registerUnitOfMeasure(new_unit)

        # doublequat
        new_unit = UnitOfMeasure(
            'dq',
            lambda x: x / 2.0,
            lambda y: y * 2.0,
        )
        new_unit.addAlias('doublequats')
        new_unit.addAlias('doublequat')
        self.__class__.PQ.registerUnitOfMeasure(new_unit)
        self.__class__.PQ2.registerUnitOfMeasure(new_unit)

       # galimpwid
        new_unit = UnitOfMeasure(
            'glw',
            lambda x: x * 10,
            lambda y: y / 10,
        )
        new_unit.addAlias('galimpwid')
        new_unit.addAlias('galimpwids')
        self.__class__.PQ.registerUnitOfMeasure(new_unit)

    def testName(self):
        result = self.PQ._toString()
        self.assertEqual(result, "1.63 q")

    def testConvertValue(self):
        result = self.PQ.toUnit("doublequats")
        self.assertEqual(result[0], 0.815)

    def testConvertUnit(self):
        temp = self.PQ.toUnit("doublequats")
        result = temp[1].getName()
        self.assertEqual(result, "dq")

    def testConvertValue2(self):
        result = self.PQ.toUnit("galimpwid")
        self.assertEqual(round(result[0], 1), 16.3)

    def testConvertUnit2(self):
        temp = self.PQ.toUnit("galimpwid")
        result = temp[1].getName()
        self.assertEqual(result, "glw")

    def testAdd(self):
        result = self.PQ2.toUnit("q")
        self.assertEqual(result[0], 8.0)
        result = self.PQ.add(self.PQ2)
        self.assertEqual(result[0], 5.63)

    def testSubtract(self):
        self.PQ2.toUnit("q")
        result = self.PQ.subtract(self.PQ2)
        self.assertEqual(round(result[0], 1), -2.4)

    def testAddError(self):
        myangle = Angle(32, "deg")
        self.assertRaises(Exception, self.PQ.add, myangle)

    def testSubtractError(self):
        myangle = Angle(32, "deg")
        self.assertRaises(Exception, self.PQ.subtract, myangle)
