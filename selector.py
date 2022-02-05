import random, time

with open('Gigs.csv') as file:
    content = file.readlines()

header = content[:1]
rows = content[1:]
rowNo = len(rows) - 1

def prRow(row):
    thisRow = rows[row]
    thisRow = thisRow.split(',')
    Artist = thisRow[0]
    Venue = thisRow[1]
    Price = thisRow[2]
    Day = thisRow[3]
    Date = thisRow[4]
    Support = thisRow[5]
    if type(Support) == str and len(Support) > 1:
        output = "Venue: " + Venue + ", Artist: " + Artist + " supported by " + Support
    elif type(Support) == str and Support == "TBC":
        output = "Venue: " + Venue + ", Artist: " + Artist + " support TBC"
    else:
        output = "Venue: " + Venue + ", Artist: " + Artist + "\n"
    output = output + Day + " " + Date + "\n" + Price
    return Artist, Venue, Price, Day, Date, Support, output

top = "_\n__\n___\n____\n_____\n______\n_______\n________\n_________\n__________\n___________\n____________\n_____________\n______________"
bottom = "‾‾‾‾‾‾‾‾‾‾‾‾‾‾\n‾‾‾‾‾‾‾‾‾‾‾‾‾\n‾‾‾‾‾‾‾‾‾‾‾‾\n‾‾‾‾‾‾‾‾‾‾‾\n‾‾‾‾‾‾‾‾‾‾\n‾‾‾‾‾‾‾‾‾\n‾‾‾‾‾‾‾‾\n‾‾‾‾‾‾‾\n‾‾‾‾‾‾\n‾‾‾‾‾\n‾‾‾‾\n‾‾‾\n‾‾\n‾"

def other(speed, delay):
    i = 0
    coin = False
    while delay < 0.5:
        speed_round = round(speed)
        top = speed_round + i
        bottom = i
        r = random.randint(bottom,top) / (speed * (top))
        if delay > 0.3:
            r = r * (10 * delay)
        delay = delay + r
        time.sleep(delay)
        speed = speed - (10 * r)
        i = i + 1
        row = random.randint(0, rowNo)
        Artist, Venue, Price, Day, Date, Support, output = prRow(row)
        draw(output)
        if delay > 0.3:
            top = round(100 * (delay - 0.3))
            r = random.randint(0,top)
            if r > 50:
                coin = True
                speed = 0


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

loop = True
box = "loop"
launch = ["go","launch","g","Go","Go!","go!"]
while loop:
    box = input()
    if box == "go":
        other(100,0)
        print("Bing!")
    if box == "stop":
        loop = False