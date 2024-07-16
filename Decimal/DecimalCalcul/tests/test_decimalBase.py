import unittest
from ..base import Decimal


class TestDecimal(unittest.TestCase):
    @classmethod
    def setup_class(self):
        self.results = []

    class Operation:
        def __init__(self, t1, t2, res, func=None) -> None:
            self.terme1 = t1
            self.terme2 = t2
            self.expectedResult = res
            if func is not None:
                self.func = func

        def setOperator(self, operator: str):
            self.operator = operator

        def setResult(self, result: bool):
            self.result = result

        def __repr__(self) -> str:
            if self.result:
                return f'{self.terme1} {self.operator} {self.terme2} = {self.expectedResult}\u2705'
            else:
                return f'{self.terme1} {self.operator} {self.terme2} = {self.func(self.terme1, self.terme2)} != {self.expectedResult}\u274C'

    def testPrivateMethod(self):
        decs = [
            (0.02, 100), (0.2, 10), (0.0000007, 10_000_000)
        ]
        for (dec, exp) in decs:
            self.assertEqual(exp, Decimal._Decimal__getPow10(dec))
            self.assertTrue(
                (exp * Decimal._Decimal__getPow10(dec)).is_integer())

    def testAddMethod(self):
        operations = [
            TestDecimal.Operation(0.1, 0.2, 0.3),
            TestDecimal.Operation(0.1, 0.02, 0.12),
            TestDecimal.Operation(0.200, 0.02, 0.22),
            TestDecimal.Operation(1, 2, 3),
            TestDecimal.Operation(1, 0.2, 1.2),
            TestDecimal.Operation(0.000005, 1, 1.000005)
        ]
        for o in operations:
            o.setOperator('+')
            o.func = Decimal.add
            try:
                self.assertEqual(
                    o.expectedResult,
                    Decimal.add(o.terme1, o.terme2)
                )
                o.setResult(True)
            except:
                o.setResult(False)
            finally:
                self.results.append(o)

    def testTimesMethod(self):
        operations = [
            TestDecimal.Operation(2, 1.5, 3),
            TestDecimal.Operation(3, 4, 12),
            TestDecimal.Operation(3.5, 4, 14),
            TestDecimal.Operation(3.5, 0.05, 0.175)
        ]
        for o in operations:
            o.setOperator('*')
            o.func = Decimal.times
            try:
                self.assertEqual(
                    o.expectedResult,
                    Decimal.times(o.terme1, o.terme2)
                )
                o.setResult(True)
            except:
                o.setResult(False)
            finally:
                self.results.append(o)

    def testDivideMethod(self):
        operations = [
            TestDecimal.Operation(6, 1.5, 4),
            TestDecimal.Operation(3, 4, 0.75),
            TestDecimal.Operation(3.5, 4, 0.875),
            TestDecimal.Operation(3.5, 0.05, 70),
            TestDecimal.Operation(1, 3, 0.3333333333333333),
            TestDecimal.Operation(0.1, 0.3, 0.3333333333333333),
            TestDecimal.Operation(0.1, 0.2, 0.5),
            TestDecimal.Operation(0.8, 9, 0.08888888888888889),
        ]
        for o in operations:
            o.setOperator('/')
            o.func = Decimal.divide
            try:
                self.assertEqual(
                    o.expectedResult,
                    Decimal.divide(o.terme1, o.terme2)
                )
                o.setResult(True)
            except:
                o.setResult(False)
            finally:
                self.results.append(o)

    def testModuloMethod(self):
        operations = [
            TestDecimal.Operation(6, 1.5, 0),
            TestDecimal.Operation(3, 2, 1),
            TestDecimal.Operation(9.5, 2, 1.5),
        ]
        for o in operations:
            o.setOperator('%')
            o.func = Decimal.modulo
            try:
                self.assertEqual(
                    o.expectedResult,
                    o.func(o.terme1, o.terme2)
                )
                o.setResult(True)
            except:
                o.setResult(False)
            finally:
                self.results.append(o)

    def testMinusMethod(self):
        operations = [
            TestDecimal.Operation(5, 3, 2),
            TestDecimal.Operation(3, 4, -1),
            TestDecimal.Operation(3.5, 4, -0.5),
            TestDecimal.Operation(3.5, 0.05, 3.45),
            TestDecimal.Operation(1, 3, -2),
            TestDecimal.Operation(0.1, 0.3, -0.2),
            TestDecimal.Operation(0.1, 0.2, -0.1),
            TestDecimal.Operation(0.3, 0.2, 0.1),
            TestDecimal.Operation(0.8, 9, -8.2),
        ]
        for o in operations:
            o.setOperator('-')
            o.func = Decimal.minus
            try:
                self.assertEqual(
                    o.expectedResult,
                    Decimal.minus(o.terme1, o.terme2)
                )
                o.setResult(True)
            except:
                o.setResult(False)
            finally:
                self.results.append(o)

    @classmethod
    def teardown_class(self):
        print()
        results = {}
        for op in self.results:
            if op.func in results.keys():
                if op.result:
                    results[op.func]['success'].append(op)
                else:
                    results[op.func]['fail'].append(op)
            else:
                results[op.func] = {'success': [], 'fail': []}
                if op.result:
                    results[op.func]['success'].append(op)
                else:
                    results[op.func]['fail'].append(op)

        for keys in results.keys():
            data = results[keys]
            print(f'\n- Decimal.'+keys.__name__)
            for suc in data['success']:
                print(suc)
            for suc in data['fail']:
                print(suc)


if __name__ == "__main__":
    t = unittest.main()
