import tkinter as tk
from Program import Parameters

labels = []
buttons = []
entries = []
frames = []

def loadQuestions(paramsList):
    maxWidth = 0
    for p in range(0, len(paramsList)):
        t = paramsList[p]['q']
        if(len(t)>maxWidth):
            maxWidth = len(t)
        f = tk.Frame(master=window, relief = tk.GROOVE, borderwidth = 5, width=maxWidth)
        frames.append(f)
        l = tk.Label(master = f, text = t, width = len(t), height = 1)
        e = tk.Entry(master = f, text = tk.StringVar(), width=5)
        l.grid(row = 2*p, column = 0, sticky = "nsew")
        e.grid(row = 2*p+1, column = 0, sticky = "nsew")
        labels.append(l)
        entries.append(e)
        f.grid(row = p, column = 0, sticky = "nsew")
    return maxWidth


def updateEmissions(event):
    try:
        for p in range(0,len(pg.params)):
            pg.updateAnswer(paramIndex=p, newAns=entries[p].get())
        em = pg.calcTotalEmissions()
        labels[-1].configure(text = "Emissions: " + str(em) + "kgCO2e")
        return True
    except ValueError:
        labels[-1].configure(text = "Invalid input.")
        return False

pg = Parameters()
pg.addParam('How many people per meeting?', lambda x: x)
pg.addParam('How many people flying in?',lambda x: 50*x)
pg.addParam('test2')
pg.addParam('test3')
pg.addParam('test4')
pg.addParam('test5')
print(pg.params)
rowsRange = list(range(0,2*(len(pg.params)+2)))

window = tk.Tk()
maxWidth = loadQuestions(pg.params)
window.rowconfigure(rowsRange, minsize=50)
window.columnconfigure([0, 1, 2, 3], minsize=50)
    
graphFrame = tk.Frame()
frames.append(graphFrame)
graphText = tk.Label(text="This is a test label.", bg = "blue",master = graphFrame)
graphFrame.grid(row = 0, column = 1, sticky="nsew")
graphText.grid(row = 0, column = 1, sticky="nsew")

answerFrame = tk.Frame(master = window, relief = tk.RIDGE, borderwidth = 5)
answerLabel = tk.Label(master=answerFrame, text = 'Emissions: 0kgCO2e')
answerLabel.grid(row=len(pg.params)+1, column = 0, sticky = "nsew")
answerFrame.grid(row=len(pg.params)+1, column = 0, sticky = "nsew")
labels.append(answerLabel)
frames.append(answerFrame)

calculateButton = tk.Button(
    text="CALCULATE!",
    width=25,
    height=5,
    bg="yellow",
    fg="red",
    master = frames[-1]
)

calculateButton.grid(row=len(pg.params)+2, column = 0, sticky = "nsew")
calculateButton.bind("<Button-1>", updateEmissions)

window.mainloop()