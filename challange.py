def readFile(filename):
    inputs = []
    with open(filename) as infile:
        for line in infile:
            if line:
                remaining = line.split("-",1)
                if len(remaining)==2:
                    input = []
                    minOccurance = remaining[0]
                    input.append(minOccurance)
                    remaining = remaining[1].split(" ",1)
                    maxOccurance = remaining[0]
                    input.append(maxOccurance)
                    remaining = remaining[1].split(":",1)
                    letter = remaining[0]
                    input.append(letter)
                    remaining = remaining[1].split(" ",1)
                    remaining = remaining[1].split("\\")
                    password = remaining[0]
                    input.append(password)
                    inputs.append(input)
                                         
    return inputs

def checkCorrectness(inputs):
    validPasswords = 0
    for input in inputs:
        numberOfOccurances = input[3].count(input[2])
        if numberOfOccurances >= int(input[0]) and numberOfOccurances <= int(input[1]):
            validPasswords += 1
    return validPasswords


inputs = readFile("inputFile.rtf")
print("Number of valid passwords are:",checkCorrectness(inputs))

