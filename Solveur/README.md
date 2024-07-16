# Solveur d'équation

Ce module est utile pour résoudre une équation de second degré.
Il gère les résultats dans l'ensemble des réels, et des complexes.

Il est également incorporé un mode résumé pour avoir le détail des opérations.

## Exemples

Pour résoudre x² + 10x + 9 = 0 :

> solve(1, 10, 9)

Pour résoudre x² + 10x - 25 = 0 :

> solve(1, 10, -25)

Pour avoir le détail des opérations, un booléen est à passer en tant que dernier paramètre.
Si l'on veut voir le détail à chaque étape, on renseigne True. Par défaut, il est considéré comme False.

> solve(1, 10, -25, True)
