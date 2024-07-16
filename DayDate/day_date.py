from colorate_console.colorizer import Colors


class Almanach:
    START_YEAR = 1901
    CYCLE_ANNUEL = 4
    JOURS = ['DIMANCHE', 'LUNDI', 'MARDI',
             'MERCREDI', 'JEUDI', 'VENDREDI', 'SAMEDI',]

    MOIS = dict(
        JANVIER=0, FÉVRIER=31, MARS=59, AVRIL=90, MAI=120, JUIN=151,
        JUILLET=181, AOÛT=212, SEPTEMBRE=243, OCTOBRE=273, NOVEMBRE=304, DÉCEMBRE=334,
    )

    @staticmethod
    def isBissextile(annee: int):
        return annee % 4 == 0 and annee % 100 != 0

    @staticmethod
    def getDayOfDate(jour: str, mois: str, annee: str):
        """Calcule le jour de la semaine d'une date donnée

        Raises:
            Exception: Si le mois donné n'existe pas, alors une exception est levée
        """

        jour = int(jour)
        # if not mois.upper() in CONSTANTES["MOIS"]:
        try:
            Almanach.MOIS[mois.upper()]
        except:
            raise Exception(f"Le mois indiqué n'existe pas ('{mois}')")
        annee = int(annee)
        ecart_date = annee - Almanach.START_YEAR
        cycle_annuel = ecart_date // Almanach.CYCLE_ANNUEL
        cumul_jours_mois = Almanach.MOIS[mois.upper()]
        nb_jours_supplementaires = 2 if Almanach.isBissextile(annee) else 1
        semaine = sum([ecart_date, cycle_annuel, cumul_jours_mois,
                       jour, nb_jours_supplementaires])
        index_jour = semaine % len(Almanach.JOURS)
        return [Almanach.JOURS[index_jour].lower(), jour, mois.lower(), annee]


def main():
    texte = Colors.getColoredMsg(
        Colors.COLORS.yellow.value,
        None,
        [Colors.extension.italic],
        "\nQuelle est votre date de naissance (JJ MMM AAAA) ? "
    )+"\n- "
    date = input(texte).split(" ")

    # Si on rencontre une erreur pendant la saisie, on l'affiche
    try:
        infosDate = Almanach.getDayOfDate(*date)
        Colors.printMsg(
            Colors.COLORS.cyan.value,
            Colors.COLORS.black.value,
            [],
            "\n=> Vous êtes né le",
            *infosDate
        )
    except Exception as e:
        Colors.printMsg(
            Colors.COLORS.red.value,
            None,
            [Colors.extension.italic, Colors.extension.marked],
            "\n"+str(e)
        )


if __name__ == "main":
    main()
