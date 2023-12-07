with open("inputs.txt") as file:
    Lines = file.readlines()

gamePowerList = []

for line in Lines:
    gameNumber = int("".join(filter(str.isdigit, line[:line.find(":")]) ))
    gameRecords = line[line.find(":")+1:].split(";")
    gameMaxDict = {}
    for gameRecord in gameRecords:
        for entry in gameRecord.split(","):
            entryNum = int("".join(filter(str.isdigit, entry)))
            entryKey = "".join(filter(str.isalpha, entry))
            if entryNum > gameMaxDict.get(entryKey,0):
                gameMaxDict[entryKey] = entryNum
    power = 1
    for i in gameMaxDict.values():
        power *= i
    gamePowerList.append(power)

sum = 0
for i in gamePowerList:
    sum += i
print(sum)
