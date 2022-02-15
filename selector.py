import random, time, datetime

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
    date = datetime.date(int(date[2]),int(date[1]),int(date[0]))
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
        rowsTried = []
        while not end:
            row = random.randint(0, rowNo)
            Artist, Venue, Price, Day, Date, Support, output = prRow(row)
            date = conv(Date)
            if not row in rowsTried:
                acceptable = True # All following statements should return in false, could be a function tbh
                if len(venue_A) > 0 and not Venue in venue_A: #A good example of the Acceptable Conditions
                    acceptable = False
                if len(venue_B) > 0 and Venue in venue_B:
                    acceptable = False
                if len(day_A) > 0 and not Day in day_A: 
                    acceptable = False
                if len(day_B) > 0 and Day in day_B:
                    acceptable = False
                if len(date_A) > 0 and not Date in date_A: 
                    acceptable = False
                if len(date_B) > 0 and Date in date_B:
                    acceptable = False
                if price_Max > 0.0:
                    if convert(Price) > price_Max:
                        acceptable = False
                if isinstance(date_Max, datetime.date):
                    if conv(Date) > date_Max:
                        acceptable = False
                if isinstance(date_Min, datetime.date):
                    if conv(Date) < date_Min:
                        acceptable = False
                if conv(Date) < datetime.date.today():
                    acceptable = False
                if row in rowList:
                    acceptable = False
            if acceptable:
                end = True
            elif not row in rowsTried: # something is wrong here but I don't know what yet
                rowsTried.append(row)
                if len(rowsTried) >= rowNo:
                    print("We've tried all the options, and none of them fit your critera, sorry!")
                    raise SystemExit
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
operation = ""
operand = ""
state = "START" #Largely just for info & acceptable values.
row = -1
# These are largely just for my use:
states = ("START","OPERATION","OPERAND","RUNNING","OUTPUT")
operationList = ("BAN","ACCEPT","MAX","MIN")
# Next comes a list of... lists (tuples) setting expected values for each variable
launch = ("go","launch","g","Go","Go!","go!","","GO!")
end = ("y", "stop", "Stop", "STOP", "end", "Y", "yes", "Yes")
accept = ("limit","Limit","LIMIT","limit.","Limit.","add","Add","ADD","Add.","ADD.","ADD!","Add!","add.","add!")
ban = ("ban","Avoid","ban.","Avoid.","BAN","BAN!","Ban")
no = ("no", "No", "NO", "no.", "No.", "NO.", "no!", "No!", "NO!","n","N")
maxx = ("max","MAX","Max","max.","MAX.","Max.","max!","MAX!","Max!") # This is a stupid name for max to avoid naming after a builtin
minn = ("min","MIN","Min","min.","MIN.","Min.","min!","MIN!","Min!") # This is a stupid name for min to avoid naming after a builtin
days = ("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday")
operandList = ("date","venue", "price", "day") # should be another list of lists to permit different spelling
# Next come some aggregate lists for overall vverification
a = launch + end + ban + accept + no + maxx + minn
b = a + ("date","venue","day")
c = a + ("date","price")
d = a + operandList
#Now come the list of (list) lists for each variable. 
rowList = []
venue_A = [] #Acceptable Venues
venue_B = [] #Unacceptable Venues
day_A = []
day_B = []
date_A = [] 
date_B = []
date_Max = False
date_Min = False
price_Max = 0.0
print("If you would like to make a list of acceptable date(s) or venue(s), type \"Add\".")
print("If you would like to ban a particular venue(s) or date(s) type \"Ban\".")
print("Or, if you'd like to set a maximum price or latest date, type \"Max\", or if you'd like an earliest date, type \"Min\"") # needs code for Max and Min
print("If you would like to just get going, type \"Go!\"")
while loop:
    box = input()
    if state == "START":
        if not box in a:
            print("I think you may have mis-typed, \nPlease try again.")
    elif state == "OPERATION":
        if operation in ("BAN","ACCEPT"):
            if not box in b:
                print("I think you may have mis-typed, \nPlease try again.")
        if operation in ("MAX","MIN"):
            if not box in c:
                print("I think you may have mis-typed, \nPlease try again.")
    elif state == "OPERAND": 
        if not box in d:
            if operand == "date":
                try:
                    box = conv(box) 
                except:
                    print("There was an error with the date format. Please input as \"DD/MM/YYYY\":")
                else:
                    if operation == "ACCEPT":
                        if box in date_A:
                            print("You've already added that one ;)")
                        else:
                            date_A.append(box)
                    if operation == "BAN":
                        if box in date_A:
                            print("You've already added that one ;)")
                        else:
                            date_B.append(box)
                    if operation == "MAX":
                        date_Max = box
                    if operation == "MIN":
                        date_Min = box
            elif operand == "price":
                try:
                    box = convert(box)
                except:
                    print("There was an error with the price format. If using a currency other than £ please ommit the symbol")
                else:
                    if price_Max > 0 and box > price_Max:
                        print("Max price raised to £" + box + "from £" + price_Max + ".")
                    elif price_Max > 0 and box < price_Max:
                        print("Max price lowered to £" + box + "from £" + price_Max + ".")
                    else:
                        print("Max price set at £" + box)
                    price_Max = box - 0.01
            elif operand == "day":
                if box in days:
                    if operation == "ACCEPT":
                        if box in day_A:
                            print("You've already added that one ;)")
                        else:
                            day_A.append(box)
                    if operation == "BAN":
                        if box in day_B:
                            print("You've already added that one ;)")
                        else:
                            day_B.append(box)
                else:
                    print("Please type what day of the week it is with a capital letter e.g. Monday, Tuesday etc.")
            elif operand == "venue":
                if operation == "ACCEPT":
                    venue_A.append(box)
                    print("Added " + box + " to the list of venues you would like to attend.")
                    print("Please note: The venue name must be typed idenically for it to work.")
                if operation == "BAN":
                    venue_B.append(box)
                    print("Added " + box + " to the list of venues you would like to avoid.")
                    print("Please note: The venue name must be typed idenically for it to work.")
    elif state == "OUTPUT": 
        if box in (end + no):
            pass
        elif not box in operandList:
            print("Sorry, please type one of the following:")
            print(operandList)
        else:
            if box == "date":
                date_B.append(Date)
            elif box == "venue":
                venue_B.append(Venue)
            elif box == "price":
                if price_Max > 0 and Price > price_Max:
                    print("Max price raised to £" + Price + "from £" + price_Max + ".")
                elif price_Max > 0 and Price < price_Max:
                    print("Max price lowered to £" + Price + "from £" + price_Max + ".")
                else:
                    print("Max price set at " + Price)
                price_Max = convert(Price)
            elif box == "day":
                day_B.append(Day)
            else:
                print("WTF have you managed?")
                raise "operandList missaligned"
    else:
        print("Something has gone wrong, please try again.")
        raise "Variable \"state\" missaligned"
    if box in accept:
        state = "OPERATION"
        operation = "ACCEPT"
        print("What would you like to limit?\n(You can do more than one, just type the next one when you're done adding)")
        print("\"date\",\"venue\" or \"day\"")
    if box in ban:
        state = "OPERATION"
        operation = "BAN"
        print("Type the name of the category you would like to avoid:")
        print("\"date\", \"venue\" or \"day\"")
    if box in maxx:
        state = "OPERATION"
        operation = "MAX"
        print("Would you like to set a latest date or a maximum price?")
    if box in minn:
        state = "OPERATION"
        operation = "MIN"
        state = "OPERAND"
        operand = "date"
        print("When would you like the earliest date to be?")
        print("Please use the format \"DD/MM/YYYY\"")
    if state != "OUTPUT":
        if box == "date": #should be changed to in
            state = "OPERAND"
            operand = "date"
            if operation == "ACCEPT":
                print("What date(s) would you like to go?")
            if operation == "BAN":
                print("What dates would you like to avoid?")
            if operation == "MAX":
                print("When's the latest date you'd like to go?")
            print("Please use the format \"DD/MM/YYYY\"")
        if box == "venue": #should be changed to in
            state = "OPERAND"
            operand = "venue"
            if operation == "ACCEPT":
                print("Where would you like to go?")
            if operation == "BAN":
                print("Where would you like to avoid?")
            print("Please note: The venue name must be typed idenically for it to work.")
        if box == "day": #should be changed to in
            state = "OPERAND"
            operand = "day"
            if operation == "ACCEPT":
                print("What day(s) of the week would you like to go?")
            if operation == "BAN":
                print("What day(s) of the week can't you go?")
            print("Please type the day in with a capital letter e.g.\"Friday\".")
        if box == "price": #should be changed to in
            state = "OPERAND"
            operand = "price"
            if operation == "MAX":
                print("What is the maximum you're wiling to pay?")
            print("BTW, I've only accounted for £s so don't bother with any other symbols please.")
    if box in launch:
        state = "RUNNING"
        Artist, Venue, Price, Day, Date, Support, row = other(100,0)
        state = "OUTPUT"
        print("Is this ok?")
    if box in no and row != -1: # This handles an early no. Could me moved up with an If state 
        rowList.append(row)
        if len(rowList) >= rowNo:
            End = False
            while not End:
                print("I'm afraid there's no other option, would you like to reset?")
                box = input("Y/N?   ")
                if box == "Y":
                    rowList = []
                    state = "START"
                    End = True
                elif box == "N":
                    print("Aright then, suit yourself!")
                    loop = False
                    print("LOL")
                    End = True
                else:
                    print("I'm sorry, it has to be either \"Y\" or \"N\".")
        else:
            print("Would you like to add the venue, day or date to the \"ban\" list or set a new max price?")
            End = False
            while not End:
                box = input("Y/N?   ")
                if box == "Y":
                    End = True
                    box = "loop"
                elif box == "N":
                    state = "START"
                    End = True
                else:
                    print("I'm sorry, it has to be either \"Y\" or \"N\".")
    elif box in no: # This handles an early no. Could me moved up with an If state 
        print("I think you may have mis-typed, \nPlease try again.")
    if box in end:
        print("Thank you!")
        loop = False