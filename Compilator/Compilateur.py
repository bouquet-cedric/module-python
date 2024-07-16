
from math import sqrt


class Compiler:
    def __init__(self):
        self.variables = dict()
        self.indicators = {'total': 0, 'analyzed': 0,
                           'empty': 0, 'commentaires': 0}

    def readFile(self, filename):
        file = open(filename, 'r', encoding='utf-8')
        line = file.readline()
        while line != "":
            self.analyse(line)
            self.indicators['total'] += 1
            line = file.readline()
        self.printIndicators()

    def printIndicators(self):
        print('=================================================================================')
        print(f"{self.indicators['analyzed']} / {self.indicators['total']} lignes de code analysées.")
        print(f"{self.indicators['commentaires']} commentaires trouvés.")
        print(f"{self.indicators['empty']} lignes vides.")

    def analyse(self, line: str):
        line = line[:-1]
        if line == "":
            self.indicators['empty'] += 1
            return
        words = line.split(" ")
        if words[0] == "com" or words[0] == ".":
            self.indicators['commentaires'] += 1
            return
        if words[0] == "let":
            indexEqual = words.index("=")
            value = words[indexEqual+1:]
            chaine = []
            for i in value:
                if i in self.variables.keys():
                    chaine.append(str(self.variables[i]))
                else:
                    chaine.append(str(i))
            self.variables[words[1]] = eval(" ".join(chaine))
        if words[0] == "show":
            chaine = []
            for i in words[1:]:
                if i in self.variables.keys():
                    chaine.append("str("+str(self.variables[i])+")")
                else:
                    chaine.append(str(i))
            print(eval(" ".join(chaine)))
        self.indicators['analyzed'] += 1


C = Compiler()
C.readFile("compile.txt")
