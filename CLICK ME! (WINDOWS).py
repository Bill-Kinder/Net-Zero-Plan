import tkinter as tk
from Program import Calculator
import csv
import matplotlib.pyplot as plt
import numpy as np

labels = []
buttons = []
entries = []
frames = []

def startGUI(configFileName):
    # Initialises some variables found in the config file, as well as loading the questions into the GUI.
    with open(configFileName, mode = 'r') as file:
        csvFile = csv.DictReader(file)
        for lines in csvFile:
            return lines

def loadQuestions(csvFileName):
    # Loads the questions from a csv file and adds them into the parameters list.
    with open(csvFileName, mode = 'r') as file:
        csvFile = csv.DictReader(file)
        for lines in csvFile:
            try:
                calc.addParam(question = lines['question'], weight = lambda x: float(lines['weight'])*x, scope = 0, sourceType = lines['sourceType'])
            except ValueError:
                print("A parameter had invalid values. Please check your parameters settings. Parameter question value: " + lines['question'])
    return None

def guiPrint(paramsList):
    # Displays all questions and answer boxes on the GUI screen.
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
    # Called when the "CALCULATE!" button is clicked.
    # Calculates gross emissions, number of trees required to reach net zero, and total cost, and displays them on the GUI screen. 
    try:
        for p in range(0,len(calc.params)):
            calc.updateAnswer(paramIndex=p, newAns=entries[p].get())
        em = calc.calcTotalEmissions()
        calc.calcTreesAndCost()
        labels[-1].configure(text = "Gross emissions: {:.2f}".format(em) + "kgCO2e.\nTrees needed to reach net zero: " + str(calc.numTrees) + "\nCost: ${:.2f}".format(calc.cost) + " (AUD).")
        return True
    except ZeroDivisionError:
        labels[-1].configure(text = "\nZero division error. Please check your inputs.\n")
        return False
    except ValueError:
        labels[-1].configure(text = "\nInvalid input. Please try again.\n")
        return False

def createNewGraph(event):
    # Called when the "DISPLAY PLOT" button is clicked.
    # Creates the CO2 per year and cost vs number of trees planted plot, as seen in our trade show poster.
    # Includes dashed lines at the exact net zero point, and the practical net zero point (where the number of trees is rounded up).
    
    #Creating data arrays
    Trees = np.arange(2*calc.numTrees)
    c02_offset = Trees * calc.co2perTree
    cost = Trees * calc.costTree
    total_emissions = np.full(2*calc.numTrees, calc.emissions)
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

    plt.axvline(x=calc.numTrees, linestyle='--', label='Practical net zero point')
    plt.axvline(x=calc.emissions/calc.co2perTree, linestyle='--',color='brown', label='Net zero emissions point')

    # Add legends to the subplots
    ax1.legend(loc='upper left')
    ax2.legend(loc='upper right')

    # Add a title and show the plot
    plt.title('Emissions Reduction NZI')
    plt.show()
    
    return None

def createPieChart(event):
    # Called when the "DISPLAY PIE CHART" button is clicked.
    # Creates a pie chart showing the percentage contribution of each emissions source.

    # Sample data
    sizes = []
    labels = []
    for p in calc.params:
        sizes.append(p['pct'])
        labels.append(p['src'])

    # Create a pie chart
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)

    # Set the aspect ratio to be equal (so the pie is circular)
    plt.axis('equal')

    # Add a title
    plt.title('Emissions sources contributions')

    # Display the pie chart
    plt.show()
    return None

p = startGUI('config.csv')
calc = Calculator(co2perTree = float(p['CO2 equivalent absorbed by 1 tree (kgCO2e)']), costTree = float(p['Cost of 1 tree (AUD)']))
loadQuestions(p['Parameters file name'])

rowsRange = list(range(0,2*(len(calc.params)+2)))

window = tk.Tk()
maxWidth = guiPrint(calc.params)
window.rowconfigure(rowsRange, minsize=50)
window.columnconfigure([0, 1, 2, 3], minsize=50)

answerFrame = tk.Frame(master = window, relief = tk.RIDGE, borderwidth = 5)
answerLabel = tk.Label(master = answerFrame, text = '\nFill in the boxes and click \"CALCULATE!\"\n')
answerLabel.grid(row=len(calc.params)+1, column = 0, sticky = "nsew")
answerFrame.grid(row=len(calc.params)+1, column = 0, sticky = "nsew")
labels.append(answerLabel)
frames.append(answerFrame)

buttonWidth = 25
if(buttonWidth < maxWidth):
    buttonWidth = maxWidth

calculateButton = tk.Button(
    text="CALCULATE!",
    width=buttonWidth,
    height=2,
    bg="yellow",
    fg="red",
    master = answerFrame
)

calculateButton.grid(row=len(calc.params)+2, column = 0, sticky = "nsew")
calculateButton.bind("<Button-1>", updateEmissions)

plotButton = tk.Button(
    text = "DISPLAY PLOT",
    width = buttonWidth,
    height = 2,
    bg = "yellow",
    fg = "green",
    master = answerFrame
)

plotButton.grid(row=len(calc.params)+3, column = 0, sticky="nsew")
plotButton.bind("<Button-1>", createNewGraph)

pieButton = tk.Button(
    text = "DISPLAY PIE CHART",
    width = buttonWidth,
    height = 2,
    bg = "yellow",
    fg = "blue",
    master = answerFrame
)

pieButton.grid(row=len(calc.params)+4, column = 0, sticky="nsew")
pieButton.bind("<Button-1>", createPieChart)

window.mainloop()