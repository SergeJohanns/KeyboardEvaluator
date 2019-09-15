import time

#Classes
class Keyboard: #Because doing this with a multidimensional list was bad for a whole bunch of reasons (unreadable, hard to add variables, etc.)
    def __init__(self, name, homeRow, keyboard):
        self.name = name
        self.homeRow = homeRow
        self.keyboard = keyboard

#Subroutines
def PrintTime(taskString, timeIn):
    """Print a log statement saying how long the current task took"""
    endTime = time.time()
    duration = endTime - timeIn
    print("{} took {} milliseconds.".format(taskString, round(duration * 1000)))
    return time.time()

def SumSubLists(listIn):
    """Takes in a list of of lists of numbers and returns a list of the sums of those sublists"""
    output = []
    for i in range(len(listIn)):
        output.append(0)
        for j in range(len(listIn[i])):
            output[i] += listIn[i][j]
    return output

#Initialise starting constructs
charIgnoreSet = {'\n'}
startTime = time.time()
keyboardList = []
keyboardList.append(Keyboard("QWERTY", 1, [['q','w','e','r','t','y','u','i','o','p'],['a','s','d','f','g','h','j','k','l'],['z','x','c','v','b','n','m']]))
keyboardList.append(Keyboard("DVORAK", 1, [['p','y','f','g','c','r','l'],['a','o','e','u','i','d','h','t','n','s'],['q','j','k','x','b','m','w','v','z']]))
keyboardList.append(Keyboard("AZERTY", 1, [['a','z','e','r','t','y','u','i','o','p'],['q','s','d','f','g','h','j','k','l','m'],['w','x','c','v','b','n']]))
startTime = PrintTime("Constructing keyboards", startTime)

#Build dictionary of chars
keyDictionary = dict([])
for i in range(len(keyboardList)):
    for j in range(len(keyboardList[i].keyboard)):
        for k in range(len(keyboardList[i].keyboard[j])):
            if not keyboardList[i].keyboard[j][k] in keyDictionary:
                keyDictionary[keyboardList[i].keyboard[j][k]] = [[i, j]]
            else:
                keyDictionary[keyboardList[i].keyboard[j][k]].append([i, j])
startTime = PrintTime("Building character dictionary", startTime)

#Get list of words
try:
    with open(input("\nRead from file: "),'r') as textFile:
        startTime = time.time() #Reset time after input statement
        wordList = textFile.readlines()
except:
    print("File not found")
    raise SystemExit
startTime = PrintTime("Importing word list", startTime)

#Gather row data
result = [] #[["word1",[[keyboard1,[row1,row2,...]],[[keyboard2,[row1,row2,...]],...],["word2",[[keyboard1,[row1,row2,...]],[[keyboard2,[row1,row2,...]],...],...]
for i in range(len(wordList)): #For every word
    result.append([wordList[i],[]]) #Create a new entry for that word in result, containing the word as a string and a list of results for every keyboard
    for j in range(len(keyboardList)): #For every keyboard
        result[i][1].append([j,[]]) #Create a new entry in the list of results for every keyboard containing the index of the keyboard and an ordered list of the rows the letters are on
    for j in range(len(wordList[i])): #For every letter in the word
        if not wordList[i][j] in charIgnoreSet: #If this isn't an ignored character
            if wordList[i][j] in keyDictionary: #If there is at least one keyboard with this key
                rowData = keyDictionary[wordList[i][j]] #Get a list of pairs consisting of a keyboard and the row that letter is on on that keyboard from the dictionary
                index = 0 #Set the rowData index to 0 (a seperate index is needed as some keyboards may be missing from the rowData because they don't have a particular key)
                for k in range(len(keyboardList)): #For every keyboard
                    if k == rowData[index][0]: #If that keyboard has this letter
                        result[i][1][k][1].append(rowData[index][1]) #Append the row to the list in the entry for the keyboard in the entry for the word
                        index += 1 #Increment the index for rowData by one, as the current element has now been coupled to a keyboard we've already processed
                        if index == len(rowData): #If every keyboard that has the key has been processed
                            for l in range(k + 1, len(keyboardList)): #For all other keyboards
                                result[i][1][l][1].append(-1) #Append a -1 to the list in the entry for the keyboard in the entry for the word
                            break #Stop the loop for this letter
                    else: #If this keyboard doesn't have this letter
                        result[i][1][k][1].append(-1) #Append a -1 to the list in the entry for the keyboard in the entry for the word
                        #Don't increment the index for rowData, as this keyboard didn't have the key and is therefore not present in rowData
            else: #If no keyboard has this key
                for k in range(len(keyboardList)): #For every keyboard
                    result[i][1][k][1].append(-1) #Append a -1 to the list in the entry for the keyboard in the entry for the word
startTime = PrintTime("Gathering row data", startTime)

#Test functions
def RowCountTest(resultList):
    """Returns a list of lists representing the number of words that can be typed on each row on the keyboard at that index of the output list"""
    output = [] #Prepare the output list
    for i in range(len(keyboardList)): #For every keyboard
        output.append([]) #Make an entry for that keyboard
        for j in range(len(keyboardList[i].keyboard)): #For every row on the keyboard
            output[i].append(0) #Add a counter for that row
    for i in range(len(resultList)): #For every word in the result list
        for j in range(len(resultList[i][1])): #For every keyboard in the entry for that word
            """Test if everything is on the same row"""
            if len(resultList[i][1][j][1]) > 0: #If there are rows to check
                hold = resultList[i][1][j][1][0] #The element everything will be checked against is the first one
                same = (hold != -1) #If that one is -1 it means that the word cannot be typed on this keyboard and therefore the test should always fail
                for k in range(1, len(resultList[i][1][j][1])): #For every entry in the row list
                    if resultList[i][1][j][1][k] != hold: #If it is not identical to the first entry
                        same = False #Fail the test
                """Increment by one if it is"""
                if same: #If the test is passed
                    output[resultList[i][1][j][0]][hold] += 1 #Increment the count of that row by one
    return output #Return results

#Perform tests
rowCountResults = RowCountTest(result)
allCountResults = SumSubLists(rowCountResults)

print("\nSingle row test:")
for i in range(len(keyboardList)):
    print("Keyboard {} can type {} words on one row, which is {}% of all tested words.".format(keyboardList[i].name, allCountResults[i], round(100*allCountResults[i]/len(wordList), 5)))

print("\nHome row test:")
for i in range(len(keyboardList)):
    print("Keyboard {} can type {} words on the home row, which is {}% of all tested words.".format(keyboardList[i].name, rowCountResults[i][keyboardList[i].homeRow], round(100*rowCountResults[i][keyboardList[i].homeRow]/len(wordList), 5)))

print("\nAll row overview:")
for i in range(len(keyboardList)):
    for j in range(len(keyboardList[i].keyboard)):
        print("Keyboard {} can type {} words on row {}, which is {}% of all tested words.".format(keyboardList[i].name, rowCountResults[i][j], j, round(100*rowCountResults[i][j]/len(wordList), 5)))
    print("") #Print empty line
