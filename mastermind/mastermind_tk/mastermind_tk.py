from functools import partial
from os import getcwd
from random import randint
from tkinter import (
    BOTTOM,
    LEFT,
    RIGHT,
    Button,
    Frame,
    Label,
    PhotoImage,
    Tk,
    simpledialog,
    Text,
)
from tkinter.messagebox import *
from importlib.resources import path

from PIL import Image, ImageTk


def asker(number):
    global btns
    answer = simpledialog.askstring("Saisie", "Entrez un caractère", parent=window)
    if answer not in UNAUTHORIZED_CHAR:
        btns[number].config(text=str(answer))


def compteurs(masterword: list, props: list):
    goods = []
    bads = []
    d = dict()
    for i in range(len(masterword)):
        if masterword[i] in d.keys():
            d[masterword[i]] += 1
        else:
            d[masterword[i]] = 1
    for i in range(len(masterword)):
        if props[i] == masterword[i]:
            goods.append(props[i])
            d[props[i]] -= 1
    for i in range(len(masterword)):
        if props[i] != masterword[i] and props[i] in masterword and d[props[i]] > 0:
            d[props[i]] -= 1
            bads.append(props[i])
    return [len(goods), len(bads)]


def initMasterWord():
    mw = []
    for _ in range(5):
        mw.append(str(randint(0, 9)))
    return mw


def manageHistoric(label: Label):
    text = label.cget("text").split("\n")
    if len(text) > LIMIT_HISTORIC:
        text = "\n".join(text[-LIMIT_HISTORIC:])
        label.config(text=text)


def verifierEvent(event):
    global checker, window
    checker.config(background="darkorange", foreground="black", borderwidth=2)
    window.after(100, check)


def newGameClick(event):
    global reloader, window
    reloader.config(background="lime", foreground="black")
    window.after(100, reload)


def exit(event):
    global quitter
    quitter.config(background="black", foreground="red", borderwidth=0)
    window.after(300, quit)


def check():
    global btns, checker, nbPlayShot
    checker.config(background="orange", foreground="white")
    nbPlayShot += 1
    response = []
    for i in btns:
        response.append(i.cget("text"))
    manageHistoric(history_text)
    manageHistoric(history_results)
    currentHist = history_text.cget("text")
    currentResults = history_results.cget("text")
    [goods, bads] = compteurs(masterword, response)
    results = f"{goods}\u2713 " if goods > 0 else ""
    results += f"{bads}\u00d8 " if bads > 0 else ""
    results += f"{5 - bads - goods}\u2715 " if 5 - bads - goods > 0 else ""
    history_text.config(text=currentHist + " ".join(response) + f"\n")
    history_results.config(text=currentResults + results + f"\n")
    if goods == 5:
        code = " ".join(masterword)
        shots = "coups" if nbPlayShot > 1 else "coup"
        showinfo(
            "Bravo !",
            f"Bravo c'était bien {code}\nTrouvé en {nbPlayShot} {shots}",
        )
        reload()


def reload():
    global masterword, history_text, history_results, nbPlayShot
    reloader.config(background="green", foreground="black")
    nbPlayShot = 0
    history_text.config(text="")
    masterword = initMasterWord()
    history_results.config(text="")
    for btn in btns:
        btn.config(text="?")


def getLegend():
    return """Légende :

- Control A : Proposer tous les nombres
- Control N : Nouvelle partie
- Control Q : Quitter
- Entrer    : Vérifier
"""


def getBoundsLegend():
    tab = getLegend().split("\n")
    max = 0
    for i in tab:
        current = len(i)
        if max < current:
            max = current
    return {"width": max, "height": len(tab)}


def quit():
    quitter.config(background="red", foreground="white")
    window.quit()


def askAllNumbers(event):
    answer = simpledialog.askstring(
        "Saisie", "Suite:\nFormat : 'n n n n n'", parent=window
    )
    if answer != None and answer != "":
        tab = answer.split(" ")
        for i in range(len(tab)):
            if tab[i] not in UNAUTHORIZED_CHAR:
                btns[i].config(text=str(tab[i]))
        check()
    window.after(200, askAllNumbers)


