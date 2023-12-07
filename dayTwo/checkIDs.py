with open("inputs.txt") as file:
    Lines = file.readlines()

REDMAX = 12
GREENMAX = 13
BLUEMAX = 14

def keyFilter (i):
    if i == "red" or i == "green" or i == "blue":
        return False
    else:
        return True

def validateRecords(gameRecords):
    for record in gameRecords:
        recordDict = {}
        for entry in record.split(","):
            recordDict["".join(filter(str.isalpha, entry))] = int("".join(filter(str.isdigit, entry)))
        if not filter(keyFilter, recordDict.keys()):
            return False
        if recordDict.get("red",0) > REDMAX or recordDict.get("green",0) > GREENMAX or recordDict.get("blue",0) > BLUEMAX:
            return False
    return True


# Define a gamebook to keep track of games
gameBook = []
# Parse each game into a game number and set of records
for line in Lines:
    gameNumber = int("".join(filter(str.isdigit, line[:line.find(":")]) ))
    gameRecords = line[line.find(":")+1:].split(";")
    if validateRecords(gameRecords):
        gameBook.append(gameNumber)
sum = 0
for i in gameBook:
    sum += i
print(sum)
    
