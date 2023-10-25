class Parameters:
# This class handles all the calculations of the program.
    def __init__(self, params=[], emissions=0, numTrees = 0, cost = 0, costTree = 0, treeConst = 0):
        # params, short for parameters, is a list of dictionaries. 
        self.params = params
        # emissions is simply the total kgCO2e, based on the parameters entered.
        self.emissions = emissions
        # numtrees, i.e.: "number of trees", is the number of trees that Net Zero Initiative should plant to offset their emissions.
        self.numTrees = numTrees
        # cost is how much (AUD) Net Zero Initiative will need to afford all the trees it needs to plant.
        self.cost = cost
        # costTree is simply the cost of 1 tree
        self.costTree = costTree
        # treeConst, short for "tree constant", is a constant that determines how much kgCO2e is absorbed by 1 tree.
        self.treeConst = treeConst

    def loadParams(paramFile):
        # UNFINISHED FUNCTION
        # Intended to load a list of parameters from a file e.g.: csv.
        return None

    def addParam(self, question = 'Question string', calculation = lambda x: x, scope = 0b000, sourceType = None):
        # This function adds a new dictionary to the list of parameters (params).
        # Each dictionary has five fields: The question (string), the answer (number), calculation (lambda function) scope (integer) and source (string).
        # The question simply tells the emission source e.g.: "How many people fly in via plane per meeting?"
        # The answer is a quantitative measure of the emissions source in the question e.g.: 5 people fly in via plane.
        # The calculation, aka conversion factor, is a lambda function which calculates the kgCO2e emitted by the source, given the answer. e.g.: 150kgCO2e per plane traveller.
        # The scope is an integer between 0 and 7, detailing which emissions (scope 1, 2 or 3) that the question refers to. 3 bit binary format: 001 means only scope 1, 010 means only scope 2, etc.
        # The sourceType is a string detailing the source of carbon emissions for that particular parameter.
        param = {'q' : question, 'a' : 0, 'c' : calculation, 'sc': scope, 'src' : sourceType}
        self.params.append(param)
        return None

    def updateAnswer(self, paramIndex=0, newAns=0):
        # This function simply updates the "answer" field of a parameter dictionary, intended for when the user enters a number into the box.
        self.params[paramIndex]['a'] = float(newAns)
        print(self.params[paramIndex]['a']==float(newAns))
        return None
    
    def calcTotalEmissions(self):
        # This function adds up the emissions of each parameter by inserting the "answer" field of each dictionary into the "calculation" field (lambda function).
        total = 0
        for p in self.params:
            total+=p['c'](p['a'])
        self.emissions = total
        return self.emissions

    def calcTreesAndCost(self):
        # This function calculates the number of trees and the cost for the parameters list.
        self.numTrees = round(self.emissions/self.treeConst + 0.5)
        self.cost = self.numTrees*self.costTree
        return (self.numTrees, self.cost)

    def loopThroughQuestions(self):
        # This function takes user input for each parameter and updates the answers field. Used in the terminal.
        # May not be useful for GUI.
        for p in range(0,len(self.params)):
            self.updateAnswer(p,input(p['q'] + '\nAnswer: '))
        print("Finished")
        return None

    def runProgram(self):
        # Runs the program as it would in the terminal.
        # May not be useful for GUI.
        self.loopThroughQuestions()
        e = self.calcTotalEmissions()
        print('Total emissions = ' + str(e) + 'kgCO2e.')
        x = self.calcTreesAndCost()
        print('You need to plant ' + str(x[0]) + ' trees, which will cost ' + str(x[1]) + 'AUD.')
        return None

# question0 = {
#     'q' : 'question0',
#     'a' : 0,
#     'c' : lambda a: 0
# }
# question1 = {
#     'q' : 'How many attendees?',    # Parameter
#     'a' : 5,                        # Quantity   
#     'c' : lambda a: 1.5*a           # Conversion factor to kgCO2e (i.e.: In this case, 1.5kgCO2e per person in a meeting)
# }
# question2 = {
#     'q': 'How many flying in?', 
#     'a' : 5,
#     'c' : lambda a: 200*a
# }

# params = [question0, question1, question2]
# params.append(createField('How many attendees?', 0, lambda a: 1.5*a))
# params.append(createField('How much food? (kg)', 0, lambda a: 50*a))

# runProgram()
