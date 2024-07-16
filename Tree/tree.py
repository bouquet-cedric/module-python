import sys
from enum import Enum
from os import listdir
from os.path import isdir

from bigtree import Node, tree_to_dot, tree_to_pillow


class STATE(Enum):
    DONE = 0,
    EXIT = 1


def setLinkedParam(command: str, action, defaultValue, needed=False, withLink=True) -> STATE:
    if command in sys.argv:
        index = sys.argv.index(command)
        if withLink:
            try:
                param = sys.argv[index+1]
            except:
                param = defaultValue
            action(param)
        else:
            action()
        return STATE.DONE
    if needed and withLink and defaultValue is not None:
        action(defaultValue)
    return STATE.EXIT


def help():
    print(f"""
\033[3mAffiche graphiquement la structure de dossiers d'un chemin.\033[0m

py tree.py \033[35m[root]\033[0m \033[36m[options]\033[0m

\033[35mroot\033[0m    : dossier racine à partir duquel on commence la recherche
\033[36moptions\033[0m :
\t--mode [h/v]  : mode horizontal (h) ou vertical (v), par défaut [v].
\t-l [number]   : permet de donner la profondeur à parcourir, par défaut 3.
\t--png [file]  : enregistre l'affichage dans le fichier donné, file.png par défaut.
\t--dot [file]  : enregistre les noeuds sous forme de graphe dans le fichier donné, file.dot.png par défaut.
\t--help        : affiche cette aide.

\033[33;4mExemples\033[0m :
\tpy tree.py \033[36m--help\033[0m
\tpy tree.py \033[35m./src/app\033[0m
\tpy tree.py \033[35m./src/app\033[0m \033[36m--mode h\033[0m
\tpy tree.py \033[35m./src/app\033[0m \033[36m--mode v\033[0m
\tpy tree.py \033[35m./src/app\033[0m \033[36m-l 2\033[0m
\tpy tree.py \033[35m./src/app\033[0m \033[36m--png architecture\033[0m
\tpy tree.py \033[35m./src/app\033[0m \033[36m--dot architecture\033[0m
\tpy tree.py \033[35m./src/app\033[0m \033[36m-l 3 --png architecture\033[0m
\tpy tree.py \033[35m./src/app\033[0m \033[36m-l 3 --dot architecture-dot\033[0m
\tpy tree.py \033[35m./src/app\033[0m \033[36m-l 3 --png architecture  --dot architecture-dot\033[0m
""")
    exit(1)


def show(mode: str):
    global root
    if mode == 'v':
        root.show()
    elif mode == 'h':
        root.hshow()
    else:
        print(
            f"\033[31;1mCe mode n'existe pas, il est donc impossible d'afficher le résultat\033[0m"
        )


def link(path: str, parent: Node, depth: int, max_depth: int):
    global unauthorized
    if depth < max_depth:
        for f in listdir(path):
            chemin = f"{path}/{f}"
            try:
                if isdir(chemin) and depth < max_depth:
                    listdir(chemin)
                    child = Node(f)
                    parent >> child
                    link(chemin, child, depth+1, max_depth)
            except:
                unauthorized.append(chemin.replace("\\", "/"))

unauthorized = []
folder = sys.argv[1] if len(sys.argv) > 1 else '.'

if folder[-1] in ['/', "\\"]:
    folder = folder[:-1]

sep = "/" if "/" in folder else "\\"

tab = folder.split(sep)
root = Node(tab[0])

def main():
    global unauthorized, root, folder
    setLinkedParam('--help', help, None, False, False)


    last = root
    for p in tab[1:]:
        noeud = Node(p)
        last >> noeud
        last = noeud

    setLinkedParam('-l', lambda l: link(folder, last, 0, int(l)), 3, True)

    setLinkedParam('--mode', lambda l: show(l), 'v', True)
    if len(unauthorized) > 0:
        print(f"\033[31;3mAccès refusés :\033[0m")
        for chemin in unauthorized:
            print(f"\t- {chemin}")

    def saveAsPng(filename: str):
        global root
        png = tree_to_pillow(root)
        png.save(f"{filename}.png")

    def saveAsDot(filename: str):
        global root
        graph = tree_to_dot(root, node_colour="gold")
        graph.write_png(f"{filename}.png")

    setLinkedParam('--png', lambda l: saveAsPng(l), "file", False)
    setLinkedParam('--dot', lambda l: saveAsDot(l), "file.dot", False)


if __name__ == "main":
    main()

