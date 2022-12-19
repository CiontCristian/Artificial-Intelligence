import tkinter as tk
from tkinter import messagebox
from Controller import Controller


class GUI:
    def __init__(self):
        self.initGUI()
        self.__controller = None

    def initGUI(self):
        window = tk.Tk()
        window.title("GUI")
        window.geometry('500x500')

        matrixSizeLabel = tk.Label(text="Matrix Size")
        matrixSizeLabel.pack()
        matrixSizeLabel.grid(column=0, row=0)
        self.matrixSizeEdit = tk.Entry(width=50)
        self.matrixSizeEdit.grid(column=1, row=0)

        populationLabel = tk.Label(text="Population")
        populationLabel.grid(column=0, row=1)
        self.populationEdit = tk.Entry(width=50)
        self.populationEdit.grid(column=1, row=1)

        probabilityLabel = tk.Label(text="Mutate Probability")
        probabilityLabel.grid(column=0, row=2)
        self.probabilityEdit = tk.Entry(width=50)
        self.probabilityEdit.grid(column=1, row=2)

        iterationsLabel = tk.Label(text="Nr. Of Iterations")
        iterationsLabel.grid(column=0, row=3)
        self.iterationsEdit = tk.Entry(width="50")
        self.iterationsEdit.grid(column=1, row=3)

        self.radioValue = tk.StringVar()
        self.EARadio = tk.Radiobutton(text="EA", value="EA", var=self.radioValue)
        self.EARadio.grid(column=0, row=4)
        self.HCRadio = tk.Radiobutton(text="HC", value="HC", var=self.radioValue)
        self.HCRadio.grid(column=1, row=4)

        exitButton = tk.Button(text="Exit", command=self.exitApp)
        exitButton.grid(column=0, row=5)

        runButton = tk.Button(text="Run", command=self.runApp)
        runButton.grid(column=1, row=5)

        self.resultLabel = tk.Label(text="")
        self.resultLabel.grid(column=0, row=6, columnspan=5, rowspan=5)

        window.mainloop()

    def exitApp(self):
        exit(0)

    def runApp(self):
        try:
            size = int(self.matrixSizeEdit.get())
            population = int(self.populationEdit.get())
            prob = float(self.probabilityEdit.get())
            iterations = int(self.iterationsEdit.get())

            self.__controller = Controller(size, population, prob, iterations)

            algorithm = self.radioValue.get()
            if algorithm == "EA":
                result = self.__controller.EA()
                fitnessOptim = result[0]
                individualOptim = result[1]
                string = "Result: The detected minimum point after " + str(iterations) + " iterations is: \n" + \
                         str(individualOptim) + "\nProblems: " + str(fitnessOptim)
                self.resultLabel.configure(text=string)
            else:
                result = self.__controller.HC()
                fitnessOptim = result[0]
                individualOptim = result[1]
                string = "Result: The detected minimum point after " + str(iterations) + " iterations is: \n" + \
                         str(individualOptim) + "\nProblems: " + str(fitnessOptim)
                self.resultLabel.configure(text=string)
        except Exception as exception:
            tk.messagebox.showerror("Error", exception)
