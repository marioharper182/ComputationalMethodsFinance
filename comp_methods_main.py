__author__ = 'Mario'

from tkinter import Tk, RIGHT, BOTH, RAISED
from tkinter.ttk import Frame, Button, Style


class Example(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.parent = parent

        self.initUI()

    def initUI(self):

        self.parent.title("First Project")
        self.style = Style()
        self.style.theme_use("default")

        frame = Frame(self, relief=RAISED, borderwidth=1)
        frame.pack(fill=BOTH, expand=1)

        self.pack(fill=BOTH, expand=1)

        closeButton = Button(self, text="Close", command=Example.destroy)
        closeButton.pack(side=RIGHT, padx=5, pady=5)
        okButton = Button(self, text="Excecute", command=self.ExcecuteButton())
        okButton.pack(side=RIGHT)


    def ExcecuteButton(self):

        pass



def main():

    root = Tk()
    root.geometry("300x200+300+300")
    app = Example(root)
    root.mainloop()


if __name__ == '__main__':
    main()