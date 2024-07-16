import turtle as T
from PIL import Image, EpsImagePlugin


class TurtleFr():
    __COEFF_SIZE = 5
    __GAP_CELL = 10

    def __init__(self, taille, nb_cases, displayGrid=True, colorGrid: str = "lightblue", borderColor="lightgrey", fondColor: str = "white"):
        """Dessine un repère carré horizontalement et verticalement, dont les dimensions varient de -taille à taille. 

        Arguments:
            taille --- taille maximum de la grille (maximum 65)\n
            nb_cases - nombre de case pour le repère
        """
        assert taille <= 65 and taille >= 5
        self.__size = taille*TurtleFr.__COEFF_SIZE
        self.__gapCase = int(taille / nb_cases) * TurtleFr.__GAP_CELL
        TurtleFr.__GAP_CELL = int(taille / nb_cases)
        self.__screen = T.Screen()
        self.__draw = T.Turtle()
        self.__draw.setheading(0)
        self.__screen.setup(self.__size*2.5, self.__size*2.5)
        self.__draw.penup()
        self.__draw.speed(0)
        self.__draw.hideturtle()
        self.__dessinerCarre(-self.__size, -self.__size,
                             self.__size, self.__size, borderColor, fondColor)
        if displayGrid:
            for row in range(-self.__size + self.__gapCase, self.__size, self.__gapCase):
                self.__dessinerLigne(-self.__size, row,
                                     self.__size, row, colorGrid)
            for column in range(-self.__size + self.__gapCase, self.__size, self.__gapCase):
                self.__dessinerLigne(column, -self.__size,
                                     column, self.__size, colorGrid)
        self.__draw.teleport(0, 0)
        self.__draw.speed(1)

    def tracerCercle(self, x, y, rayon, color, fillColor=None):
        self.__draw.penup()
        self.__draw.goto(x*TurtleFr.__GAP_CELL, y *
                         TurtleFr.__GAP_CELL+rayon*TurtleFr.__GAP_CELL)
        self.__draw.color(color)
        self.__draw.pendown()
        if fillColor is not None:
            self.__draw.fillcolor(fillColor)
            self.__draw.begin_fill()
        self.__draw.circle(rayon*TurtleFr.__GAP_CELL)
        if fillColor is not None:
            self.__draw.end_fill()

    def tracerCarre(self, minX, minY, maxX, maxY, color: str | None = None, fillColor: str | None = None):
        self.__draw.hideturtle()
        self.__draw.setheading(0)
        self.__draw.showturtle()
        self.__dessinerCarre(minX*TurtleFr.__GAP_CELL, minY*TurtleFr.__GAP_CELL,
                             maxX*TurtleFr.__GAP_CELL, maxY*TurtleFr.__GAP_CELL,
                             color,
                             fillColor)
        self.__draw.hideturtle()

    def __dessinerCarre(self, minX, minY, maxX, maxY, color: str | None = None, fillColor=None):
        params = [
            [minX, minY, minX, maxY],
            [minX, maxY, maxX, maxY],
            [maxX, maxY, maxX, minY],
            [maxX, minY, minX, minY]
        ]
        if fillColor is not None:
            self.__draw.begin_fill()
            self.__draw.fillcolor(fillColor)
        for i in range(len(params)):
            if i == 0:
                self.__draw.left(90)
            else:
                self.__draw.right(90)
            if color is not None:
                self.__dessinerLigne(*params[i], color, fillColor)
            else:
                self.__dessinerLigne(*params[i], fillColor=fillColor)
        if fillColor is not None:
            self.__draw.end_fill()

    def tracerLigne(self, x: int, y: int, x2: int, y2: int, color):
        self.__dessinerLigne(x*TurtleFr.__COEFF_SIZE, y*TurtleFr.__COEFF_SIZE,
                             x2*TurtleFr.__COEFF_SIZE, y2*TurtleFr.__COEFF_SIZE, color)

    def __dessinerLigne(self, x: int, y: int, x2: int, y2: int, color="lightgrey", fillColor=None):
        self.__draw.penup()
        self.__draw.goto(x, y)
        self.__draw.pendown()
        self.__draw.color(color)
        self.__draw.goto(x2, y2)
        if fillColor is not None:
            self.__draw.color(fillColor)
        self.__draw.penup()

    def changeVitesse(self, ratio: int):
        """Change la vitesse de déplacement des animations

        Arguments:
            ratio : nombre entier compris entre 0 et 10. 
                     0 -- le plus rapide\n
                     10 - rapide\n
                     6 -- normal\n
                     3 -- lent\n
                     1 -- le plus lent\n

        """
        self.__draw.speed(ratio)

    def exit(self):
        self.__screen.exitonclick()

    def save(self, gsLocation, filename):
        EpsImagePlugin.gs_windows_binary = gsLocation
        self.__draw.getscreen().getcanvas().postscript(
            file=filename+".ps", colormode='color')
        psImage = Image.open(filename+".ps")
        psImage.save(filename+".png")
        psImage.close()
        from os import remove
        remove(filename+".ps")


def example():
    X = TurtleFr(60, 5, True, "red", "green", "blue")
    X.changeVitesse(0)

    X.tracerCercle(10, 12.5, 7.5, "red", "yellow")
    X.tracerCercle(10, 12.5, 2, "red", "black")
    X.tracerCercle(-10, 12.5, 7.5, "red", "yellow")
    X.tracerCercle(-10, 12.5, 2, "red", "black")
    X.tracerCercle(0, 0, 5, "blue", "white")
    X.exit()


def showExample():
    print("""
        X = TurtleFr(60, 5, True, "red", "green", "blue")
        X.changeVitesse(0)

        X.tracerCercle(10, 12.5, 7.5, "red", "yellow")
        X.tracerCercle(10, 12.5, 2, "red", "black")
        X.tracerCercle(-10, 12.5, 7.5, "red", "yellow")
        X.tracerCercle(-10, 12.5, 2, "red", "black")
        X.tracerCercle(0, 0, 5, "blue", "white")
        X.save(r'C:\Program Files\gs\gs10.03.1\bin\gswin64c', "Test")
        X.exit()
    """)
