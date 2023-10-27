class Calculator:
# This class handles all the calculations of the program.
    def __init__(self, params=[], emissions=0, numTrees = 0, cost = 0, costTree = 0, co2perTree = 0):
        # Initialisation function.
        # params: a list of dictionaries. "params" is short for "parameters".
        # emissions: the total kgCO2e emitted, based on the parameters entered.
        # numtrees: the number of trees that Net Zero Initiative should plant to offset their emissions. 
        # cost: amount in AUD Net Zero Initiative will need to spend to afford all the trees it needs to plant.
        # costTree: the cost of 1 tree in AUD.
        # co2perTree: a constant that determines how much kgCO2e is absorbed by 1 tree.

        self.params = params
        self.emissions = emissions
        self.numTrees = numTrees
        self.cost = cost
        self.costTree = costTree
        self.co2perTree = co2perTree

    def addParam(self, question = 'Question string', weight = lambda x: x, scope = 0b000, sourceType = 'Source type string', pctCont = 0):
        # Adds a new dictionary to the list of parameters (params).
        # question: displayed to the user to determine how much an emissions source contributes to the total emissions. e.g.: "How many people take public transport?". If it is an empty string, it will be the same as "sourceType."
        # answer: a quantitative measure of the emissions source in the question e.g.: 50 people take public transport.
        # weight: a lambda function which calculates the kgCO2e emitted by the source, given the answer. e.g.: 150*x means 150kgCO2e is produced per quantity x.
        # scope: an integer between 0 and 7, in binary format, which determines which emissions (scope 1, 2 or 3) that the question refers to. e.g.: 010: Only scope 2. 101: Only scope 1 and scope 3.
        # sourceType: a string detailing the source of carbon emissions for a parameter. e.g.: Public transport. Only explicitly defined for the purposes of the pie chart.
        # pctCont: percent contribution of the parameter to the total emissions.

        if(question==''):
            question = sourceType
        param = {'q' : question, 'a' : 0, 'w' : weight, 'sc': scope, 'src' : sourceType, 'pct' : pctCont}
        self.params.append(param)
        return None

    def updateAnswer(self, paramIndex=0, newAns=0):
        # Updates the "answer" field of a parameter dictionary, intended for when the user enters a number into the box.
        self.params[paramIndex]['a'] = float(newAns)
        return None
    
    def calcTotalEmissions(self):
        # Adds up the emissions of each parameter by inserting the "answer" field of each dictionary into the "weight" field.
        total = 0
        for p in self.params:
            total+=p['w'](p['a'])
        for p in self.params:
            p['pct'] = (p['w'](p['a'])/total)*100
        self.emissions = total
        return self.emissions

    def calcTreesAndCost(self):
        # Calculates the number of trees and the cost for the parameters list.
        self.numTrees = round(self.emissions/self.co2perTree + 0.5)
        self.cost = self.numTrees*self.costTree
        return (self.numTrees, self.cost)

    def loopThroughQuestions(self):
        # Takes user input for each parameter and updates the answers field. Used in the terminal. Unused for GUI.
        for p in range(0,len(self.params)):
            self.updateAnswer(p,input(p['q'] + '\nAnswer: '))
        print("Finished")
        return None

    def runProgram(self):
        # Loops through questions and makes calculations in the terminal. Unused for GUI.
        self.loopThroughQuestions()
        e = self.calcTotalEmissions()
        print('Total emissions = ' + str(e) + 'kgCO2e.')
        x = self.calcTreesAndCost()
        print('You need to plant ' + str(x[0]) + ' trees, which will cost ' + str(x[1]) + 'AUD.')
        return None