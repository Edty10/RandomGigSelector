import random, time

with open('Gigs.csv') as file:
    content = file.readlines()

header = content[:1]
rows = content[1:]
rowNo = len(rows)

def prRow(row):
    thisRow = rows[row]
    thisRow = thisRow.split(',')
    Artist = thisRow[0]
    Venue = thisRow[1]
    Price = thisRow[2]
    Day = thisRow[3]
    Date = thisRow[4]
    Support = thisRow[5]

top = "_\n__\n___\n____\n_____\n______\n_______\n________\n_________\n__________\n___________\n____________\n_____________\n______________"
bottom = "‾‾‾‾‾‾‾‾‾‾‾‾‾‾\n‾‾‾‾‾‾‾‾‾‾‾‾‾\n‾‾‾‾‾‾‾‾‾‾‾‾\n‾‾‾‾‾‾‾‾‾‾‾\n‾‾‾‾‾‾‾‾‾‾\n‾‾‾‾‾‾‾‾‾\n‾‾‾‾‾‾‾‾\n‾‾‾‾‾‾‾\n‾‾‾‾‾‾\n‾‾‾‾‾\n‾‾‾‾\n‾‾‾\n‾‾\n‾"

def draw(output):
    increase = True
    lineNo = 0
    drawLoop = True
    while drawLoop:
        if increase:
            line = "_"
            lineNo = lineNo + 1
        else:
            line = "‾"
            lineNo = lineNo - 1
        if lineNo == 0:
            drawLoop = False
        n = 1
        Line = line
        while n < lineNo:
            Line = Line + line
            n = n + 1
        if lineNo > 15:
            print(output)
            increase = False
        elif lineNo > 0:
            print(Line)
        #Add a time.sleep

loop = True
box = "loop"
launch = ["go","launch","g","Go","Go!","go!"]
while loop:
    box = input()
    if box == "go":
        speed = 5
        while speed >0:
            output = "test"
            draw(output)
            #add speed slower