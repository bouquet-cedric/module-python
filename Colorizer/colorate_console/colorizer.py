from sys import argv
from enum import Enum


class Colors:
    class COLORS(Enum):
        black = 0
        red = 1
        green = 2
        yellow = 3
        blue = 4
        purple = 5
        cyan = 6
        white = 7

    class extension:
        marked = 1
        unmarked = 2
        italic = 3
        underline = 4
        blink = 5
        blink2 = 6
        surline_by_fg = 7
        surline_by_bg = 8
        striped = 9

    def colorize(fg: int | None, bg: int | None = None, *extension: int):
        start = f"\033["
        if fg is not None:
            start = start + f"3{fg};"
        if bg is not None:
            start = start + f"4{bg};"
        if extension:
            for i in extension:
                start = start + f"{i};"
        if start[-1] == ';':
            start = start[:-1]
        return start + "m"

    def printMsg(fg, bg, extension: list, *msg):
        print(Colors.getColoredMsg(fg, bg, extension, *msg))

    def getColoredMsg(fg, bg, extension: list, *msg):
        texte = " ".join([str(_msg) for _msg in msg])
        return f"{Colors.colorize(fg, bg, *extension)}{texte}{Colors.colorize(None, None, 0)}"


def main():
    fg = None
    bg = None
    extensions = []
    msg = ""
    for indexParam in range(len(argv)):
        if argv[indexParam] == "--msg":
            msg = argv[indexParam + 1]
        elif argv[indexParam] == "--fg":
            _fg = argv[indexParam + 1]
            if _fg in Colors.COLORS._member_names_:
                print(Colors.COLORS[_fg])
                fg = Colors.COLORS[_fg].value

        elif argv[indexParam] == "--bg":
            _bg = argv[indexParam + 1]
            if _bg in Colors.COLORS._member_names_:
                print(Colors.COLORS[_bg].value)
                bg = Colors.COLORS[_bg].value
        elif argv[indexParam] == "-i":
            extensions.append(Colors.extension.italic)
        elif argv[indexParam] == "-b":
            extensions.append(Colors.extension.blink2)
        elif argv[indexParam] == "-s":
            extensions.append(Colors.extension.striped)
        elif argv[indexParam] == "-u":
            extensions.append(Colors.extension.underline)
        elif argv[indexParam] == "-sbg":
            extensions.append(Colors.extension.surline_by_bg)
        elif argv[indexParam] == "-sfg":
            extensions.append(Colors.extension.surline_by_fg)
        elif argv[indexParam] == "-m":
            extensions.append(Colors.extension.marked)
        elif argv[indexParam] == "-um":
            extensions.append(Colors.extension.unmarked)
    Colors.printMsg(fg, bg, extensions, msg)


if __name__ == "main":
    main()
