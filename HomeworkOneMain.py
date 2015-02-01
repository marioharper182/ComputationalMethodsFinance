__author__ = 'Mario'

from tkinter import Tk, LEFT, RIGHT, BOTH, RAISED, Listbox, StringVar,END, Entry
from tkinter.ttk import Frame, Button, Style, Label
import chickennugget
import GuessMyNumber
import sys, random
import subprocess as sub

class MainGUI(Frame):

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

        self.parent.title("Homework 1 GUI Interface")
        self.pack(fill=BOTH, expand=1)
        self.style = Style()
        self.style.theme_use("default")

        frame = Frame(self, relief=RAISED, borderwidth=1)
        frame.pack(fill=BOTH, expand=1)
        self.pack(fill=BOTH, expand=1)

        # ChickenButton = Button(self, text="ChickenNugget", command = HomeworkOneFunctions.chickennugget_main)
        # ChickenButton.pack(side=RIGHT)
        # GuessButton = Button(self, text="GuessTheNumber", command = HomeworkOneFunctions.guessinggame_main)
        # GuessButton.pack(side=RIGHT)

        # Create the objects on the frame
        options = ['Chicken Nugget Problem', 'Guess the Number (User Input)',
                   'Guess the Number (Random Input)']
        lb = Listbox(self, height = 5, width = 35)
        for i in options:
            lb.insert(END, i)
        lb.place(x=20, y=20)
        self.guessInput = Entry(self, width = 70)
        self.guessInput.pack(side=LEFT)
        # Bindings
        # ChickenButton.bind('<c>', HomeworkOneFunctions.chickennugget_main)
        # ChickenButton.bind('<g>', HomeworkOneFunctions.chickennugget_main)
        lb.bind("<<ListboxSelect>>", self.onActive)
        lb.bind("<Double-Button-1>", self.onSelect)

        # Set Location for printed text
        self.var = StringVar()
        self.label = Label(self, text=0, textvariable=self.var)
        self.label.place(x=19, y=250)

        self.resultprint = StringVar()
        self.labeltext = Label(self, text=0, textvariable=self.resultprint)
        self.labeltext.place(x=19, y =195)

    def onActive(self, val):
        sender = val.widget
        idx = sender.curselection()
        value = sender.get(idx)


    def onSelect(self, val):
        sender = val.widget
        idx = sender.curselection()
        value = sender.get(idx)

        self.resultprint.set('')

        if value == 'Chicken Nugget Problem':
            A = chickennugget.chickennugget_main()
            text = "The highest integer of chicken nuggets purchasable is:", str(A)
            self.var.set(text)

        if value == 'Guess the Number (User Input)':
            text = "Enter a number between 1-100: Double-click on the option again: "
            self.var.set(text)
            def getinput(number):
                valtext = GuessMyNumber.Guessengine(int(number))
                self.resultprint.set(valtext)
            if self.guessInput.get() != '':
                self.guessInput.bind("<Enter>", getinput(self.guessInput.get()))
            else: pass

        if value == 'Guess the Number (Random Input)':
            A = random.randint(1,100)
            text = "To save you the hassle, you choose to pick the number:", str(A)
            self.var.set(text)
            valtext = GuessMyNumber.Guessengine(A)
            self.resultprint.set(valtext)

def main():
    root = Tk()
    root.geometry("400x300+300+300")
    app = MainGUI(root)
    root.mainloop()

if __name__ == '__main__':
    main()
