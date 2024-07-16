class Decimal:

    @staticmethod
    def add(nb1, nb2):
        p1 = Decimal.__getPow10(nb1)
        p2 = Decimal.__getPow10(nb2)
        pMax = max(p1, p2)
        return float(int(nb1 * pMax) + int(nb2 * pMax)) / pMax

    @staticmethod
    def __getPow10(number: float):
        string = str('{:.16f}'.format(float(number))).rstrip("0")
        indexDot = string.index(".")
        return 10 ** (len(string) - 1 - indexDot)

    @staticmethod
    def times(nb1, nb2):
        p1 = Decimal.__getPow10(nb1)
        p2 = Decimal.__getPow10(nb2)
        return float(int(nb1 * p1) * int(nb2 * p2)) / (p1 * p2)

    @staticmethod
    def divide(nb1, nb2):
        p1 = Decimal.__getPow10(nb1)
        p2 = Decimal.__getPow10(nb2)
        pMax = max(p1, p2)
        return float(int(nb1 * pMax) / int(nb2 * pMax))

    @staticmethod
    def minus(nb1, nb2):
        p1 = Decimal.__getPow10(nb1)
        p2 = Decimal.__getPow10(nb2)
        pMax = max(p1, p2)
        return float(int(nb1 * pMax) - int(nb2 * pMax)) / pMax
    
    @staticmethod
    def modulo(nb1, nb2):
        entDiv = int(Decimal.divide(nb1, nb2))
        quot = Decimal.times(entDiv, nb2)
        return Decimal.minus(nb1, quot)

def main():
    pass


if __name__ == "__main__":
    main()
