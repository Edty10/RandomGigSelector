import random, time, datetime
from re import T

with open('Gigs.csv', encoding='utf_8') as file: # this will need to be changed to whatever you've named your file... or just name it gigs.csv
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
    if type(Support) == str and Support == "TBC\n":
        output = Artist + " (Support TBC)\n" + Venue + "\n"
    elif type(Support) == str and len(Support) > 1:
        output = Artist + " supported by " + Support + Venue + "\n"
    else:
        output = Artist + "\n" + Venue + "\n"
    output = output + Day + " " + Date + "\n" + Price
    return Artist, Venue, Price, Day, Date, Support, output

def convert(Price):
    price = float(Price.replace("£",""))
    return price

def conv(Date):
    date = Date.split("/")
    date = datetime.datetime(int(date[2]),int(date[1]),int(date[0]))
    return date

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
        if lineNo > 13:
            print(output)
            increase = False
        elif lineNo > 0:
            print(Line)

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
        acceptable = False
        end = False
        while not end:
            row = random.randint(0, rowNo)
            Artist, Venue, Price, Day, Date, Support, output = prRow(row)
            date = conv(Date)
            acceptable = True
            if len(venue_A) > 0 and not Venue in venue_A:
                acceptable = False
            if prices > 0.0:
                if convert(Price) > prices:
                    acceptable = False
            if len(venue_B) > 0 and Venue in venue_B:
                acceptable = False
            if row in rowList:
                acceptable = False
            if acceptable:
                end = True    
        draw(output)
        if delay > 0.3:
            top = round(100 * (delay - 0.3))
            r = random.randint(0,top)
            if r > 50:
                coin = True
                speed = 0
    return Artist, Venue, Price, Day, Date, Support, row # So if the answer is no it can be added to a list

loop = True
box = "loop"
launch = ("go","launch","g","Go","Go!","go!","","GO!")
end = ("y", "stop", "Stop", "STOP", "end", "Y", "yes", "Yes")
avoid = ("avoid","Avoid","avoid.","Avoid.")
please = ("limit","Limit","LIMIT","limit.","Limit.")
no = ("no", "No", "NO", "no.", "No.", "NO.", "no!", "No!", "NO!","n","N")
a = launch + end + avoid + please + no
rowList = []
venue_A = []
venue_B = []
prices = 0.0
row = -1
print("If you would like to limit to one date or venue, type \"limit\".")
print("If you would like to restrict price, or avoid a particular venue, type \"Avoid\".")
print("If you would like to just get going, type \"Go!\"")
while loop:
    box = input()
    if not box in a:
        print("I think you may have mis-typed, \nPlease try again.")
    if box in please:
        print("Are you after a particular date or ")
    if box in avoid:
        print("Type the name of the catagory you would like to restrict:")
    if box in launch:
        Artist, Venue, Price, Day, Date, Support, row = other(100,0)
        print("Is this ok?")
    if box in no and row != -1:
        rowList.append(row)
        if len(rowList) >= rowNo:
            End = False
            while not End:
                print("I'm afraid there's no other option, would you like to reset?")
                box = input("Y/N?")
                if box == "Y":
                    rowList = []
                    End = True
                elif box == "N":
                    print("Aright then, suit yourself!")
                    loop = False
                    print("LOL")
                    End = True
                else:
                    print("I'm sorry, it has to be either \"Y\" or \"N\".")
        else:
            print("What is wrong with it?")
    elif box in no:
        print("I think you may have mis-typed, \nPlease try again.")
    if box in end:
        print("Thank you!")
        loop = False