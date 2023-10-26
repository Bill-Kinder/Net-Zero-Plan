import tkinter as tk
from Program import Parameters
import matplotlib.pyplot as plt
import numpy as np

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
        pg.calcTreesAndCost()
        labels[-1].configure(text = "Gross emissions: " + str(em) + "kgCO2e.\nPlant " + str(pg.numTrees) + " trees to reach net zero.\nCost: " + str(pg.cost) + "AUD.")
        return True
    except ValueError:
        labels[-1].configure(text = "Invalid input.")
        return False

def createNewGraph(event):
    #Creating data arrays
    Trees = np.arange(2*pg.numTrees)
    c02_offset = Trees * pg.treeConst
    cost = Trees * pg.costTree
    total_emissions = np.full(2*pg.numTrees, pg.emissions)
    net_emissions = total_emissions - c02_offset # Needs to extend at least to 0, for net zero.
    #Graphing arrays
    # Create a Matplotlib figure with two subplots
    fig, ax1 = plt.subplots()
    ax2 = ax1.twinx()

    ax1.plot(Trees, total_emissions, label='Gross Emissions', color='blue')
    ax1.plot(Trees, net_emissions, label='Net Emissions', color='green')
    ax1.plot(Trees, c02_offset, label='CO2 Offset', color='magenta')
    ax2.plot(Trees, cost, label='Cost', color='red')

    # Set labels for the axes
    ax1.set_ylabel('CO2 per year (kg)')
    ax2.set_ylabel('Cost ($AUD)')
    ax1.set_xlabel('Number of Trees Planted')

    # Grid line width
    ax1.grid(which = "major", linewidth = 1)
    ax1.grid(which = "minor", linewidth = 0.2)
    ax1.minorticks_on()

    plt.axvline(x=pg.numTrees, linestyle='--', label='Effective net zero point')
    plt.axvline(x=pg.emissions/pg.treeConst, linestyle='--',color='brown', label='Net zero emissions point')

    # Add legends to the subplots
    ax1.legend(loc='upper left')
    ax2.legend(loc='upper right')

    # Add a title and show the plot
    plt.title('Emissions Reduction NZI')
    plt.show()
    
    return None

def createPieChart(event):
    # Sample data
    sizes = [15, 30, 45, 10]
    labels = ['A', 'B', 'C', 'D']

    # Create a pie chart
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)

    # Set the aspect ratio to be equal (so the pie is circular)
    plt.axis('equal')

    # Add a title
    plt.title('Sample Pie Chart')

    # Display the pie chart
    plt.show()
    return None

pg = Parameters(treeConst = 25, costTree = 1.55)
pg.addParam(question='How many people per meeting?', calculation=lambda x: 1.09*x,scope=0b100)
pg.addParam('How many people flying in?', lambda x: 50*x)
pg.addParam('Average travel distance', lambda x: x)

print(pg.params)
rowsRange = list(range(0,2*(len(pg.params)+2)))

window = tk.Tk()
maxWidth = loadQuestions(pg.params)
window.rowconfigure(rowsRange, minsize=50)
window.columnconfigure([0, 1, 2, 3], minsize=50)
    
graphFrame = tk.Frame()
frames.append(graphFrame)
graphFrame.grid(row = 0, column = 1, sticky="nsew")

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

plotButton = tk.Button(
    text = "DISPLAY PLOT",
    width = 25,
    height = 2,
    bg = "yellow",
    fg = "red",
    master = graphFrame
)

plotButton.grid(row = 2, column = 1, sticky="nsew")
plotButton.bind("<Button-1>", createNewGraph)

pieButton = tk.Button(
    text = "DISPLAY PIE CHART",
    width = 25,
    height = 2,
    bg = "yellow",
    fg = "red",
    master = graphFrame
)

pieButton.grid(row = 3, column = 1, sticky="nsew")
pieButton.bind("<Button-1>", createPieChart)

window.mainloop()