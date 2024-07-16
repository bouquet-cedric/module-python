# Decimal

This class is used to compute real result from decimal calcul.
By example, if we wan't to calcule 0.1 + 0.2, we'd like to have 0.3,
but really, we obtain 0.30000000000004.
So, this class allow to be precize computing with pows of 10 and treating only integers.
Then, the result for 0.1 + 0.2 is 0.3.

# Tests

To verify results, tests are presents. For that, it's possible to launch pytest to check calcul.

# Operations

## Plus

- Decimal.plus(0.1, 0.2) => 0.3
- Decimal.plus(0.1, 0.02) => 0.12
- Decimal.plus(0.200, 0.02) => 0.22
- Decimal.plus(1, 2) => 3
- Decimal.plus(1, 0.2) => 1.2
- Decimal.plus(0.000005, 1) => 1.000005

## Minus

- TestDecimal.Operation(5, 3) => 2
- TestDecimal.Operation(3, 4) => -1
- TestDecimal.Operation(3.5, 4) => -0.5
- TestDecimal.Operation(3.5, 0.05) => 3.45
- TestDecimal.Operation(1, 3) => -2
- TestDecimal.Operation(0.1, 0.3) => -0.2
- TestDecimal.Operation(0.1, 0.2) => -0.1
- TestDecimal.Operation(0.3, 0.2) => 0.1
- TestDecimal.Operation(0.8, 9) => -8.2

## Times

- Decimal.times(2, 1.5) => 3
- Decimal.times(3, 4) => 12
- Decimal.times(3.5, 4) => 14
- Decimal.times(3.5, 0.05) => 0.175

## Divide

- Decimal.divide(6, 1.5) => 4
- Decimal.divide(3, 4) => 0.75
- Decimal.divide(3.5, 4) => 0.875
- Decimal.divide(3.5, 0.05) => 70
- Decimal.divide(1, 3) => 0.3333333333333333
- Decimal.divide(0.1, 0.3) => 0.3333333333333333
- Decimal.divide(0.1, 0.2) => 0.5
- Decimal.divide(0.8, 9) => 0.08888888888888889

## Modulo

- Decimal.modulo(6, 1.5) => 0
- Decimal.modulo(3, 2) => 1
- Decimal.modulo(9.5, 2) => 1.5
