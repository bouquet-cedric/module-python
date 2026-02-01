from functools import partial
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

from PIL.Image import Resampling
from getpass import getuser


class MasterMind:

    LIMIT_HISTORIC = 40
    UNAUTHORIZED_CHAR = [None, "", " "]

    def __init__(self):
        self.window = Tk()
        self.window.title("MasterMind")
        self.window.geometry("1300x650")
        self.window.attributes("-fullscreen", True)
        self.window.bind("<Control-q>", self.exit)
        self.window.bind("<Control-Q>", self.exit)
        self.window.bind("<Control-w>", self.exit)
        self.window.bind("<Control-W>", self.exit)
        self.window.bind("<Control-a>", self.askAllNumbers)
        self.window.bind("<Control-A>", self.askAllNumbers)
        self.window.bind("<Control-N>", self.newGameClick)
        self.window.bind("<Control-n>", self.newGameClick)
        self.window.bind("<Return>", self.verifierEvent)
        self.masterword = MasterMind.initMasterWord()
        self.nbPlayShot = 0

        resourcePath = path("mastermind_tk.resources", "icon-font.png")
        with resourcePath as resource:
            self.iconFont = resource
            self.icon = PhotoImage(file=str(self.iconFont))
            self.window.iconphoto(True, self.icon)
        self.window.config(background="black")
        self.crossPanel = Frame(self.window, borderwidth=0, relief="groove")
        self.reloadPanel = Frame(self.window, borderwidth=0, relief="groove")
        self.reloader = Button(
            self.reloadPanel,
            text="Nouvelle partie",
            background="green",
            command=self.reload,
        )
        self.panelHigh = Frame(self.window, borderwidth=0, relief="groove")
        self.history = Frame(self.window, background="brown", relief="groove")
        self.history_label = Label(
            self.history,
            background="brown",
            font=("JetBrains", 11, "bold"),
            foreground="white",
            text="Historique",
        )
        self.history_text = Label(self.history, background="darkred", text="")
        self.history_results = Label(self.history, background="orange", text="")
        self.quitter = Button(
            self.crossPanel,
            text="\u2bbf Quitter",
            foreground="white",
            background="red",
            font=("JetBrains", 10, "bold"),
            command=self.window.quit,
        )
        self.panelNumbers = Frame(self.window)
        self.checker = Button(
            self.panelNumbers,
            text="Vérifier",
            activebackground="darkorange",
            command=self.check,
        )

        self.btns: list[Button] = []

        self.crossPanel.pack(side=RIGHT, padx=5, pady=5, anchor="ne")
        self.reloadPanel.pack(padx=5, pady=5, anchor="nw")
        self.reloader.pack()
        self.panelHigh.pack(padx=5, pady=5)
        self.history.pack(side=LEFT, anchor="nw")
        self.history_label.pack()
        self.history_text.pack(side=LEFT)
        self.history_results.pack(side=RIGHT)
        self.history_label.config(width=20)
        self.history_text.config(width=15)
        self.history_results.config(width=15)
        self.history.config(width=20, height=600)
        self.quitter.pack()

        self.img = Image.open(self.iconFont)
        self.img = self.img.resize((49, 40), resample=Resampling.LANCZOS)
        self.img = ImageTk.PhotoImage(self.img)
        Label(
            self.panelHigh,
            font=("Lucida Handwriting", 18, "bold"),
            background="darkred",
            foreground="orange",
            image=self.img,
            compound=LEFT,
            text=" MasterMind  ",
        ).pack(side=RIGHT)
        self.panelNumbers.pack()
        bg = ["lime", "darkred", "lightblue", "lightyellow", "orange"]
        fg = ["black", "white", "black", "black", "black"]
        for i in range(5):
            btn = Button(
                self.panelNumbers,
                text="?",
                background=bg[i],
                foreground=fg[i],
                font=("JetBrains", 12, "bold"),
                command=partial(self.asker, i),
            )
            btn.grid(row=1, column=i + 1, padx=5)
            btn.config(width=10, height=5)
            self.btns.append(btn)
        self.checker.grid(row=1, column=6, padx=5)
        self.checker.config(background="orange", foreground="white")
        self.panelNumbers.config(background="black")

        # Afficher les infos en bas dans une frame dédiée
        bottomFrame = Frame(self.window, bg="black")
        bottomFrame.pack(padx=0, pady=0, side=BOTTOM, fill="x")
        bottomFrame.columnconfigure(0, weight=0)
        bottomFrame.columnconfigure(0, weight=1)
        bottomFrame.columnconfigure(0, weight=2)
        Label(
            bottomFrame,
            font=("Lucida Handwriting", 18, "bold"),
            background="black",
            foreground="yellow",
            text=f" Bienvenue {getuser()} ",
            padx=30,
            pady=20,
        ).grid(row=0, column=0, sticky="w")

        bounds = MasterMind.getBoundsLegend()
        legend = Text(
            bottomFrame, wrap="word", width=bounds["width"], height=bounds["height"]
        )
        legend.grid(row=0, column=1, sticky="nsew")
        legend.insert(1.0, bounds["legend"])
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

    def asker(self, number):
        answer = simpledialog.askstring(
            "Saisie", "Entrez un caractère", parent=self.window
        )
        if answer not in self.UNAUTHORIZED_CHAR:
            self.btns[number].config(text=str(answer))

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

    def manageHistoric(self: MasterMind, label: Label):
        text = label.cget("text").split("\n")
        if len(text) > self.LIMIT_HISTORIC:
            text = "\n".join(text[-self.LIMIT_HISTORIC :])
            label.config(text=text)

    def verifierEvent(self, event):
        self.checker.config(background="darkorange", foreground="black", borderwidth=2)
        self.window.after(100, self.check)

    def newGameClick(self, event):
        self.reloader.config(background="lime", foreground="black")
        self.window.after(100, self.reload)

    def exit(self, event):
        self.quitter.config(background="black", foreground="red", borderwidth=0)
        self.window.after(300, self.quit)

    def check(self: MasterMind):
        self.checker.config(background="orange", foreground="white")
        self.nbPlayShot += 1
        response = []
        for i in self.btns:
            response.append(i.cget("text"))
        self.manageHistoric(self.history_text)
        self.manageHistoric(self.history_results)
        currentHist = self.history_text.cget("text")
        currentResults = self.history_results.cget("text")
        [goods, bads] = MasterMind.compteurs(self.masterword, response)
        results = f"{goods}\u2713 " if goods > 0 else ""
        results += f"{bads}\u00d8 " if bads > 0 else ""
        results += f"{5 - bads - goods}\u2715 " if 5 - bads - goods > 0 else ""
        self.history_text.config(text=currentHist + " ".join(response) + f"\n")
        self.history_results.config(text=currentResults + results + f"\n")
        if goods == 5:
            code = " ".join(self.masterword)
            shots = "coups" if self.nbPlayShot > 1 else "coup"
            showinfo(
                "Bravo !",
                f"Bravo c'était bien {code}\nTrouvé en {self.nbPlayShot} {shots}",
            )
            self.reload()

    def reload(self: MasterMind):
        self.reloader.config(background="green", foreground="black")
        self.nbPlayShot = 0
        self.history_text.config(text="")
        self.masterword = MasterMind.initMasterWord()
        self.history_results.config(text="")
        for btn in self.btns:
            btn.config(text="?")

    def getLegend():
        return """Légende :

    - Control A : Proposer tous les nombres
    - Control N : Nouvelle partie
    - Control W/Q : Quitter
    - Entrer    : Vérifier
    """

    def getBoundsLegend():
        legend = MasterMind.getLegend()
        tab = legend.split("\n")
        max = 0
        for i in tab:
            current = len(i)
            if max < current:
                max = current
        return {"width": max, "height": len(tab), "legend": legend}

    def quit(self: MasterMind):
        self.quitter.config(background="red", foreground="white")
        self.window.quit()

    def askAllNumbers(self: MasterMind, event):
        answer = simpledialog.askstring(
            "Saisie", "Suite:\nFormat : 'n n n n n'", parent=self.window
        )
        if answer != None and answer != "":
            tab = answer.split(" ")
            for i in range(len(tab)):
                if tab[i] not in self.UNAUTHORIZED_CHAR:
                    self.btns[i].config(text=str(tab[i]))
            self.check()
            self.window.after(1000, lambda: self.askAllNumbers(None))

    def play(self):
        self.window.mainloop()


def main():
    window = MasterMind()
    window.play()


if __name__ == "main":
    main()
