from math import sqrt

class Solution:
    def __init__(self, x=None, x1=None, x2=None):
        self.x = x
        self.x1 = x1
        self.x2 = x2

    def __repr__(self):
        if self.x is not None:
            return f"x = {self.x}"
        return f"x' = {self.x1}\nx\" = {self.x2}"

class Complexe:
    def __init__(self, reel, imaginaire):
        self.reel = reel
        self.imaginaire = imaginaire

    def __repr__(self):
        return f"{self.reel} + {self.imaginaire}i"

    def multiplier(self, complexe):
        r = self.reel
        i = self.imaginaire
        cR = complexe.reel
        cI = complexe.imaginaire
        partieReelle = r * cR - i * cI
        partieImaginaire = (r + i)*(cR + cI) - partieReelle
        return Complexe(partieReelle, partieImaginaire)

def solve(a, b, c, withResume: bool = False):
    if withResume:
        partB = f"- {-b}" if b < 0 else f"+ {b}"
        partC = f"- {-c}" if c < 0 else f"+ {c}"
        print(f"Résoudre {a}x² {partB}x {partC} = 0")
    delta = b*b - 4*a*c
    if withResume:
        print(f"""
delta
= {b}² - 4 x {a} x {c} 
= {b**2} - {4*a*c}
= {delta}
""")
    if delta == 0:
        return Solution(-b / 2*a)
    elif delta > 0:
        x1 = (-b - sqrt(delta)) / (2*a)
        if withResume:
            print(f"""
x' = ({-b} - """+u"\u221A"+f"""{delta}) / {2*a}
   = ({-b} - {sqrt(delta)}) / {2*a}
   = {x1} 
""")
        x2 = (-b + sqrt(delta)) / (2*a)
        if withResume:
            print(f"""
x' = ({-b} + """+u"\u221A"+f"""{delta}) / {2*a}
   = ({-b} + {sqrt(delta)}) / {2*a}
   = {x2}
""")
            print(f"""
Vérification:
* {a} x {x1}² + {b} x {x1} + {c}
    = {a} x {x1**2} + {b*x1} + {c}
    = {a*(x1**2)} + {b*x1 + c}
    = {a*(x1**2) + b*x1 + c}
* {a} x {x2}² + {b} x {x2} + {c}
    = {a} x {x2**2} + {b*x2} + {c}
    = {a*(x2**2)} + {b*x2 + c}
    = {a*(x2**2) + b*x2 + c}
""")
    else:
        x1 = Complexe(-b / (2*a), -sqrt(abs(delta))/ (2*a))
        if withResume:
            print(f"""
x' = ({-b} - i"""+u"\u221A"+f"""{abs(delta)}) / {2*a}
   = ({-b} - {sqrt(abs(delta))} i) / {2*a}
""")
        x2 = Complexe(-b / (2*a), sqrt(abs(delta))/ (2*a))
        if withResume:
            print(f"""
x" = ({-b} + i"""+u"\u221A"+f"""{abs(delta)}) / {2*a}
   = ({-b} + {sqrt(abs(delta))} i) / {2*a}
""")
    return Solution(None, x1, x2)


