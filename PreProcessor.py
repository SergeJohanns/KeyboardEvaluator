"""
This script does pre-processing of text files for the keyboard evaluator.
It creates a new variant of a given text file that meets the requirements
for input  files for the evaluator.  This means all words have to be on a
seperate line, all-lowercase and, optionally, all-alpha. If the words are
not all-alpha and the keyboards have not been modified to be able to type
non-alpha characters the evaluator will simply ignore them in the report.
"""

fileName = input("File to process: ")
fileNamePrefix, fileNameSuffix = fileName.split('.')[0], fileName.split('.')[1]
onlyAlpha = input("Filter non-alpha characters? (y/n): ") == 'y'
words = []

with open(fileName, 'r') as readFile:
    lineList = readFile.readlines()
    for line in lineList:
        words.extend(line.split())

for i in range(len(words)):
    words[i] = words[i].lower()
words.sort()
output = [words[0]]
hold = words[0]
for i in range(1, len(words)):
    if words[i] != hold:
        output.append(words[i])
        hold = words[i]
words = output
if onlyAlpha:
    output = []
    for i in range(len(words)):
        if words[i].isalpha():
            output.append(words[i])
    words = output
    
with open(fileNamePrefix + "_processed." + fileNameSuffix, 'w') as outputFile:
    for i in range(len(words)):
        outputFile.write(words[i] + '\n')
