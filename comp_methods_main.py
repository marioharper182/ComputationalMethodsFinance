__author__ = 'Mario'

from tkinter import Tk, RIGHT, BOTH, RAISED
from tkinter.ttk import Frame, Button, Style
import Homework1
import sys
import subprocess as sub



class Example(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.parent = parent
        self.initUI()

    def run_script(self):
        p = sub.Popen('./script',stdout=sub.PIPE,stderr=sub.PIPE)
        output, errors = p.communicate()
        sys.stdout = self
        ## sys.stderr = self
        try:
            del(sys.modules["test_script"])
        except:
            ## Yeah, it's a real ugly solution...
            pass
        # import test_script
        print('Hello Mario, console output is working')
        sys.stdout = sys.__stdout__

    def initUI(self):

        self.parent.title("First Project")
        self.style = Style()
        self.style.theme_use("default")

        frame = Frame(self, relief=RAISED, borderwidth=1)
        frame.pack(fill=BOTH, expand=1)

        self.pack(fill=BOTH, expand=1)

        ChickenButton = Button(self, text="ChickenNugget", command = Homework1.chickennugget_main)
        ChickenButton.pack(side=RIGHT)
        ChickenButton.bind('<c>', Homework1.chickennugget_main)
        GuessButton = Button(self, text="GuessTheNumber", command = Homework1.guessinggame_main)
        GuessButton.pack(side=RIGHT)
        ChickenButton.bind('<g>', Homework1.chickennugget_main)

def main():

    root = Tk()
    root.geometry("300x200+300+300")
    app = Example(root)
    root.mainloop()


if __name__ == '__main__':
    main()