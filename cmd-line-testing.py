from Program import Calculator
calc = Calculator()
calc.addParam(question = 'Total number of attendees?', weight = 20, sourceType = 'Food production and waste')
calc.addParam(question = 'Number of local attendees?', weight = 25, sourceType = 'Car fuel')
calc.addParam(question = 'Number of attendees from overseas?', weight = 30, sourceType = 'Aeroplane fuel')
calc.runProgram()
