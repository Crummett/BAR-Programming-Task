import sys

def main():
    
    inputNames, surnamesFile = getInputs()
    surnames = open(surnamesFile, 'r').read().splitlines()
    output = ""
    for name in inputNames:
        output = output + match(name, surnames) + '\n'
    output = output[:-2]
    print(output)
    
def getInputs():
    
    inputNames = sys.argv[1:(len(sys.argv)-1)]
    surnamesFile = sys.argv[(len(sys.argv)-1)]
    
    return inputNames, surnamesFile
    
def match(nameFromCMD, surnamesFileContents):
    
    nameInput, surnamesList = nameFromCMD, surnamesFileContents
    equivalents = generateEquivalents()
    
    name = disregarder(treat(nameInput), equivalents)
    matches = []
    for surname in surnamesList:
        surnameToCheck = disregarder(treat(surname), equivalents)
        if (compareEquivalents(name, surnameToCheck, equivalents)):
            matches.append(surname)
    
    output = nameInput + ':'
    try:
        for match in matches:
            output = output + ' ' + match + ','
    except IndexError:
        output = output + ' No matches found'
    output = output[:-1]
    return output

def compareEquivalents(nameInput, surnameInput, equivalentsDictionary):
    name, surname, equivalents = nameInput, surnameInput, equivalentsDictionary
    finished, equivalent = False, True
    
    while (not finished):
        for i in range(len(surname)):
            try:
                if (surname[i] not in equivalents[name[i]]):
                    finished, equivalent = True, False
            except IndexError:
                finished, equivalent = True, False
        finished = True
    
    return equivalent
    
def treat(nameInput):
    
    name = nameInput.lower()
    treatedName = ""
    
    for letter in name:
        if letter.islower():
            treatedName = treatedName + letter
    
    return treatedName
    
def disregarder(nameInput, equivalentsDictionary):
    name, equivalents = nameInput, equivalentsDictionary
    firstStage = name[0]
    for letter in name[1:]:
        if (letter not in ['a', 'e', 'i', 'h', 'o', 'u', 'w', 'y']):
            firstStage = firstStage + letter
    
    secondStage = name[0]
    for letterNum in range(1, len(firstStage)):
        if (firstStage[letterNum] not in equivalents[firstStage[letterNum-1]]):
            secondStage = secondStage + firstStage[letterNum]
    
    return secondStage
    
def generateEquivalents():
    # Creates a dictionary of equivalents.
    # Enter a letter into the dictionary, and it'll return a list of all of its equivalents
    equiv1 = {x: ['a', 'e', 'i', 'o', 'u' ] 
        for x in ['a', 'e', 'i', 'o', 'u' ]}
    equiv2 = {x: ['c', 'g', 'j', 'k', 'q', 's', 'x', 'y', 'z'] 
        for x in ['c', 'g', 'j', 'k', 'q', 's', 'x', 'y', 'z']}
    equiv3 = {x: ['b', 'f', 'p', 'v', 'w'] 
        for x in ['b', 'f', 'p', 'v', 'w']}
    equiv4 = {x: ['d', 't'] 
        for x in ['d', 't']}
    equiv5 = {x: ['m', 'n'] 
        for x in ['m', 'n']}
    equiv6 = {x: []
        for x in ['h', 'l', 'r']}
    # Create 1 mega-dictionary
    equiv1.update(equiv2)
    equiv1.update(equiv3)
    equiv1.update(equiv4)
    equiv1.update(equiv5)
    equiv1.update(equiv6)
    
    return equiv1

main()