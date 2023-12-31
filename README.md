# NetZeroPlan
A Git repository for our net zero project. Calculate the number of trees and cost of planting them to offset the Net Zero Initiative's carbon dioxide equivalent emissions!

# File Information
- "CLICK ME! (MAC).command": Double click this to run the GUI program on MAC OS.
  
- "CLICK ME! (WINDOWS).py": Double click this to run the GUI program on Windows OS. Also contains the main code for the program.
  
- "Program.py": Contains code used by the program.

- "cmd-line-testing.py": A Python executable script used for testing the main functions of the program. Only used in the command line for basic tests. Not used for GUI.

- "params.csv": Contains all the questions and emissions sources used in the program to determine emissions sources and calculate total emissions. The parameters are:
  - question: A string containing the question that links an emissions source or activity to a quantity of emissions. This could be something like "How many people attend each meeting?"
  - weight: A numerical variable that determines how much an emissions source contributes. An example of weight could be the number "50", indicating that the specific emissions source contributes 50kg of CO2 equivalent per unit of the emissions source. This value should always be numerical.
  - scope: A number that determines what combination of scopes 1, 2 and 3 that particular emissions source is. Due to time constraints this parameter was not integrated fully into the program.
  - sourceType: A string that tells the program what to call the emissions source. e.g.: "Fuel emissions". Distinct from the question string. Used by the program when generating the pie chart.
  
- "config.csv": Comma-separated value (csv) file containing 3 headings: "Cost of 1 tree (AUD)", "CO2 equivalent absorbed by 1 tree (kgCO2e)" and "Parameters file name". Parameters can be edited by opening the csv file in a spreadsheet or text editor (e.g.: Excel). However, the file extension must always be ".csv".
  - Cost of 1 tree: By default we assumed 1 tree costs $1.55 in Australian Dollars. This can be changed by the user if necessary.
  - CO2 equivalent absorbed by 1 tree: By default we assumed 1 tree absorbs 25kg of CO2 equivalent per year of its life. This can be changed if necessary.
  - Parameters file name: By default, set to "params.csv". If the user has a different parameters file, this field can be changed. However, the parameters file must always have the extension ".csv".

# How to open the program

- Make sure you have the latest version of Python installed on your computer.
  - You also need the following packages installed in your environment: `csv`, `matplotlib`, `numpy` and `tkinter`. To install a package, type this in the terminal: `pip install <package-name>` or `pip3 install <package-name>`. e.g.: `pip3 install tkinter`.
  
- Download all of the files in this repository, and unzip the folder. The folder should be named "Net-Zero-Plan-main". Do not change any of the file names.
  
- Opening the program depends on what computer you are using:
  
  - If you are using Windows, double click the file "CLICK ME! (WINDOWS).py" to run the program. Open the program using Python launcher.
    
  - If you are using Mac, double click the file named "CLICK ME! (MAC).command" to run the program. If you do not have appropriate access privileges, do the following:
    - Right click the folder "Net-Zero-Plan-main", and click the option "New terminal at folder".
    - Wait for the terminal window to load. When you can type commands, enter the command `chmod u+x "CLICK ME! (MAC).command"`. This should grant you access privileges. Try to double click the file again.

# How to use the program

1. Enter the correct quantities into the boxes under each question. (More questions can be added in the file "params.csv")
2. Click the red "CALCULATE!" button to calculate total emissions, number of trees to reach net zero, and cost.
3. Click the green "DISPLAY PLOT" button to display a plot showing CO2 per year vs number of trees planted vs cost. Close the graph window when finished.
4. Click the blue "DISPLAY PIE CHART" button to display a pie chart detailing how each emissions source contributes to the overall emissions. Close the pie chart window when finished.
5. Each time you change the numbers under each question, you need to press "CALCULATE!" again to update the plot and pie chart.
6. Displaying the pie chart and plot at the simultaneously sometimes leads to one being displayed on top of the other. If this happens, just close the pie chart/plot window and view them separately.

# How the program works

1. The program reads the contents of "config.csv" and "params.csv" to determine which questions to ask, what weightings to assign to each question, and determine other constants such as how much 1 tree costs, and how much CO2 is absorbed by 1 tree.
2. The program displays the questions and all other GUI elements in the window.
3. When the user enters numbers into the answer boxes, and clicks "CALCULATE!", the program calculates total emissions, number of trees and cost in the box, and displays the variables above the button.


