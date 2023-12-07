with open("inputs.txt") as input_file:
    Lines = input_file.readlines()

replaceDict = {"one": "one1one",
               "two": "two2two",
               "three": "three3three",
               "four": "four4four",
               "five": "five5five",
               "six": "six6six",
               "seven": "seven7seven",
               "eight": "eight8eight",
               "nine": "nine9nine"}

def dictReplace (string_in):
    for i,j in replaceDict.items():
        string_in = string_in.replace(i, j)
    return string_in

sum = 0
for line in Lines:
    print(line)
    line = dictReplace(line)
    print(line)
    line = "".join( filter(str.isdigit, line) )
    print(line)
    line = line[0] + line[-1]
    print(line)
    sum += int(line)

print(sum)