LIMIT_HISTORIC = 40
UNAUTHORIZED_CHAR = [None, "", " "]
masterword = initMasterWord()
nbPlayShot = 0
window = Tk()
window.title("MasterMind")
window.geometry("1300x650")
window.attributes("-fullscreen", True)
window.bind("<Control-q>", exit)
window.bind("<Control-Q>", exit)
window.bind("<Control-a>", askAllNumbers)
window.bind("<Control-A>", askAllNumbers)
window.bind("<Control-N>", newGameClick)
window.bind("<Control-n>", newGameClick)
window.bind("<Return>", verifierEvent)
resourcePath = path("mastermind_tk.resources", "icon-font.png")
with resourcePath as resource:
    iconFont = resource
icon = PhotoImage(file=str(iconFont))
window.iconphoto(True, icon)
window.config(background="black")
crossPanel = Frame(window, borderwidth=0, relief="groove")
reloadPanel = Frame(window, borderwidth=0, relief="groove")
reloader = Button(
    reloadPanel, text="Nouvelle partie", background="green", command=reload
)
panelHigh = Frame(window, borderwidth=0, relief="groove")
history = Frame(window, background="brown", relief="groove")
history_label = Label(
    history,
    background="brown",
    font=("JetBrains", 11, "bold"),
    foreground="white",
    text="Historique",
)
history_text = Label(history, background="darkred", text="")
history_results = Label(history, background="orange", text="")
quitter = Button(
    crossPanel,
    text="\u2bbf Quitter",
    foreground="white",
    background="red",
    font=("JetBrains", 10, "bold"),
    command=window.quit,
)
panelNumbers = Frame(window)
checker = Button(
    panelNumbers, text="Vérifier", activebackground="darkorange", command=check
)

btns = []


def main():
    global btns, crossPanel, reloadPanel, reloader, panelHigh, history, history_label, history_results, history_text, quitter, panelNumbers, checker, iconFont

    crossPanel.pack(side=RIGHT, padx=5, pady=5, anchor="ne")
    reloadPanel.pack(padx=5, pady=5, anchor="nw")
    reloader.pack()
    panelHigh.pack(padx=5, pady=5)
    history.pack(side=LEFT, anchor="nw")
    history_label.pack()
    history_text.pack(side=LEFT)
    history_results.pack(side=RIGHT)
    history_label.config(width=20)
    history_text.config(width=15)
    history_results.config(width=15)
    history.config(width=20, height=600)
    quitter.pack()

    img = Image.open(iconFont)
    img = img.resize((49, 40), Image.LANCZOS)
    img = ImageTk.PhotoImage(img)
    Label(
        panelHigh,
        font=("Lucida Handwriting", 18, "bold"),
        background="darkred",
        foreground="orange",
        image=img,
        compound=LEFT,
        text=" MasterMind  ",
    ).pack(side=RIGHT)
    panelNumbers.pack()
    bg = ["lime", "darkred", "lightblue", "lightyellow", "orange"]
    fg = ["black", "white", "black", "black", "black"]
    for i in range(5):
        btn = Button(
            panelNumbers,
            text="?",
            background=bg[i],
            foreground=fg[i],
            font=("JetBrains", 12, "bold"),
            command=partial(asker, i),
        )
        btn.grid(row=1, column=i + 1, padx=5)
        btn.config(width=10, height=5)
        btns.append(btn)
    checker.grid(row=1, column=6, padx=5)
    checker.config(background="orange", foreground="white")
    panelNumbers.config(background="black")

    bounds = getBoundsLegend()
    legend = Text(window, wrap="word", width=bounds["width"], height=bounds["height"])
    legend.pack(expand=False, side=BOTTOM, anchor="se")
    legend.insert(1.0, getLegend())
    legend.config(
        state="disabled", background="black", foreground="white", borderwidth=0
    )
    legend.tag_add("title", 1.0, 1.9)
    legend.tag_configure(
        "title",
        justify="center",
        foreground="blue",
        font=("JetBrains Mono", 12, "italic"),
    )
    window.mainloop()


if __name__ == "main":
    main()
